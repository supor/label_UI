# coding: utf-8

STIME = 0.5
TASK_AMOUNT = "1"


# ######################################################################################################################
# 用户登录名和密码
USERNAME_VENDOR = ["r", "test_editor", "test_checker", "test_reviewer", "test_reviewer", "w1"]  # 管理员、标注员、检查员、抽查员、验收员
PWD_VENDOR = "vendor"
# PWD_VENDOR = "zsp14006"

BASE_URL_VENDOR = "https://staging.zzcrowd.com/"
# BASE_URL_VENDOR = "https://www.zzcrowd.com/"
USERNAME_DEV = ["r", "c3", "c4"]
PWD_DEV = "dev"
BASE_URL_DEV = "http://caihao.dev.zzcrowd.com/"

BASE_URL = "https://staging.zzcrowd.com/"
# BASE_URL = "http://caihao.dev.zzcrowd.com/"

# ######################################################################################################################
# 流式-任务列表页面需要标注的项目名称 #
# 标注
STREAM_EDIT_TASK_NAME = u"Face - 假脸识别"
# 检查
STREAM_CHECK_TASK_NAME = u"Face - 假脸识别"
# 验收
STREAM_REVIEW_TASK_NAME = u"Face - 假脸识别"

# 项目列表页面，筛选项目类型，xpath 的option id, 项目列表url
TASK_XPATH_ID = "13"
TASK_POOL_ID = "1"
JOB_LIST = "spa/job/manager/jobs?sorts=&page=1&per_page=10&"

# 多队列测试的项目类型名称
MULT_TASK_NAME = u"Face - 假脸识别"

# ######################################################################################################################
# #新增任务池
# 选择任务池类型
TASK_ID = "8"
# 添加小组长，验收员，标注员，检查员，抽查员，验收员
CREATE_GROUP_LEADER = "m"
UPDATE_GROUP_LEADER = "r"
CREATE_REVIEWER = "test_reviewer"
UPDATE_REVIEWER = "r"

# 标注和检查时间
CREATE_EDIT_TIME = "240"
CREATE_CHECK_TIME = "180"
UPDATE_EDIT_TIME = "200"
UPDATE_CHECK_TIME = "300"
# 任务池工作进度收件人
SCHEDULE_EMAIL = "zhousuping@megvii.com"
UPDATE_SCHEDULE_EMAIL = "zhousuping@megvii.com,liyubao@megvii.com"

# 任务池工作量统计收件人
STATISTIC = "zhousuping@megvii.com"
UPDATE_STATISTIC_EMAIL = "zhousuping@megvii.com,liyubao@megvii.com"

# 工作流收件人
TASK_FLOW_EMAIL = "zhousuping@megvii.com"
UPDATE_TASK_FLOW_EMAIL="zhousuping@megvii.com,liyubao@megvii.com"

# 统计页面 ########################################################################################
# 任务池-工作量统计页面url
TASK_POOL_STATISTIC_URL = "statistics/flow/task-pools"
# 任务池-列表xpath前半部分
LIST_XPATH = '//*[@id="salary-list"]/table/tbody/tr'
# 老的工作量统计页面url
OLD_STATISTIC_URL = "manager/statistic/task-type"
# 我的工作量统计页面url
MY_STATISTIC_URL = "me/statistic/task-type"

# 任务池进度页面url
POOL_PROGRESS_URL = "spa/manager/taskflow/pool-progress?type=4"
PROGRESS_XPATH = '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr'



