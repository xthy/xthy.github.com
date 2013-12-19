---
layout: post
title: "Jekyll과 Github로 만든 블로그"
date:   2013-12-17 21:30:30
category: blog
tags: jekyll, github, blog  

---

이 블로그는 Jekyll과 Github를 통해 만들고 호스팅 한다.
Jekyll과 Github가 무엇이고, 어떻게 블로그가 동작하는지, 설치-운영 시 생긴 문제들과 해결책들을 정리해보았다.

# Jekyll과 Github  

### Jekyll이란?

* Jekyll is a blog-aware, static site generator in **Ruby**. (Jekyll 창시자가 Github 저장소에 쓴 Jekyll 1줄 설명)
* **Transform your plain text into static websites and blogs.** (Jekyll 공식 사이트 대문에 가장 큰 글씨로 써진 한 문장)
* Simple (No Database), Static (Markdown, Textile, Liquid, HTML, CSS), Blog-aware (Permalinks, Categories, Pages, Posts)  


### Github란?  
* GitHub is a **web-based hosting service for software development projects that use the Git** revision control system. GitHub offers both paid plans for private repositories, and free accounts for open source projects. As of May 2011, GitHub was the **most popular code repository site for open source projects**. (Wikipedia 첫 문단)  
* GitHub is the best place to share code with friends, co-workers, classmates, and complete strangers. Over four million people use GitHub to build amazing things together. (Github 홈페이지 About의 첫 문단) 

# Jekyll + Github = Blog?

/img/Screen Shot 2013-12-12 at 10.24.54 PM.png
/img/Screen Shot 2013-12-12 at 10.26.23 PM.png
/img/Screen Shot 2013-12-12 at 10.41.44 PM.png
/img/Screen Shot 2013-12-12 at 11.01.54 PM.png
/img/Screen Shot 2013-12-12 at 11.02.22 PM.png
/img/Screen Shot 2013-12-12 at 11.04.55 PM.png
/img/Screen Shot 2013-12-12 at 11.40.18 PM.png
/img/xthy — bash — 87×18 2013-12-12 22-21-55.png
/img/xthy — bash — 87×24 2013-12-12 22-22-49.png
/img/xthy — bash — 87×24 2013-12-12 22-23-12.png

## Trouble Shooting  

* 초기 Github push 에러  
	* 명령어
	
			$ git push orgin master
	* 에러 출력  
	
			To https://github.com/xthy/xthy.github.com.git
			 ! [rejected]        master -> master (non-fast-forward)
			 error: failed to push some refs to 'https://github.com/xthy/xthy.github.com.git'
			 hint: Updates were rejected because the tip of your current branch is behind
			 hint: its remote counterpart. Merge the remote changes (e.g. 'git pull')
			 hint: before pushing again.
			 hint: See the 'Note about fast-forwards' in 'git push --help' for details.

	* 원인: 기존에 생긴 Repository 내 파일 충돌(Master-Branch) 
	* 해결책: **Repository 파일 삭제 후 다시 생성하니 문제 해결**

* 한글 입력시 Liquid Encoding 에러
	* 명령어  
	
			$ jekyll serve --watch
	* 에러 출력  

			Configuration file: /Users/xthy/Documents/jekyllX/xthy.github.com/_config.yml
			Source: /Users/xthy/Documents/jekyllX/xthy.github.com
		    Destination: /Users/xthy/Documents/jekyllX/xthy.github.com/_site
		    Generating... Error reading file /Users/xthy/Documents/jekyllX/xthy.github.com/index.html
		    : invalid byte sequence in US-ASCII
		    Liquid Exception: invalid byte sequence in US-ASCII in index.html
		    error: invalid byte sequence in US-ASCII. Use --trace to view backtrace
	    
	* 해결책: **Terminal에 export LANG="en_US.UTF-8"로 충돌 해결.**
  
    
      
  
        

## References
1. Jekyll
	* http://jekyllrb.com/
	* http://dogfeet.github.io/articles/2012/github-pages.html
	* http://nolboo.github.io/blog/2013/10/15/free-blog-with-github-jekyll/
	* http://jekyllthemes.org  

2. Markdown
	* http://daringfireball.net/projects/markdown/  
  
  
      
  
  