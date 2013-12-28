---
layout: post
title: "Jekyll & Github Trouble Shooting"
date:   2013-12-23 19:35:30
category: BLOG
tags: jekyll, github  

---

## Trouble Shooting  
Jekyll + Github 설치 및 적용시 발생한 문제점들과 해결 방법들 정리  
(계속해서 업데이트 예정, 최신 update 2013-12-25)  


===
`Problem: ` Github push 시 에러  

* 명령어     	{%highlight console linenos=table%}$ git push orgin master {%endhighlight%} 
	    
* 에러 출력  
{%highlight console linenos=table%}
To https://github.com/xthy/xthy.github.com.git
! [rejected]        master -> master (non-fast-forward)
error: failed to push some refs to 'https://github.com/xthy/xthy.github.com.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Merge the remote changes (e.g. 'git pull')
hint: before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.{%endhighlight%}
* 원인: 기존에 생긴 Repository 내 파일 충돌(Master-Branch) 
* 해결책: **Repository 파일 삭제 후 다시 생성하니 문제 해결됨**  
<br />  
 
===  

`Problem: ` 한글 입력시 Liquid Encoding 에러  

* 명령어  
	{%highlight console linenos=table%}$ jekyll serve --watch{%endhighlight%}
	  
* 에러 출력  
{%highlight console linenos=table%}Configuration file: /Users/xthy/Documents/jekyllX/xthy.github.com/_config.yml
Source: /Users/xthy/Documents/jekyllX/xthy.github.com
Destination: /Users/xthy/Documents/jekyllX/xthy.github.com/_site
Generating... Error reading file /Users/xthy/Documents/jekyllX/xthy.github.com/index.html
: invalid byte sequence in US-ASCII
Liquid Exception: invalid byte sequence in US-ASCII in index.html
error: invalid byte sequence in US-ASCII. Use --trace to view backtrace{%endhighlight%}
* 해결책: **Terminal에 export LANG="en_US.UTF-8"로 해결.**  
<br />  
 
===