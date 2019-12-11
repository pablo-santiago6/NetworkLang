import socket as sk
import _thread
import time

#server creater
def server(someIP):
    _thread.start_new_thread(nserver, ())
    time.sleep(1)
    return cl(someIP)


def nserver():
    s = sk.socket(sk.AF_INET , sk.SOCK_STREAM)
    someIP = sk.gethostbyname("0.0.0.0")
    s.bind((someIP , 8080))
    s.listen(5)


    while True:
        conn , addr = s.accept()
        from_client = ''

        while True:

            data = conn.recv(4096)
            if not data:break

            print ("\n" + "Msg recv: " + data.decode())


            # st = "hello person\n"
            # byt = st.encode()
            # conn.send(byt)

        conn.close()
        print (' client disconnect')

def cl(someIP):

    cl = sk.socket(sk.AF_INET , sk.SOCK_STREAM)
    cl.connect((someIP , 8080))
    return cl
    #sendMuch(cl)

def close(s):
    s.close()


def send(s , msg):

    byt = msg.encode()
    s.send(byt)
    # from_server = s.recv(4096)
    # print (from_server.decode)

def sendMuch(s):
    while True:

        msg = input("Enter msg: ")
        byt = msg.encode()
        s.send(byt)
        from_server = s.recv(4096)
        print (from_server.decode)

def test():
    home = "127.0.0.1"
    my_server =  server(home) # create my_server "192.168.0.10"
    send(my_server , "Hello I am Server 1"); #send
    time.sleep(1)
    send(my_server , "I will leave now , bye !")
    close(my_server)


# global home = "127.0.0.1"












# def receive(sk):
