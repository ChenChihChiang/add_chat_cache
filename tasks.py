from celery import Celery
from kombu import Exchange, Queue
import requests
import json

backend = 'redis://redis-svc-infra:6379/0'

broker = 'redis://redis-svc-infra:6379/1'

 
CELERY_QUEUES = (
)

celery = Celery('tasks', backend=backend, broker=broker)


@celery.task
def add(x, y):
	return x + y 
 
@celery.task
def add_cache_1(question_list, url, headers):

	for i in range(len(question_list)-1):

		#print(question_list[i])

		data = {"dialog":[question_list[i]],"info":{"info":"cache"},"xiaomi":{"xiaomi":"cache"}}

		res = requests.post(url, json=data, headers=headers)

		print(data)

		#print(res)

		#print(res.text)

		#print(json.loads(res.text))


@celery.task
def add_cache_2(question_list, url, headers):

	for i in range(len(question_list)-1):

		for j in range(len(question_list)-1):

			#print(question_list[i])

			data = {"dialog":[question_list[i],question_list[j]],"info":{"info":"cache"},"xiaomi":{"xiaomi":"cache"}}

			res = requests.post(url, json=data, headers=headers)

			print(data)

			#print(res)

			#print(res.text)

			#print(json.loads(res.text))


@celery.task
def add_cache_3(question_list, url, headers):

	for i in range(len(question_list)-1):

		for j in range(len(question_list)-1):

			for k in range(len(question_list)-1):

				print(question_list[i])

				data = {"dialog":[question_list[i],question_list[j],question_list[k]],"info":{"info":"cache"},"xiaomi":{"xiaomi":"cache"}}

				res = requests.post(url, json=data, headers=headers)

				print(data)

				print(res)

				print(res.text)

				#print(json.loads(res.text))


@celery.task
def add_cache_4(question_list, url, headers):

	for i in range(len(question_list)-1):

		for j in range(len(question_list)-1):

			for k in range(len(question_list)-1):

				for m in range(len(question_list)-1):

					print(question_list[i])

					data = {"dialog":[question_list[i],question_list[j],question_list[k],question_list[m]],"info":{"info":"cache"},"xiaomi":{"xiaomi":"cache"}}

					res = requests.post(url, json=data, headers=headers)

					print(data)

					print(res)

					print(res.text)

					#print(json.loads(res.text))


@celery.task
def add_cache_5(question_list, url, headers):

	for i in range(len(question_list)-1):

		for j in range(len(question_list)-1):

			for k in range(len(question_list)-1):

				for m in range(len(question_list)-1):

					for n in range(len(question_list)-1):

						#print(question_list[i])

						data = {"dialog":[question_list[i],question_list[j],question_list[k],question_list[m],question_list[n]],"info":{"info":"cache"},"xiaomi":{"xiaomi":"cache"}}

						res = requests.post(url, json=data, headers=headers)

						print(data)

						#print(res)

						#print(res.text)

						#print(json.loads(res.text))
