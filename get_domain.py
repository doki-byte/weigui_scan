import re



def main_get_domain():
    # 白名单
    white_domain = ['edu.cn']

    # 复合域名
    two_domain = ["com.cn","gov.cn","edu.cn","org.cn","mil.cn","ac.cn","net.cn","ah.cn","bj.cn","cq.cn","fj.cn","gd.cn","gs.cn","gz.cn","gx.cn","ha.cn","hb.cn","hl.cn","hn.cn","jl.cn","js.cn","jx.cn","ln.cn","nm.cn","nx.cn","qh.cn","sc.cn","sd.cn","sh.cn","sn.cn","sx.cn","tj.cn","tw.cn","xj.cn","xz.cn","yn.cn","zj.cn"]

    # 读取网址
    filename = "./source/html_title.txt"
    with open(filename,"r",encoding="utf-8") as f:
        webtitles = f.readlines()

    # 解析根域名
    domains = []
    for webtitle in webtitles:
        webtitle = webtitle.split()[0].replace("https://","").replace("http://","")
        webtitle = re.sub(r':\d+','',webtitle)
        web_domain = webtitle.split(".")
        web_domain_last = web_domain[-1]
        web_domain_previous = web_domain[-2]
        domain = ".".join([web_domain_previous,web_domain_last])
        if domain in two_domain:
            web_domain_three = web_domain[-3]
            domain = ".".join([web_domain_three,web_domain_previous,web_domain_last])

        if domain not in domains:
            domains.append(domain)

        # print(domains)
    # 写入文件
    for domain in domains:
        print(domain)
        with open("./source/top_domain.txt","a+",encoding="utf-8") as f:
            f.write(domain + "\n")


if __name__ == "__main__":
    main_get_domain()