import re
src2 = '''
<html>
<head>
<meta charset="utf-8" />
<title>建国初期、社会主义革命和建设时期 1、《毛泽东选集第五卷》 出版说明_《毛泽东选集 第五卷》_读典籍</title>
<link href="/skin/v3/p1.css" rel="stylesheet" />
<script src="/skin/v3/js/jquery.min.js"></script>
<script src="/skin/v3/js/jquery.cookie.js"></script>
<script type="text/javascript">
$(document).ready(function(){
var prevpage="/hongsejingdian/53/";//向左
var nextpage="/hongsejingdian/53/1597.html";//向右
var bookpage="/hongsejingdian/53/";  //回车
$("body").keydown(function(event){
if(event.keyCode==13) location=bookpage;
if(event.keyCode==37) location=prevpage;
if(event.keyCode==39) location=nextpage;
});
});
</script>
</head>
'''

src = "123 3.14 0.68 abc -20"

#能够匹配全部小数的正则
#1.\d表示数字,    2.+表示前面的\d至少出现一次, 3.\.是.
p = "\d+\.\d+"  

#通过正则表达式 定义出一个 正则句柄
pattern = re.compile(p)
#通过正则表达式,去匹配源数据
result = pattern.findall(src)
#或者直接下面也可以
result1 = re.findall(p,src)
#1.()表示把内容取出来,如果不带,那么回包含<title></title>     2. .表示任意字符  3. *表示前面的字符出现认识多次
p2 = "<title>(.*)</title>"
result2 = re.findall(p2,src2)

#输出结果
print(result) 
print(result1)
print(result2)