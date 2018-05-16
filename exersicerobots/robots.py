# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     robots
   Description :
   Author :       caigao
   date：          2018/3/4 0004
-------------------------------------------------
   Change Activity:
                   2018/3/4 0004:
-------------------------------------------------
"""
__author__ = 'caigao'

import string
import time
import linecache
import random
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def ordinal_read_file(questions_path,answers_path): #顺序练习，输入exit退出
	answernum = 1
	maxline = len((open(questions_path)).readlines())+1
	try:
		with open(questions_path, 'r') as f:
			print '顺序训练加载题库'

	except:
		print '题库不存在'
	with open(questions_path, 'r') as f:
		for line in f:
			print line, '请在A B C 中选择正确答案'
			answer = raw_input() + '\n'
			real_answer = linecache.getline(answers_path, answernum)
			if real_answer == str.upper(answer):
				print '回答正确。'
				answernum += 1
				questionsnumback(answernum)
				if maxline == answernum:
					print '这是最后一题。'

				mb = raw_input()
				if mb == 'EXIT':
					exit(0)

			else:
				print '正确答案是', real_answer
				wrongback(line, real_answer)
				answernum += 1
				questionsnumback(answernum)
				if maxline == answernum:
					print '\033[1;31;40m这是最后一题。\033[0m'
				mb = raw_input()
				if mb == 'EXIT':
					exit(0)



def random_read_file(questions_path,answers_path): #随机训练
	try:
		with open(questions_path, 'r') as f:
			print '随机训练加载题库'
	except:
		print '题库不存在'
		exit(0)

	answernum = 1
	maxline = len((open(questions_path)).readlines())
	# print maxline
	questionnum = random.randint(1,maxline)
	while questionnum > 0:
		print questionnum
		question = linecache.getline(questions_path,questionnum)
		print question,'请在A B C中选择正确答案'
		answer = raw_input() + '\n'
		real_answer = linecache.getline(answers_path, questionnum)
		questionnum = random.randint(1, maxline)
		if real_answer == str.upper(answer):
			print '回答正确。'
			answernum += 1
			mb = raw_input()
			if mb == 'EXIT':
				exit(0)

		else:
			print '正确答案是', real_answer
			wrongback(question, real_answer)
			answernum += 1
			mb = raw_input()
			if mb == 'EXIT':
				exit(0)


def back_read_file(questions_path, answers_path): #从答题记录开始答题

	try:
		with open(questions_path, 'r') as f:
			print '随即训练加载题库'
	except:
		print '题库不存在'
		exit(0)

	answernum = 1
	maxline = len((open(questions_path)).readlines()) + 1
	questionnum = questionnumread()
	print ('从第{}题开始答题'.format(questionnum))
	'''
	如果有答题记录从答题记录开始答题，没有的话从头开始
	'''
	if questionnum != None:
		while questionnum > 0:
			question = linecache.getline(questions_path, questionnum)
			print question, '请在A B C中选择正确答案'
			answer = raw_input() + '\n'
			real_answer = linecache.getline(answers_path, questionnum)
			questionnum += 1
			questionsnumback(questionnum)
			if real_answer == str.upper(answer):
				print '回答正确。'
				answernum += 1
				mb = raw_input()
				if mb == 'EXIT':
					exit(0)
			else:
				print '正确答案是 ', real_answer
				wrongback(question,real_answer)
				answernum += 1
				mb = raw_input()
				if mb == 'EXIT':
					exit(0)
			if questionnum == maxline:
				questionsnumback('1')
				print '\033[1;31;40m这是最后一题。\033[0m'
				exit(0)


	else:
		ordinal_read_file(questions_path, answers_path)

def wrong_review(questions_path,answers_path): #复习错题
	try:
		with open(questions_path, 'r') as f:
			print '加载错题库'
	except:
		print '错题库不存在'
		exit(0)

	answernum = 1
	maxline = len((open(questions_path)).readlines())+1
	print maxline
	with open(questions_path, 'r') as f:
		for line in f:
			print line, '请在A B C 中选择正确答案'
			answer = raw_input() + '\n'
			real_answer = linecache.getline(answers_path, answernum)
			# print real_answer
			if real_answer == str.upper(answer):
				print '回答正确。'
				answernum += 1
				if maxline == answernum:
					print '\033[1;31;40m这是最后一题。\033[0m'
					exit(0)

				mb = raw_input()
				if mb == 'EXIT':
					exit(0)

			else:
				print '正确答案是',real_answer
				answernum += 1
				if maxline == answernum:
					print '\033[1;31;40m这是最后一题。\033[0m'
					exit(0)
				mb = raw_input()
				if mb == 'EXIT':
					exit(0)

def practice_exam(questions_path,answers_path,n=100,p=80): #模拟考试
	try:
		with open(questions_path, 'r') as f:
			print '正在抽取试题'
	except:
		print '题库不存在'
		exit(0)

	print '考试开始,开始计时'
	time_start = time.time()
	maxline = len((open(questions_path)).readlines())+1
	random_list = random.sample([x for x in range(1,maxline)],n) #默认随机选择100道题作为考试内容
	j = 1
	points = 0
	for i in random_list:
		question = linecache.getline(questions_path,i)
		print '\n第{}题'.format(j)
		print question,'请在A B C中选择正确答案'
		answer = raw_input() + '\n'
		real_answer = linecache.getline(answers_path, i)
		if real_answer == str.upper(answer):
			points += 1
			print '回答正确。'

		else:
			wrongback(question, real_answer)
			print '回答错误,正确答案是 ', real_answer
		j += 1
		time_run = (time.time() - time_start) / 60
		if time_run >= 120:
			print '答题时间到，考试结束。'
			print '总分 {} 分'.format(points)
			if points >= p:
				print '考试合格，再接再厉\n'
			else:
				print '考试不合格，请继续练习\n'

			break

		if j == n+1:

			print '答题结束，总分 {} 分'.format(points)
			print '耗时 {:d} 分钟\n'.format(int(time_run))
			if points >= p:
				print '考试合格，再接再厉\n'
			else:
				print '考试不合格，请继续练习\n'


def wrongback(question,answer): #记录答错的题目和正确答案
	with open('wrongquestion.txt','a+') as wq:
		wq.writelines(question)
	with open('wrongquestionanswer.txt','a+') as wqa:
		wqa.writelines(answer)


def questionsnumback(number): #记录答题的题目序号
	with open('questionnumback.txt', 'w+') as b:
		number = str(number)
		b.write(number)

def questionnumread(): #查找答题记录
	try:
		with open ('questionnumback.txt', 'r') as b:
			backnum = b.read()
			backnum = int(backnum)
			return backnum

	except:
		print '没有答题记录'


''''''
###########################################################
''''''
if __name__ == '__main__':
	questions = 'test.txt'
	answers = 'answers.txt'
	wrong_questions ='wrongquestion.txt'
	wrong_question_answers = 'wrongquestionanswer.txt'
	zonghe_questions = 'ZHtest.txt'
	zonghe_answers = 'ZHanswers.txt'
	a = 1
	while a == True:
		choice = raw_input('请选择: \n 1.顺序练习\n 2.随机练习\n 3.复习错题\n 4.模拟理论考试\n 5.模拟综合考试\n输入 EXIT 退出程序\n')
		if choice == '1':
			back_read_file(questions,answers)

		elif choice == '2':
			random_read_file(questions,answers)

		elif choice == '3':
			wrong_review(wrong_questions,wrong_question_answers)

		elif choice == '4':
			practice_exam(questions,answers)

		elif choice == '5':
			practice_exam(zonghe_questions,zonghe_answers,10,7) #抽取10题作为综合考试题目

		elif choice =='EXIT':
			exit(0)



		else:
			print '请重新选择'

	# ordinal_read_file(questions,answers)





