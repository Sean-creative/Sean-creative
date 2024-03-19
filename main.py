import feedparser, time

URL = "https://sean-lets-go.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5

markdown_text = """
<div align="center"> 

![header](https://capsule-render.vercel.app/api?type=Waving&color=558168&height=150&section=header&text=Cheers🚀&fontColor=ffffff&fontSize=70&animation=fadeIn&fontAlignY=45&desc=%20&descAlignY=62&descAlign=62&fontAlign=53)
  
####  :wave: 안녕하세요 개발자 션입니다!
 재미있게 경험하고 배운 것들을 피드백합니다!<br>
 
  
<h3 align="center">⛏️ Skills </h3>
<p align="center">
  <img src="https://img.shields.io/badge/Java-ed921e?style=flat-square&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAAh1BMVEXe5uzAztqxwtHc4OT09PT19fXw8PCqu8rn5+f8/Pzs0Lf6+vrnrXrleiugscLk5OT39/fs7OzkcR7lx6zh4eHhr4LhZRLhpW+Vp7fd3d3gYA6Knq3W1tbbbhzXoW1cepV6jZ6EmKdIZoJWc4vQ0NB8kJ6otb3Ly8twhZV1jqW5vcK9yM9ofY52NCXaAAAAr0lEQVR4AU3KhUIDMQwA0BwrWWftZWQSLrDq/P+/jxPsVaIAzcs/TV/PzOsI+2dmDcztYoTLVf/bed9YDXC9MX3oG863PVpv6c20rXfg2BiDuz0ftmgMOzgKItKe9nsiRDn2DSKyG3m3Vpj6RqfWq+rHp8opiHYQ1XNKub8dp1Ai1MIi554rJYVLhXAR0Zz6DU1BLwGCsmqZMGuAq7K7nSbe6hXqnf/4e4VHfP4TH1/dVRTdLcfq+gAAAABJRU5ErkJggg==&logoColor=white"/></a>&nbsp
  <img src="https://img.shields.io/badge/Kotlin-7F52FF?style=flat-square&logo=kotlin&logoColor=white"/></a>&nbsp
  <img src="https://img.shields.io/badge/SpringBoot-6DB33F?style=flat-square&logo=SpringBoot&logoColor=white"/></a>&nbsp 
  <img src="https://img.shields.io/badge/JPA-bbae79?style=flat-square&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAMAAABF0y+mAAAAVFBMVEVHcExNWF2xqo3JupG/sYovLytib3WFi4Sjl3VZZWpreX9ndn2/sow8QD5zfoCwo39jcHaZmYePhGdCS06toX1QWl9pdnzFuI98eGSOhWhaZ21YY2hTQR8WAAAAHHRSTlMAWv//5A/h/52D///8Kv+1xf9EQ3hq8f9uUKCs3hqMhAAAANRJREFUeAFd0QWyxDAMA1CXW7nMcP9zfsjG0H2DTeKpNKYgSTORF/RWlFWmanprwDbadu9BBnobHcgbAfBktzOZhfGvtUxkynDHLtNKYkPkMhWSZgfi6CG0zgJ1XuLsNGt0k7rHr9HdynfAQh8PguZVfJd3oWdZkEj82wZ/EreGEF7+sgOjX0PwWCaXRoovksDXQDTKa9cfQkfrQ1UsxSV/YQtLEW0k1kzF0ZJMbgsLd7yQmW10YsmqBrvtAS7I61wmtjVInb/jI2aSNagiz+Q6/azhF7bGEQOpXYvuAAAAAElFTkSuQmCC&logoColor=white"/></a>&nbsp
  <img src="https://img.shields.io/badge/QueryDSL-0085c8?style=flat-square&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADdUlEQVR4AcVWU6DcQBS9tW3bdvtV27Zt2253k9na+qlt285Mnmrbdrd3krxtssw+fpyHwb0nF2cu2O32aIX5gyLrDiINAkKPwZyArI711ffi4/o6XL+JZ5pHCgEgbDDMluzoyA6C8vsP2K5k0IgdBIu2N+u6Hay0fsQTEKWv3IEDVu6QbVL2pl/jazqweRFPwKp3oEWB0MMqOfoABD0xqSeQwJR8H3EGyNXcfhEAS0B6NNgabNeLw9IrcZQ1QVplIDCbh1qupKUnJ649R3wHgW3U0rKEk9GI7TZNAC9MVxxYJNWJSC/CwsDEGIFEaHwB/v8Rjd9yV2z8nK5gO8GMa2pNEGmyKQIwm+bjjN3kum+Y2ounQmQjVXIYVRKQGzdieCYgsjro9K8x1wjC9oS710X6S7PZ1AuBgGJuIyCwcRFA4JNiyyrX9VEDbBXmXvf19B2v6HATIOcSwLxbSc11gY02472MJMbCIpYiQmVXYFMx0pU9EjAWScSCR1LpDEEKdCEAwrVsINA1INK9YKXDI42ESKuCLSiDYQ0dpgVCvxtEhqiCEtHgwgYLglMZCQhSe+fqR/zkL17Ep4EORNtfYTbN7FjDhd5uCPzgwuF3jnuo0u0JKO/Z0fYwYwRscgFc/G0QH5HeM+14kj0m2OhOENkHvPsCiFza79cQRLkdOr3GHaOhHZirhKYN2Fg1pwhedC0+OQvWWuHQGUIP45dsssfytxWBsM5OBH459mYqL+U9xB8NfxEBvPA9C9EcOR0QqTE/ZIrAPJqZ14zSPbMQ6oASACLbrnuSnd4X+gUEVsqFADrNoVzimInGbKyCaanF4gIhoCYsuJgKjX/jznzgDZBHCZyF4i4IBrY3YdOmWP5LLl2MH+GLwF9Eeed8PjWGjN2CScdjh2EWOASCdwKqH9bduU+LK9OvBTGN55LVCaPk7jdFgNCubsIXlA0d9+TvgzophSTB/2fhhYW8jczVhNwVLD4IEPqXa4aJr2F7/38N225yik6E51/5qIFn/G0wE85junbar6xZaFOlYEVpvPL/rCvJ8P+r+vkRCGuojfBu5kz6EubJufg5E31+Kx4alvHSQ5hPc3Ch4pHQIvJNdSZlghnX0ZnxFYXFNC2ekZRwi1Ko3O/kEXIvRObVr4gyPxBay7GGJLw+VKgxesdGAtGIaCfwD+uUnoqt9iLIAAAAAElFTkSuQmCC&logoColor=white"/></a>&nbsp   
  <img src="https://img.shields.io/badge/Junit5-25A162?style=flat-square&logo=junit5&logoColor=white"/></a>&nbsp 
  <br>
  <img src="https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=AmazonAWS&logoColor=white"/></a>&nbsp 
  <img src="https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white"/></a>&nbsp 
  <img src="https://img.shields.io/badge/Helm-0F1689?style=flat-square&logo=helm&logoColor=white"/></a>&nbsp   
  <img src="https://img.shields.io/badge/Kustomize-326CE5?style=flat-square&logo=kustomize&logoColor=white"/></a>&nbsp 
  <img src="https://img.shields.io/badge/GitHub Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white"/></a>&nbsp 
  <img src="https://img.shields.io/badge/Argo CD-eb7456?style=flat-square&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAMAAABF0y+mAAAAclBMVEVbZJdzdqRUYZtdYpVgZZdPa6ZnZZNHcExbY5RcYpXtek2scnq/dGvqeU3leVLVc1vDc2LSdVtdYZPvekz////uc0D0fU7zm3r78Ovxh1/618tdYZPheFLg4N+RkpP2u6YKBwmxXDtAQ0W4ubleYZTUlH+sMF1vAAAAE3RSTlMkMRVVMis6AB9D70pt2LSHwPDu6zsXTwAAAXtJREFUKJFl0tuCoyAMBuBwLBHsYQAFO9pOu/v+rzgJ2rGz+194wacBQ+CwRzoAJ98W4EcsorWan/JfRNRuDWhE+Y5OGYcatjhQsKNGB0ahbjHMqF/oyNDSsqZNTWOHZkO12anvuv7ITKpkQzTNbDcMkROaAjJKdJatjxt23lBl2ovQakCuGV84HI0QAAYJ0WnesI97vCB1hB+Kzq2F7d4wmIYfcG1IVWvMDHmo8bjiFf4wmtNYUhlJ862kqZL+IBVN8zKnMeYxPZdUsl+Ryxo/puW+pFvOU3rc51RPZkOJgrA8y4rzM6UaCNWVOkG/IvqSUiqVy1KmtaymJlD3hO+mMlU+7DiVWwyi9Q/4Tqw1vlv/hDjmwIe10BpPLwl461DH3XOt8QepaDYY65hzHRnZ1is70JlAHmP8nKdp/ktIZvVrTCy6ho9leXwNhM7iPmBGMQ5f9ztZ7LcReo2mxDPf5NCu9PJ7NCn+fPlsuZzDfxNPX/twCsG7feUbAx4iNIAN04MAAAAASUVORK5CYII=&logoColor=white"/></a>&nbsp   
  <br>
  <img src="https://img.shields.io/badge/Prometheus-E6522C?style=flat-square&logo=prometheus&logoColor=white"/></a>&nbsp  
  <img src="https://img.shields.io/badge/Grafana-F46800?style=flat-square&logo=grafana&logoColor=white"/></a>&nbsp  
  <img src="https://img.shields.io/badge/Kafka-231F20?style=flat-square&logo=apachekafka&logoColor=white"/></a>&nbsp  
</p>

<h3 align="center">🔊 Contact</h3>
<p align="center">
  <a href="https://sean-lets-go.tistory.com/"><img src="https://img.shields.io/badge/Tech%20Blog-11B48A?style=flat-square&logo=Vimeo&logoColor=white&link=https://sienna1022.tistory.com/"/></a>&nbsp
  <a href="mailto:ksw6125000@gmail.com"><img src="https://img.shields.io/badge/Gmail-d14836?style=flat-square&logo=Gmail&logoColor=white&link=20200803@gmail.com"/></a>
</p>


## ✅ Latest Blog Post

"""  # list of blog posts will be appended here

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"
        
f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
