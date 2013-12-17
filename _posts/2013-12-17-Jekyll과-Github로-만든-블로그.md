---
layout: post
title: "Jekyll과 Github로 만든 블로그"
date:   2013-12-17 21:30:30
category: blog
tags: jekyll, github, blog
---
### Shooting
* git push

		thyngMBP:xthy.github.com xthy$ git push origin master
		To https://github.com/xthy/xthy.github.com.git
		 ! [rejected]        master -> master (non-fast-forward)
		 error: failed to push some refs to 'https://github.com/xthy/xthy.github.com.git'
		 hint: Updates were rejected because the tip of your current branch is behind
		 hint: its remote counterpart. Merge the remote changes (e.g. 'git pull')
		 hint: before pushing again.
		 hint: See the 'Note about fast-forwards' in 'git push --help' for details.

기존에 생긴 Repository 내 파일 충돌(Master-Branch)였음.
모든 파일 삭제 후 다시 생성하니 문제 해결.


* Liquid Encoding

		Configuration file: /Users/xthy/Documents/jekyllX/xthy.github.com/_config.yml
		Source: /Users/xthy/Documents/jekyllX/xthy.github.com
	    Destination: /Users/xthy/Documents/jekyllX/xthy.github.com/_site
	    Generating... Error reading file /Users/xthy/Documents/jekyllX/xthy.github.com/index.html: invalid byte sequence in US-ASCII
	    Liquid Exception: invalid byte sequence in US-ASCII in index.html
	    error: invalid byte sequence in US-ASCII. Use --trace to view backtrace
	    
Terminal에 export LANG="en_US.UTF-8"로 충돌 해결.


### References
#### Jekyll
* http://jekyllrb.com/
* http://dogfeet.github.io/articles/2012/github-pages.html
* http://nolboo.github.io/blog/2013/10/15/free-blog-with-github-jekyll/
* http://jekyllthemes.org

#### Markdown
* http://daringfireball.net/projects/markdown/