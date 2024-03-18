import requests
import os
from dotenv import load_dotenv

load_dotenv()

AI_DEVS_TASK_APIKEY = os.getenv("AI_DEVS_TASK_APIKEY")
TASKNAME_KEY = "\{\{TASKNAME\}\}"
TOKEN_KEY = "\{\{TOKEN\}\}"

BASE_URL = "https://tasks.aidevs.pl"
TOKEN_ENDPOINT = BASE_URL + f"/token/{TASKNAME_KEY}"
GET_TASK_ENDPOINT = BASE_URL + f"/task/{TOKEN_KEY}"
SEND_ANSWER_ENDPOINT = BASE_URL + f"/answer/{TOKEN_KEY}"

def getToken(taskName: str) -> str:
    url = TOKEN_ENDPOINT.replace(TASKNAME_KEY, taskName)
    
    payload = {
        "apikey": AI_DEVS_TASK_APIKEY
    }

    response = requests.post(url, json=payload).json()

    return response["token"]

def getTask(token: str) -> any:
    url = GET_TASK_ENDPOINT.replace(TOKEN_KEY, token)

    return requests.get(url).json()

def sendAnswer(token: str, json: any) -> requests.Response:
    url = SEND_ANSWER_ENDPOINT.replace(TOKEN_KEY, token)

    return requests.post(url, json=json)

def taskSender(taskName: str, callback):
    token = getToken(taskName)
    task = getTask(token)

    print(f"{taskName}:\n{task}")
    answer = callback(task)

    response = sendAnswer(token=token, json=answer)

    print(response)
    print(response.json())

def task_0():
    taskName = "helloapi"

    def task(task):
        cookie = task["cookie"]

        return {
            "answer": cookie
        }
    
    return (taskName, task)

taskSender(*task_0())