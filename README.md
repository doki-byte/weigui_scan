## 网信办查询违规站点小工具
### 使用
将需要进行检测的url放在source目录下面的urls.txt文件中  

运行main.py即可  

![image](https://github.com/Muhansrc/weigui_scan/assets/128204479/ab91ee5f-4df1-4bfc-97e9-c91a37e9f4db)
![image](https://github.com/Muhansrc/weigui_scan/assets/128204479/6cd74c9f-737d-4f51-b121-df2f4ce887a1)
![image](https://github.com/Muhansrc/weigui_scan/assets/128204479/fdf50e9c-08b9-45a5-8299-7f20df9bc369)




### 脚本思路
+ 导入违规词url
+ 检查url存活
+ 判断是否存在备案
+ 根据备案反查title，确定违规站点


### cookie设置
如果一直备案查询失败
修改icp_check里面的cookie_str字符
![image](https://github.com/Muhansrc/weigui_scan/assets/128204479/29182bd9-592c-4952-a434-51b8a32ee04c)
![image](https://github.com/Muhansrc/weigui_scan/assets/128204479/470118ff-2cbd-49bf-8724-e03ba6485482)


### 后续更新
1. 匹配查询机制,多次查询得到ip被ban的提示，然后自动更换代理地址
2. 全部查询完之后从excal中提取所有存在备案域名的Webtitle
3. 增加更多第三方接口，提高检测正确率
4. 适配已存在的官方检测接口，避免出现冗余数据查询
