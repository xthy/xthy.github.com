---
layout: post
title: "Jekyll과 Github로 만든 블로그"
date:   2013-12-17 21:30:30
category: blog
tags: jekyll, github, blog  

---

이 블로그는 Jekyll과 Github를 통해 만들고 호스팅 한다.  
Jekyll과 Github가 무엇이고, 왜 선택했는지, 설치와 운영 중 생긴 문제들과 해결책들을 정리해보았다.




# Jekyll과 Github  

### Jekyll이란?

* Jekyll is a blog-aware, static site generator in **Ruby**. (Jekyll 창시자가 Github 저장소에 쓴 Jekyll 1줄 설명)
* Transform your plain text into static websites and blogs. (Jekyll 공식 사이트 대문에 가장 큰 글씨로 써진 한 문장)
* **Simple (No Database), Static (Markdown, Textile, Liquid, HTML, CSS), Blog-aware (Permalinks, Categories, Pages, Posts)**  


### Github란?  

* GitHub is a **web-based hosting service for software development projects that use the Git** revision control system. GitHub offers both paid plans for private repositories, and free accounts for open source projects. As of May 2011, GitHub was the **most popular code repository site for open source projects**. (Wikipedia 첫 문단)  
* GitHub is the best place to share code with friends, co-workers, classmates, and complete strangers. Over four million people use GitHub to build amazing things together. (Github 홈페이지 About의 첫 문단) 

짧게 요약하면 **Jekyll은 문서 파일을 웹 페이지용으로 변환 시켜주는 도구, Github는 온라인 형상관리 서비스.**



# 왜 Jekyll + Github로 블로그를?

이미 [Wordpress 설치형 블로그](http://thtyle.com/blog/)를 갖고 있지만, SW 개발관련한 내용만 싣기 위한 블로그가 필요했다.  
내 요구사항은,  

* 너무하다 싶을 정도로 간결할 것  
* 최소한의 기술 (결국 사이트의 높은 속도, 성능을 보장)  
* 테마나 위젯이 없어야 함 (눈에 보이면 설치하고 싶어지니까)  
* 무료로 안정적인 호스팅 보장  
* Markdown 지원 필요  

Github의 Pages 기능으로 무료 호스팅, Jekyll이 Markdown을 HTML로 변환해주고, 레이아웃도 '쌩짜' HTML.  
Jekyll과 Github 조합은 내 요구사항에 딱 맞아 떨어졌다.  



# Jekyll + Github 블로그 예  
* [Tom Preston-Werner, Github Founder](http://tom.preston-werner.com/)  
* [Zach Holman, Github Engineer](http://zachholman.com/)  
* [Chris Yin, Coupa Product Manager](http://www.chrisyin.com/)  
* [Paperplanes](http://www.paperplanes.de/)  
* [그 외 사이트 리스트 via Jekyll Wiki](https://github.com/jekyll/jekyll/wiki/Sites)  



# 설치 및 적용 순서  
1. Github 가입 및 Repository 생성  
2. 로컬에 Jekyll 및 Rubygem 설치   
![_](http://xthy.github.io/img/1.png)  
![_](http://xthy.github.io/img/2.png)
3. 로컬의 Jekyll 폴더를 Github Repository에 Commit & Push  
![_](http://xthy.github.io/img/3.png)  
![_](http://xthy.github.io/img/4.png)  
4. Layout 수정 (CSS)
5. 추가 기능 적용 (Disqus, Google Analytics)  
![_](http://xthy.github.io/img/5.png)  

		<!DOCTYPE html>
		<html>
		    <head>
		        <meta charset="utf-8">
		        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
		        <title>{{ page.title }}</title>
				<meta name="viewport" content="width=device-width">
		        <!-- syntax highlighting CSS -->
		        <link rel="stylesheet" href="/css/syntax.css" type="text/css">
		        <!-- Custom CSS -->
		        <link rel="stylesheet" href="/css/main.css" type="text/css" media="screen, projection" />
		    </head>
		    <body>
		        <div class="site">
		          <div class="header">
		            <h1 class="title"><a href="/">{{ site.name }}</a></h1>
		          </div>
		          {{ content }}    
		          <div class="footer">
		            <div class="contact">
		              <p>Contact: xthy@me.com,
						<a href="http://twitter.com/xthy" target="_blank">Twitter</a>,
		                <a href="http://github.com/xthy" target="_blank">Github</a>,
						<a href="http://thtyle.com/blog" target="_blank">THTYLE Blog</a> 
		                <br/>
		              </p>
		            </div>
		          </div>		  
		        </div>
				<!-- Google Analytics -->
				<script>
				  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
				  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
				  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
				  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
		
				  ga('create', 'UA-46395179-1', 'xthy.github.io');
				  ga('send', 'pageview');
		
				</script>
				<!-- Google Analytics end -->
		    </body>
		</html>

설치 및 적용의 상세내용은 웹 상에서 쉽게 찾을 수 있어서 생략했다. 아래 References 사이트들을 참고했다.


# Trouble Shooting  

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
  

# References  

1. Jekyll + Github
	* [공식사이트](http://jekyllrb.com/)
	* [Dogfeet님 포스팅 자료 : Github-Pages-Jekyll 설명](http://dogfeet.github.io/articles/2012/github-pages.html)
	* [Nolboo님 포스팅 자료 : 처음 Jekyll 및 Github 설정 관련](http://nolboo.github.io/blog/2013/10/15/free-blog-with-github-jekyll/)

2. Markdown
	* [Markdown 개발자 John Gruber가 설명하는 문법](http://daringfireball.net/projects/markdown/)
	* [Mashery가 제공하는 Cheat Sheet](http://support.mashery.com/docs/customizing_your_portal/Markdown_Cheat_Sheet)
	* [추천 Markdown 에디터: Haroopad](http://pad.haroopress.com/user.html)
  
  
      
  
  