from custom_parser import *
import xlsxwriter


group_name,group_dict=json_file_load('APT32.json')
excel_file_name=group_name+'.xlsx'
workbook = xlsxwriter.Workbook(excel_file_name) 
worksheet = workbook.add_worksheet(group_name)
header_cell_format = workbook.add_format({'bold': True, 'border': True, 'bg_color': 'yellow'})
body_cell_format = workbook.add_format({'border': True})
merge_format = workbook.add_format({'border': 1,'align': 'center','valign': 'vcenter'})
worksheet.write(0,0,"TACTIC ID",header_cell_format)
worksheet.write(0,1,"TACTIC NAME",header_cell_format)
worksheet.write(0,2,"TECHNIQUE ID",header_cell_format)
worksheet.write(0,3,"TECHNIQUE NAME",header_cell_format)
worksheet.write(0,4,"PROCEDURE",header_cell_format)

row=1
for k,v in group_dict.items():
	tactic_name=(k.replace("-"," ").title())
	tactic_id=get_tatic_id(tactic_name)
	tactic_url='https://attack.mitre.org/tactics/'+tactic_id
	for tech_id in v:
		tech_name=get_tech_name(tech_id)
		tech_url='https://attack.mitre.org/techniques/'+tech_id
		tech_procedure=get_group_tech_procedure(tech_id)
		worksheet.write_url(row,0,tactic_url,string=tactic_id)
		worksheet.write(row,1,tactic_name,body_cell_format)
		worksheet.write_url(row,2,tech_url,string=tech_id)
		worksheet.write(row,3,tech_name,body_cell_format)
		worksheet.write(row,4,tech_procedure,body_cell_format)		
		row=row+1
workbook.close() 
