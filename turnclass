# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 19:01:07 2018

@author: luo xi yang
"""
import xml.etree.cElementTree as ET
import csv
import os
class TurnClass():
    def __init__(self,filepath):
        self.filepath=filepath
        
    def Xml_Turn_Csv(self):
        #tree = et.ElementTree(file="C:/Users/luo xi yang/Desktop/temp_workspace/python/pre.xml")
        tree = ET.ElementTree(file=self.filepath)
        root = tree.getroot()
        
        """
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%提取相应的数据，存入列表%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        """
        all_data_for_tag,all_data_for_attrib=[],[]
        for spectrum_list in root.iter('spectrumList'):
            #print(spectrum_list [0].attrib)
            #print(spectrum_list [0].tag)
            for spectrum in spectrum_list .iter():
                print("Output test for Spectrum.tag:\n ",str(spectrum.tag))
                print("Output test for Spectrum.attrib:\n ",str(spectrum.attrib))
                all_data_for_tag.append(spectrum.attrib)
                all_data_for_attrib.append(spectrum.attrib)
                
        """
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%取得各个标签对应的值%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        """
        key_for_label_of_dictionary,values_for_value_of_dictionary=[],[]
        for temp_value in range(len(all_data_for_attrib)):
            print("Output test for all_data_for_attrib:\n",str(all_data_for_attrib[temp_value]))
            if len(all_data_for_attrib[temp_value])==0:
                pass
            else:
                for k,v in all_data_for_attrib[temp_value].items():
                    key_for_label_of_dictionary.append(k)
                    values_for_value_of_dictionary.append(v)
        print("Output test for Label and Values of Dictionary :\n")
        print(key_for_label_of_dictionary,values_for_value_of_dictionary)
        return key_for_label_of_dictionary,values_for_value_of_dictionary
        
    def save_to_csv(self):
        """
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%将取得的标签和值按两行写入csv文件%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        """
        """Get the return value from Xml_Turn_Csv（self）"""
        all_data = TurnClass.Xml_Turn_Csv(self)
        key_for_label_of_dictionary=list(all_data)[0]
        values_for_value_of_dictionary = list(all_data)[1]
        
        temp_key,temp_value,temp_Merge_list =[],[],[]
        
        """Setting the save path for the CSV file """
        savepath='D:'
        filename = "/test.csv"
        savepath_for_csv = savepath+filename
        print('save\n\n\n',str(savepath_for_csv))
        #'C:/Users/luo xi yang/Desktop/test.csv'
        
        """Start writing to the CSV file """
        with open(os.path.abspath(savepath_for_csv), 'w',newline ='') as csvfile:
            spamwriter=csv.writer(csvfile,dialect='excel')
            for position_of_key in range(len(key_for_label_of_dictionary)):
                temp_key.append(key_for_label_of_dictionary[position_of_key])
                temp_value.append(values_for_value_of_dictionary[position_of_key])
                temp_Merge_list=temp_key+temp_value#这样可以使得键值对同时添加到两列中
                print("Output test for Cell of CSV:\n",str(temp_Merge_list))
                spamwriter.writerow(temp_Merge_list) 
                #使用[X]来输入，不然会一个字母占一格子
                del temp_Merge_list[0],temp_key[0],temp_value[0]
                #需要使用del来使得temp从新为空，不然会输出为阶梯状
