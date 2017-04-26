import time
from AutoTranscript import AutoTranscript
from settings import GAccountInfo


user = GAccountInfo['username']
password = GAccountInfo['password']
doc_name = "Prueba 1"

autoTranscript = AutoTranscript(user,password)
autoTranscript.login()
autoTranscript.createGDoc(doc_name)
autoTranscript.startTranscribing()

#time.sleep(5)
#autoTranscript.exit()


