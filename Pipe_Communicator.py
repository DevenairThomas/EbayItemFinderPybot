import os 
import datetime
import time
import sys
import types
import win32pipe, win32file, pywintypes

class PipeCommunicator(object):
    #Connection Status boolean
    Connection = False
    #Create handle as an Empty Object for a win32file object
    handle = types.SimpleNamespace()
    #String object for the OK message
    okResponse = "OK\r\n"
    #String object for the SUCCESS message
    successResponse = "SUCCESS\r\n"
    
    #List of messages recieved from the host
    msgRecievedList = []
    #List of messages to send to the host
    msgSendList = []
    
    #add messages recieved from the host to the list
    def addRecievedMessageList(self, string):
        self.msgRecievedList.append(string)
    
    #add messages to send to the host to the list
    def addSendMessageList(self, string):
        self.msgRecievedList.append(string)
        
    #get messages from the Send Message List and  deletes them from the list
    def retrieveMessageFromSendMessageList(self):
        returnString = self.msgRecievedList[0]
        self.msgRecievedList.remove[0]
        if (self.msgRecievedList.len()<1):
            return False
        return returnString
       
    #Open a pipe server and wait for a connection from the host
    #If a connection is made, the pipe server will send the OK message to the host
    #If the host sends a message, the pipe server will add the message to the recieved message list
    #If the host sends the END message, the pipe server will send the SUCCESS message to the host and close the connection 
    def recieveDataFromHost(self, pipeName):
        INIT_RESPONSE = self.CONNECT_TO_PIPE_SERVER_AS_CLIENT(pipeName)
        INIT_RESPONSE_STRING = INIT_RESPONSE[1]
        if(INIT_RESPONSE_STRING == "CONNECTION"):
            self.Connection = True
            response = str.encode(f"{self.okResponse}")
            win32file.WriteFile(self.handle, response)
        while (self.Connection == True):
            resp = win32file.ReadFile(self.handle, 64*1024)
            self.createRecievedMessageList(resp)
            if(response != "END\r\n"):
                win32file.WriteFile(self.handle, response)
            else:
                self.Connection = False
        response = str.encode(f"{self.successResponse}")
        win32file.WriteFile(self.handle, response) 
    
    #Open a pipe server and wait for a connection from the host
    def CONNECT_TO_PIPE_SERVER_AS_CLIENT(self,pipeName):
        print("PIPE CLIENT")
        quit = False
        while not quit:
            try:
                self.handle = win32file.CreateFile(
                    pipeName,
                    win32file.GENERIC_READ | win32file.GENERIC_WRITE,
                    0,
                    None,
                    win32file.OPEN_EXISTING,
                    0,
                    None
                )
                self.handle = win32pipe.SetNamedPipeHandleState(self.handle, win32pipe.PIPE_ACCESS_DUPLEX, win32pipe.PIPE_TYPE_MESSAGE | win32pipe.PIPE_WAIT, None)
                win32pipe.ConnectNamedPipe(self.handle, None)
                if self.handle == 0:
                    print(f"SetNamedPipeHandleState return code: {res}")
                while True:
                    resp = win32file.ReadFile(self.handle, 64*1024)
                    return resp
                    #print(f"message: {resp}")
            except pywintypes.error as e:
                if e.args[0] == 2:
                    print("NO PIPE, RETRY")
                    time.sleep(1)
                elif e.args[0] == 109:
                    print("NO CONNECTION")
                    quit = True
                    
    
    def PIPE_SERVER(self):
        print("Connecting to Pipe Server...")
        SUCCESS = False
        pipe = win32pipe.CreateNamedPipe(
            r'\\.\pipe\Foo',
            win32pipe.PIPE_ACCESS_DUPLEX,
            win32pipe.PIPE_TYPE_MESSAGE | win32pipe.PIPE_READMODE_MESSAGE | win32pipe.PIPE_WAIT,
            1, 65536, 65536,
            0,
            None)
        try:
            print("Trying to Connect To Host...")
            win32pipe.ConnectNamedPipe(pipe,None)
            print("Host Connection Success")
            
            while self.msgSendList.len() >= 0:
                print(f"Writing to Host...")
                sendMessage = self.retrieveMessageFromSendMessageList(self)
                if(sendMessage == False):
                    break
                some_data = str.encode(f"{sendMessage}")
                win32file.WriteFile(pipe, some_data)
                time.sleep(1)
                SUCCESS = True
            print("SUCCESS!")
        except:
            pass
        finally:
            win32file.CloseHandle(pipe)

    def PIPE_CLIENT():
        print("PIPE CLIENT")
        quit = False
        while not quit:
            try:
                handle = win32file.CreateFile(
                    r'\\.\pipe\Foo',
                    win32file.GENERIC_READ | win32file.GENERIC_WRITE,
                    0,
                    None,
                    win32file.OPEN_EXISTING,
                    0,
                    None
                )
                res = win32pipe.SetNamedPipeHandleState(handle, win32pipe.PIPE_READMODE_MESSAGE, None, None)
                if res == 0:
                    print(f"SetNamedPipeHandleState return code: {res}")
                while True:
                    resp = win32file.ReadFile(handle, 64*1024)
                    print(f"message: {resp}")
            except pywintypes.error as e:
                if e.args[0] == 2:
                    print("no pipe, trying again in a sec")
                    time.sleep(1)
                elif e.args[0] == 109:
                    print("broken pipe, bye bye")
                    quit = True