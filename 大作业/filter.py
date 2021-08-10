from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import pygal
import sys


c_finished_name, c_finished_url, c_finished_num = [], [], []  # 存放已结束、可查看、并且免费的课程名和URL
c_ongoing_name, c_ongoing_url, c_ongoing_num = [], [], []     # 存放正在进行、并且免费的课程名和URL
plot_dicts_finished, plot_dicts_ongoing = [], []              # 数据可视化要用到的数据
page_num = 3                                                  # 设定爬取的页面数量
keyword = ''                                                  # 搜索关键字


# 获取课程信息，并存到csv文件中
def get_info(browser):
    status, href = '', ''
    # 处理无法获取网页的异常
    try:
        browser.get("https://www.icourse163.org/search.htm?search={}".format(keyword))
        time.sleep(5)           # 让页面加载一会
    except:
        print('无法获取网页！')
    # 处理搜索无结果的异常
    try:
        browser.find_element_by_css_selector('.lists').text == ''
    except:
        print('搜索结果为无。')
        return False
    # 首先向文件存入列索引信息
    with open('course_info.csv', 'w', encoding='utf-8') as f:
        f.write(','.join(['name', 'school_teacher', 'num', 'status', 'href\n']))
    # 开始爬取
    page = 1
    while True:
        course_list = browser.find_elements_by_css_selector('.m-course-list > div > div')

        for item in course_list:
            try:
                href = item.find_element_by_css_selector('.g-mn1c > div > a').get_attribute('href')
                name = item.find_element_by_css_selector('.g-mn1c > div > div:nth-child(1) > a:nth-child(1)').text
                school_teacher = item.find_element_by_css_selector('.g-mn1c > div > div:nth-child(2)').text
                num = item.find_element_by_css_selector('.g-mn1c > div > div:nth-child(4) > span:nth-child(2)').text
                num = num[:num.index('人参加')]
                status = item.find_element_by_css_selector('.g-mn1c > div > div:nth-child(4) > div').text
            except:
                pass
            # 将信息存到csv文件中
            with open('course_info.csv', 'a', encoding='utf-8') as f:
                f.write(','.join([name, school_teacher, num, status, href + '\n']))
        # 本页爬取完了，点击下一页继续爬取
        next_page = browser.find_element_by_css_selector('.ux-pager > li:last-child')
        next_page_class = next_page.find_element_by_css_selector('a').get_attribute('class')
        if next_page_class == 'th-bk-disable-gh' or page == page_num:
            break
        next_page.click()
        time.sleep(2)           # 让页面加载一会
        page = page + 1

    return True


# 过滤掉还未开始的课程和已经结束但是无法查看的课程
def filter_1():
    with open('course_info.csv', 'r', encoding='utf-8') as targetfile:
        col_index = targetfile.readline()           # 读取文件第一行的列索引
        raw_data = targetfile.readlines()
        for row in raw_data:
            course_info = row.split(',')
            status = course_info[3]
            if status == '已结束，可查看内容':
                c_finished_name.append(course_info[0])
                c_finished_url.append(course_info[4])
                c_finished_num.append(int(course_info[2]))
                plot_dict = {
                    'value': int(course_info[2]),
                    'label': course_info[1],
                    'xlink': course_info[4],
                }
                plot_dicts_finished.append(plot_dict)
            elif status == '已结束':
                pass
            elif '进行至' in status:
                c_ongoing_name.append(course_info[0])
                c_ongoing_url.append(course_info[4])
                c_ongoing_num.append(int(course_info[2]))
                plot_dict = {
                    'value': int(course_info[2]),
                    'label': course_info[1] + '\n' + course_info[3],
                    'xlink': course_info[4],
                }
                plot_dicts_ongoing.append(plot_dict)


# 过滤掉要付费的课程
def filter_2(name_list, url_list, browser):
    for url in url_list:
        price = ''

        # 处理获取网页信息失败的异常
        try:
            browser.get(url)
        except:
            print('无法获取网页！')

        # 处理找不到存放课程价格标签的异常
        try:
            price = browser.find_element_by_css_selector('.info-row__value__current-price__price').text
        except:
            pass

        # 如果课程显示要付费，过滤掉
        if price == '免费' or price == '':
            pass
        else:
            loc = url_list.index(url)
            url_list.remove(url)
            del name_list[loc]


# 筛选后的课程数据可视化
def visualize(file_path, name_list, plot_dicts):
    show_num = len(name_list) if len(name_list) < 10 else 10    # 显示的课程数目始终不超过10个

    # 设置图表样式
    my_config = pygal.Config()
    my_config.x_label_rotation = 20
    my_config.show_legend = False
    my_config.style.title_font_size = 40
    my_config.style.label_font_size = 25
    my_config.style.major_label_font_size = 25
    my_config.truncate_label = 10       # 限制x轴标签显示的字符数目
    my_config.show_y_guides = False     # 隐藏图表中的水平线
    my_config.width = 1200
    my_config.height = 700

    chart = pygal.Bar(my_config, y_title='参加的人数')
    chart.title = '中国大学MOOC：' + file_path[:-4]
    chart.x_labels = name_list[:show_num]
    chart.add('', plot_dicts[:show_num])
    chart.render_to_file(file_path)


# 将两幅图合并到一个html文件中
def merge_show(path1, path2):
    file_path = 'result.html'
    with open(file_path, 'w', encoding='utf-8') as html_file:
        html_file.write('<html><head><title>筛选后的课程</title><meta charset="utf-8"></head><body>\n')
        for svg in [path1, path2]:
            html_file.write('<object type="image/svg+xml" data="{0}" height=700 width=1600></object>\n\n\n'.format(svg))
        html_file.write('</body></html>')


# 整合操作
def integrate(driver_path, flag):
    driver_service = Service(driver_path)
    driver_service.command_line_args()
    driver_service.start()

    if flag == '1':
        browser_options = webdriver.ChromeOptions()
    elif flag == '2':
        browser_options = webdriver.FirefoxOptions()

    browser_options.add_argument('--headless')      # 无头模式
    browser_options.add_argument('--disabled-gpu')  # 禁用GPU加速

    if flag == '1':
        browser = webdriver.Chrome(executable_path=driver_path, options=browser_options)
    elif flag == '2':
        browser = webdriver.Firefox(executable_path=driver_path, options=browser_options)

    # 能够搜索到课程信息，才去过滤
    if get_info(browser):
        filter_1()
        filter_2(c_finished_name, c_finished_url, browser)
        filter_2(c_ongoing_name, c_ongoing_url, browser)
        browser.quit()          # 结束对浏览器的控制
        driver_service.stop()   # 杀死chromedriver.exe进程
    else:
        sys.exit(0)


if __name__ == '__main__':
    # 从文件中读入用户的输入
    with open('user_input.txt', 'r', encoding='utf-8') as f:
        input_content = f.readline()
        keyword = input_content[:input_content.index(',')]
        flag = input_content[input_content.index(',')+1]

    if flag == '1':
        integrate('chromedriver.exe', flag)
    elif flag == '2':
        integrate('geckodriver.exe', flag)

    # 筛选后的结果可视化
    filename1 = '已结束课程的筛选结果.svg'
    filename2 = '正在进行课程的筛选结果.svg'
    visualize(filename1, c_finished_name, plot_dicts_finished)
    visualize(filename2, c_ongoing_name, plot_dicts_ongoing)

    # 将两幅图合并到一个html文件中
    merge_show(filename1, filename2)
    print('已完成筛选，查看结果请打开生成的result.html文件。')
