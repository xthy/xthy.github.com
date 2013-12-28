---
layout: post
title: "Jekyll에서 Syntax Highlight 하기"
date:   2013-12-23 20:05:30
category: BLOG
tags: jekyll, code, syntax, highlight  

---

## Syntax Highlight 
Jekyll에서 Syntax, Code Highlight를 사용하는 방법인 Pygments와 highlight.js를 정리해본다.   
현재 이 블로그에는 Jekyll에 친화적인 Pygments를 사용 중이다.

### 1. Pygments  

**특징**  

* Jekyll에서 기본 지원하는 기능이다.  
* 100여개의 언어를 지원하고, Jekyll CSS 설정변화로 다양한 스타일 커스터마이징이 가능하다.  
* Markdown에서 사용하기 편하다.  
  
**사용법**  

1-1. Terminal에서 Pygments 설치 (Mac 환경에서 테스트 함).    
{%highlight console linenos=table%}
$ sudo easy_install Pygments
{%endhighlight%}  
1-2. Terminal에서 CSS 생성 (@Jekyll이 생성된 폴더에서).  
{%highlight console linenos=table%}
$ pygmentize -S default -f html > syntax.css
{%endhighlight%}  
1-3. _config.yml 파일에 설정 추가  
{%highlight console linenos=table%}
pygments: true
{%endhighlight%}  
1-4. HTML 파일에 1-2에서 생성한 syntax.css 파일 링크 삽입하기  
{%highlight html linenos=table%}
<link rel="stylesheet" href="/css/syntax.css">
{%endhighlight%}  
1-5. Markdown 파일(포스트)에 사용하기 ([사용법 링크](http://thedereck.github.io/gh-pages-blog/user-manual/syntax-highlighting.html)).
<br />
<br />

### 2. highlight.js  
**특징**  

* [highlight.js](http://highlightjs.org/)는 Syntax Highlight를 지원해주는 오픈소스 프로젝트이다.  
* 67개 언어 32개 스타일을 지원한다 ([데모링크](http://highlightjs.org/static/test.html)).  
* .js, .css 파일 두 개와 HTML 내 코드 삽입만으로 동작한다.  
* HTML 파일 내 `<Code>` 태그에 반응한다.  
* 그들이 호스팅하는 js, css 파일을 사용할 수 있다 (물론 내가 설정할 수도 있고).  
* [Github Link](https://github.com/isagalaev/highlight.js)  
  
**사용법** 

2-1. highlight.js에서 제공해주는 .js와 .css 파일을 다운받아 내 블로그 사이트에 업로드 한다.  
2-2. Syntax Highlight를 사용할 HTML 파일에 .js와 .css 파일의 위치정보를 아래처럼 지정해주면 자동 동작한다.  
(Tip. 블로그 전체 포스트에 적용하고 싶다면, 블로그 테마나 레이아웃 헤더 파일에 적용하면 된다.)  
{%highlight html linenos=table%}
<link rel="stylesheet" href="css/syntax.css">
<script src="syntax/highlight.pack.js"></script>
<script>hljs.initHighlightingOnLoad();</script>
{%endhighlight%}  
2-3. highlight.js에서 자체 호스팅 중인 .js, .css를 사용하면 내 블로그 사이트에 업로드 하지 않고도 간단하게 적용할 수도 있다.  
{%highlight html linenos=table%}
<link rel="stylesheet" href="http://yandex.st/highlightjs/7.5/styles/default.min.css">
<script src="http://yandex.st/highlightjs/7.5/highlight.min.js"></script>
{%endhighlight%}
