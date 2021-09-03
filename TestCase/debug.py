# -- coding:utf-8 --
import os
report_path = '.\\reprot\\test_report.htlm'



project_dir = os.path.abspath(os.path.dirname(__file__))
# report_path = project_dir + r'\report\test_report.html'
report_path = r'E:\python_code\alwin\appium_jmbon\report\test_report.html'
with open(report_path,'w') as f:
    tmpe = f.readlines()
    print(tmpe)

print(report_path)