---
layout: post
title: "CSS, HTML Trouble Shooting"
date:   2013-12-28 09:34:30
category: WEB	  
tags: css, html  
  
---

블로그 설정 중 자잘하게 발생한 문제나 커스터마이징시 필요했던 방법들을 정리.  
(계속해서 업데이트 예정, 최신 update 2014-01-01)  

## CSS 및 디자인    

===
`Problem: ` Markdown으로 Image 삽입시 문단 크기 벗어남  

* 문제 상태  
![_](http://xthy.github.io/img/css_img1.png)  
* 원인: Markdown에서 Image 삽입시 설정은 Origin Size Embeded임.
* 해결책: **CSS 혹은 HTML 코드에서 Image Auto Size 관련 설정 필요**  
내 경우에는 Post 화면에 일괄 적용을 원하므로, main.css에서 post 부분 img 태그에 코드 삽입.  
문단의 Width에 맞춰 Image Auto Sizing.   
	{%highlight CSS linenos=table%}
	@main.css
	.post img {
	    max-width: 100%;
	    height: auto;
	}{%endhighlight%}
* 결과  
![_](http://xthy.github.io/img/css_img2.png)  
<br />  
 
===  

`Problem: ` 모바일 화면 비율이 깨진다 

* 문제 상태  
iPad 등 타블렛에서는 문제가 없었지만, 스마트 폰에서는 사이트 비율이 깨진다.  
![_](http://xthy.github.io/img/css_img3.png) ![_](http://xthy.github.io/img/css_img4.png)  
* 원인: CSS Default에서 .site size를 px, em으로 고정해두어 스마트 폰에서는 무조건 그 크기가 표현됨.  
	{%highlight CSS linenos=table%}
	@main.css
  .site {
  font-size: 110%;
  text-align: justify;
  margin: 3em auto 2em auto;
  line-height: 1.5em;
  width: 52em; 
  }{%endhighlight%}

* 해결책: px, em 크기 고정이 아닌 % 비율로 변경 + max-width 설정 + viewport로 모바일 화면 scale 조정.  
	{%highlight CSS linenos=table%}
	@main.css
  .site {
  font-size: 110%;
  text-align: justify;
  margin: 3em auto 2em auto;
  line-height: 1.5em;
  max-width: 650px;
  width: 90%;
  }{%endhighlight%}

	{%highlight CSS linenos=table%}
	@default.html
	<meta name="viewport" content="width=device-width, initial-scale=0.8" />{%endhighlight%}
* 결과   
![_](http://xthy.github.io/img/css_img5.png)  
<br />  
 
===  
   
`Problem: ` Syntax Highlight 테이블이 스마트 폰에서 깨진다. 

* 문제 상태  
iPad 등 타블렛에서는 문제가 없었지만, 스마트 폰에서는 사이트 비율이 깨진다.      
![_](http://xthy.github.io/img/css_img6.png)  
* 원인: 미파악
* 해결책: 미해결
<br />  
 
===  

