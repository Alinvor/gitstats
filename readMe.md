
# gitstats

gitstats



## 构建`venv`环境

### venv2

```
virtualenv -p /usr/local/bin/python2 --no-site-packages venv2
```

## venv3

```
virtualenv -p /usr/local/bin/python3 --no-site-packages venv
```

## 使用方式

### 方式一

目录结构如下:

```
+ root
  + --- directory_work_space_xxx
  | + - directory_the_current_project
  |
  + --- directory_work_space_gitstats
    + - directory_the_gitstats_project   //即 gitstats
```

使用如下命令:
```
$ cd root/directory_work_space_gitstats/directory_the_gitstats_project(即gitstats)
$ ./code.sh

$ enter the directory(format is ../workspace/the_current_project, but you only input the_current_project or workspace/the_current_pr
oject): 
$ directory_work_space_xxx/directory_the_current_project

$ enter the start date(format is xxxx-xx-xx): 
$ enter the start date(format is xxxx-xx-xx): 2019-12-12

# the sensible browser
# sensible-browser 'directory_work_space_gitstats/gitstats/out/statistics_directory_the_current_project_2019-xx-xx_2019-12-12_xxxxxx/index.html'
```

### 方式二

目录结构如下:

```
+ root
  + --- directory_work_space_gitstats
    + - directory_the_gitstats_project   //即 gitstats
    + - directory_the_current_project
```

使用如下命令:
```
$ cd root/directory_work_space_gitstats/directory_the_gitstats_project(即gitstats)
$ ./code.sh

$ enter the directory(format is ../workspace/the_current_project, but you only input the_current_project or workspace/the_current_pr
oject): 
$ directory_the_current_project

$ enter the start date(format is xxxx-xx-xx): 
$ enter the start date(format is xxxx-xx-xx): 2019-12-12

# the sensible browser
# sensible-browser 'directory_work_space_gitstats/gitstats/out/statistics_directory_the_current_project_2019-xx-xx_2019-12-12_xxxxxx/index.html'
```
## FAQ

### Note

> 其实就是注意一下,输入的目录:
> 一种为: `directory_work_space_xxx/directory_the_current_project`
> 一种为: `directory_the_current_project`
>
> 再然后就是注意一下，日期输入格式: `xxxx-xx-xx`
> 举例: 2019-12-12
>
> 最后浏览器打开:
> `../gitstats/out/statistics_directory_the_current_project_2019-xx-xx_2019-12-12_xxxxxx/index.html`