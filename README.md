# AI_devs-python-uFramework

Mikro framework, o którym wspominał Kuba na Q&A. Wersja Python

## Jak działa kod:
Do taskSender przekazujemy nazwę zadania i funkcję która wyprodukuje JSON odpowioedzi na podstawie pobranego JSON task.
Przykład rozwiązania zadania "helloapi"

```
def task_0():
    taskName = "helloapi"

    def task(task):
        cookie = task["cookie"]

        return {
            "answer": cookie
        }
    
    return (taskName, task)

taskSender(*task_0())
```

## Instrukcja: 
1. Sklonuj repo
2. Zainstaluj python 3
3. Stwórz i aktywuj virtual env https://realpython.com/python-virtual-environments-a-primer/
```
python3 -m venv venv
source venv/bin/activate
```
4. Zainstaluj zależności
```
python3 -m pip -r requirements.txt
```
5. Uzupełnij plik .env o klucz API z https://tasks.aidevs.pl
6. Odpal main.py i sprawdź czy działa
```
python3 main.py
```
