import pandas as pd
import json
from string import punctuation
import re
import argparse

key_exp = ['Kinh nghiệm làm việc', 
           'Kinh nghiệm', 
           'Kinh nghiệm làm việc và kỹ năng',
           'Experience',
           ]

key_job = ['Công việc mong muốn',
           'Công việc',
           'Công việc hiện tại',
           'Job'
            ]

key_obj = ['Mục tiêu nghề nghiệp',
            'Mục tiêu',
            'Mục tiêu nghề nghiệp và sự nghiệp',
            'Objective'
            ]

key_edu = ['Trình độ học vấn',
            'Trình độ',
            'Trình độ học vấn và bằng cấp',
            'Học vấn',
            'Education'
            ]

key_skill = ['Kỹ năng',
            'Kỹ năng và sở trường',
            'Skills'
            ]

key_add = ['Địa chỉ làm việc',
            'Địa chỉ',
            'Địa chỉ thường trú'
            ]

key_award = ['Giải thưởng',
            'Giải thưởng và thành tích',
            'Awards'
            ]

key_cert = ['Chứng chỉ',
            'Chứng chỉ và kỹ năng',
            'Certifications'
            ]

key_hobby = ['Sở thích',
            'Sở thích và tính cách',
            'Hobbies'
            ]

key_ref = ['Người tham chiếu',
            'Người tham chiếu và thông tin thêm',
            'References'
            ]

key_act = ['Hoạt động',
            'Hoạt động và dự án',
            'Activities'
            ]

key_pro = ['Dự án',
            'Dự án đã tham gia',
            'Projects'
            ]

key_info = ['Thông tin thêm',
            'Thông tin thêm về bản thân',
            'Additional information'
            ]

features = {'key_exp': key_exp,
            'key_job': key_job,
            'key_obj': key_obj,
            'key_edu': key_edu,
            'key_skill': key_skill,
            'key_add': key_add,
            'key_award': key_award,
            'key_cert': key_cert,
            'key_hobby': key_hobby,
            'key_ref': key_ref,
            'key_act': key_act,
            'key_pro': key_pro,
            'key_info': key_info
            }

map_features = {'key_exp': 'Kinh nghiệm làm việc',
                'key_job': 'Công việc mong muốn',
                'key_obj': 'Mục tiêu nghề nghiệp',
                'key_edu': 'Trình độ học vấn',
                'key_skill': 'Kỹ năng',
                'key_add': 'Địa chỉ làm việc',
                'key_award': 'Giải thưởng',
                'key_cert': 'Chứng chỉ',
                'key_hobby': 'Sở thích',
                'key_ref': 'Người tham chiếu',
                'key_act': 'Hoạt động',
                'key_pro': 'Dự án',
                'key_info': 'Thông tin bổ sung'
                }

infos = ['Avatar',
        'Họ và tên',
        'Vị trí mong muốn làm', 
        'Số điện thoại',
        'Ngày/tháng/năm sinh',
        'Email',
        'Giới tính',
        'Địa chỉ hiện tại',
        'Kinh nghiệm làm việc', 
        'Mục tiêu nghề nghiệp', 
        'Trình độ học vấn', 
        'Kỹ năng', 
        'Địa chỉ làm việc', 
        'Giải thưởng', 
        'Chứng chỉ', 
        'Sở thích', 
        'Người tham chiếu', 
        'Hoạt động', 
        'Dự án tham gia', 
        'Thông tin bổ sung'
    ]

# remove vietnamese accents
s1 = u'ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯưẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ'
s0 = u'AAAAEEEIIOOOOUUYaaaaeeeiioooouuyAaDdIiUuOoUuAaAaAaAaAaAaAaAaAaAaAaAaEeEeEeEeEeEeEeEeIiIiOoOoOoOoOoOoOoOoOoOoOoOoUuUuUuUuUuUuUuYyYyYyYy'
def remove_accents(input_str):
	s = ''
	for c in input_str:
		if c in s1:
			s += s0[s1.index(c)]
		else:
			s += c
	return s

def extract_feature_from_keys(text):
    for key in features.keys():
        for k in features[key]:
            for i in range(len(text.split('\n'))):
                if remove_accents(k.lower()) in remove_accents(text.lower().split('\n')[i]):
                    return map_features[key], text.replace(text.split('\n')[i], '')
    return 'Thông tin bổ sung', text

def resume_extract(avatar, texts, labels):
    result = {}
    
    for info in infos:
        result[info] = ''
    result['Thông tin bổ sung'] = []

    for i, text in enumerate(texts):
        if labels[i] == 'Text':
            feature, res_text = extract_feature_from_keys(text)
            if feature == 'Trình độ học vấn':
                tdhv = ['Cao đẳng', 'Đại học', 'Thạc sĩ', 'Tiến sĩ', 'Trung cấp']
                for td in tdhv:
                    if td in res_text:
                        res_text = td
                        break
            elif feature != 'Thông tin bổ sung':
                result[feature] = res_text
            else:
                result['Thông tin bổ sung'].append(res_text)
        else:
            result[labels[i]] = text

    result['Avatar'] = avatar
    result['Thông tin bổ sung'] = '\n'.join(result['Thông tin bổ sung'])
    return result