#!/usr/bin/env python
import redis, redisbayes
import jieba
def chinese_tokenizer(text):
    return [w for w in jieba.cut_for_search(text)]

rb = redisbayes.RedisBayes(redis=redis.Redis(),tokenizer = chinese_tokenizer)
rb.flush()
ac_on = open('oncn.data')
ac_off = open('offcn.data')

for line in ac_on.readlines():
	print 'trained ' +line[:-1]+' as '+'on'
	rb.train('on',line[:-1])
for line in ac_off.readlines():
	print 'trained ' +line[:-1]+' as '+'off'
	rb.train('off',line[:-1])


while True:
	line = raw_input('TEST :')
	if line == 'quit':
		break
	words =" ".join(jieba.cut_for_search(line))
	print rb.classify(words)
	print rb.score(words)

ac_on = open('oncn.data')
ac_off = open('offcn.data')

for line in ac_on.readlines():
	rb.untrain('on',line[:-1])
for line in ac_off.readlines():
	rb.untrain('off',line[:-1])






