from django.db import models

class Bonethree(models.Model):
	name=models.CharField(max_length=500)
	course=models.CharField(max_length=150)
	course_code=models.CharField(max_length=100)
	year=models.CharField(max_length=100)
	link=models.CharField(max_length=100)
	
	

class Bonetwo(models.Model):
	description=models.CharField(max_length=500)
	add_info=models.CharField(max_length=150)
	link=models.CharField(max_length=100)

class Boneone(models.Model):
	description=models.CharField(max_length=500)
	add_info=models.CharField(max_length=150)
	link=models.CharField(max_length=100)

class Bonefour(models.Model):
	description=models.CharField(max_length=500)
	add_info=models.CharField(max_length=150)
	link=models.CharField(max_length=100)

class Bonefive(models.Model):
	name=models.CharField(max_length=500)
	mode_course=models.CharField(max_length=150)
	course_code=models.CharField(max_length=100)
	year=models.CharField(max_length=100)
	hours=models.CharField(max_length=100)
	st_enrolled=models.CharField(max_length=100)
	st_completed=models.CharField(max_length=100)
	link=models.CharField(max_length=100)	


class Bonesix(models.Model):
	name=models.CharField(max_length=500)
	code=models.CharField(max_length=100)
	component_choice=models.CharField(max_length=100)
	component_name=models.CharField(max_length=100)
	component_code=models.CharField(max_length=100)
	student=models.CharField(max_length=100)
	link=models.CharField(max_length=100)		


class Boneseven(models.Model):
	year=models.CharField(max_length=100)
	choice=models.CharField(max_length=300)
	link=models.CharField(max_length=100)

class Btwoone(models.Model):
	year=models.CharField(max_length=5)
	program=models.CharField(max_length=500)
	code=models.CharField(max_length=150)
	no_sanction=models.CharField(max_length=100)
	no_admitted=models.CharField(max_length=100)
	
class Btwotwo(models.Model):
	year=models.CharField(max_length=100)
	res_sc=models.CharField(max_length=10)
	res_st=models.CharField(max_length=10)
	res_obc=models.CharField(max_length=10)
	res_general=models.CharField(max_length=10)
	res_others=models.CharField(max_length=10)
	adm_sc=models.CharField(max_length=10)
	adm_st=models.CharField(max_length=10)
	adm_obc=models.CharField(max_length=10)
	adm_general=models.CharField(max_length=10)
	adm_others=models.CharField(max_length=10)

class Btwothree(models.Model):
	description=models.CharField(max_length=500)
	add_info=models.CharField(max_length=150)
	link=models.CharField(max_length=100)

class Btwofour(models.Model):
	description=models.CharField(max_length=500)
	add_info=models.CharField(max_length=150)
	link=models.CharField(max_length=100)

class Btwofive(models.Model):
	description=models.CharField(max_length=500)
	add_info=models.CharField(max_length=150)
	list_active_mem=models.CharField(max_length=150)
	link=models.CharField(max_length=100)

class Btwosix(models.Model):
	description=models.CharField(max_length=500)
	add_info=models.CharField(max_length=150)
	link=models.CharField(max_length=100)

class Btwoseven(models.Model):
	year=models.CharField(max_length=100)
	prof=models.CharField(max_length=100)
	associate_prof=models.CharField(max_length=100)
	assisstant_prof=models.CharField(max_length=100)
	total=models.CharField(max_length=100)
	authority=models.CharField(max_length=100)
	name=models.CharField(max_length=100)
	designation=models.CharField(max_length=100)
	year_app=models.CharField(max_length=100)
	nature=models.CharField(max_length=100)
	dept_name=models.CharField(max_length=100)	

class Btwoeight(models.Model):
	sl_no=models.CharField(max_length=500)
	name=models.CharField(max_length=150)
	year_join=models.CharField(max_length=100)
	qualification=models.CharField(max_length=100)
	year_qual=models.CharField(max_length=100)

class Btwonine(models.Model):
	sl_no=models.CharField(max_length=500)
	name=models.CharField(max_length=150)
	year=models.CharField(max_length=10)
	experience=models.CharField(max_length=100)
	
class Btwoten(models.Model):
	year=models.CharField(max_length=5)
	programme=models.CharField(max_length=500)
	date_exam=models.CharField(max_length=10)
	date_result=models.CharField(max_length=10)
	gap=models.CharField(max_length=100)
	
class Btwoeleven(models.Model):
	name=models.CharField(max_length=150)
	type_complain=models.CharField(max_length=100)
	
class Btwotwelve(models.Model):
	choice=models.CharField(max_length=50)

class Btwothirteen(models.Model):
	description=models.CharField(max_length=500)
	add_info=models.CharField(max_length=150)
	link=models.CharField(max_length=100)	
	PO_CO=models.CharField(max_length=100)

class Btwofourteen(models.Model):
	year=models.CharField(max_length=5)
	code=models.CharField(max_length=100)
	name=models.CharField(max_length=150)
	name_student=models.CharField(max_length=100)	
	cleared=models.CharField(max_length=100)	
		
class Btwofifteen(models.Model):
	year=models.CharField(max_length=5)
	name_student=models.CharField(max_length=100)
	gender=models.CharField(max_length=150)
	category=models.CharField(max_length=100)	
	domicile_state=models.CharField(max_length=100)
	nationality=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	name_program=models.CharField(max_length=100)
	st_UID=models.CharField(max_length=100)
	mobile=models.CharField(max_length=100)
	year_join=models.CharField(max_length=100)


class Bthreeone(models.Model):
	description=models.CharField(max_length=500)
	add_info=models.CharField(max_length=150)
	link=models.CharField(max_length=100)

class Bthreetwo(models.Model):
	sl_no=models.CharField(max_length=500)
	name=models.CharField(max_length=100)
	amount=models.CharField(max_length=100)
	date=models.CharField(max_length=150)
	link=models.CharField(max_length=100)

class Bthreethree(models.Model):
	teacher_name=models.CharField(max_length=500)
	fellowship_name=models.CharField(max_length=100)
	financial_support=models.CharField(max_length=100)
	purpose=models.CharField(max_length=150)
	status=models.CharField(max_length=150)
	agency=models.CharField(max_length=150)
	year=models.CharField(max_length=150)
	link=models.CharField(max_length=150)

class Bthreefour(models.Model):
	name=models.CharField(max_length=500)
	grant=models.CharField(max_length=100)
	agency=models.CharField(max_length=150)
	year=models.CharField(max_length=150)
	period=models.CharField(max_length=150)

class Bthreefive(models.Model):
	sl_no=models.CharField(max_length=500)
	name_person=models.CharField(max_length=500)
	title=models.CharField(max_length=100)
	name_agency=models.CharField(max_length=100)
	duration=models.CharField(max_length=150)
	year=models.CharField(max_length=150)
	amount=models.CharField(max_length=150)

class Bthreesix(models.Model):
	description=models.CharField(max_length=500)
	add_info=models.CharField(max_length=150)
	link=models.CharField(max_length=100)

class Bthreethreetwo(models.Model):
	name_awardee=models.CharField(max_length=500)
	name_award=models.CharField(max_length=500)
	name_body=models.CharField(max_length=500)
	award_category=models.CharField(max_length=500)
	award_year=models.CharField(max_length=500)

class Bthreeseven(models.Model):
	choice=models.CharField(max_length=1)

class Bthreeeight(models.Model):
	name=models.CharField(max_length=500)
	patent_number=models.CharField(max_length=150)
	date=models.CharField(max_length=100)
	agency=models.CharField(max_length=100)

class Bthreenine(models.Model):
	name_scholar=models.CharField(max_length=500)
	name_superviser=models.CharField(max_length=500)
	year_reg=models.CharField(max_length=150)
	year_completed=models.CharField(max_length=100)

class Bthreeten(models.Model):
	title=models.CharField(max_length=500)
	name_author=models.CharField(max_length=500)
	teacher_dept=models.CharField(max_length=150)
	name_journal=models.CharField(max_length=100)
	year=models.CharField(max_length=500)
	issn=models.CharField(max_length=500)
	link_website=models.CharField(max_length=150)
	link_article=models.CharField(max_length=100)
	listed=models.CharField(max_length=100)


class Bthreeeleven(models.Model):
	sl_no=models.CharField(max_length=500)
	name_teacher=models.CharField(max_length=500)
	title_book=models.CharField(max_length=100)
	title_chapter=models.CharField(max_length=100)
	year=models.CharField(max_length=150)
	isbn=models.CharField(max_length=100)
	affiliating_inst=models.CharField(max_length=150)
	name_publisher=models.CharField(max_length=150)


class Bthreetwelve(models.Model):
	choice=models.CharField(max_length=1)

class Bthreethirteen(models.Model):
	name=models.CharField(max_length=500)
	org=models.CharField(max_length=150)
	duration=models.CharField(max_length=100)
	amount=models.CharField(max_length=100)

class Bthreefourteen(models.Model):
	name=models.CharField(max_length=500)
	org_unit=models.CharField(max_length=150)
	date=models.CharField(max_length=100)
	no_of_students=models.CharField(max_length=100)

class Bthreefifteen(models.Model):
	year=models.CharField(max_length=500)
	name=models.CharField(max_length=500)
	duration=models.CharField(max_length=500)
	purpose=models.CharField(max_length=150)
	list_activities=models.CharField(max_length=100)
	date=models.CharField(max_length=100)



class Bfourone (models.Model):
	description=models.CharField(max_length=500)
	add_info=models.CharField(max_length=150)
	link=models.CharField(max_length=100)

class Bfourtwo(models.Model):
	head_expenditure=models.CharField(max_length=500)
	item=models.CharField(max_length=150)
	infra_expenditure=models.CharField(max_length=500)
	book_expenditure=models.CharField(max_length=500)
	physical_expenditure=models.CharField(max_length=500)
	salary_expenditure=models.CharField(max_length=500)
	other_expenditure=models.CharField(max_length=500)
	year=models.CharField(max_length=500)

class Bfourthree (models.Model):
	description=models.CharField(max_length=500)
	add_info=models.CharField(max_length=150)
	link=models.CharField(max_length=100)

class Bfourfour (models.Model):
	description=models.CharField(max_length=500)
	add_info=models.CharField(max_length=150)
	link=models.CharField(max_length=100)

class Bfourfive (models.Model):
	description=models.CharField(max_length=500)
	add_info=models.CharField(max_length=150)
	link=models.CharField(max_length=100)

class Bfoursix(models.Model):
	add_mix_edit=models.CharField(max_length=500)
	lcs=models.CharField(max_length=150)
	central_inst=models.CharField(max_length=500)
	animal_house=models.CharField(max_length=500)
	museum=models.CharField(max_length=500)
	business_lab=models.CharField(max_length=500)
	reasearch=models.CharField(max_length=500)
	mootcourt=models.CharField(max_length=500)
	theatre=models.CharField(max_length=500)
	art=models.CharField(max_length=500)
	others=models.CharField(max_length=500)

class Bfourseven (models.Model):
	description=models.CharField(max_length=500)
	add_info=models.CharField(max_length=150)
	link=models.CharField(max_length=100)



class Bfiveone(models.Model):
	year=models.CharField(max_length=500)
	title=models.CharField(max_length=500)
	no_of_students=models.CharField(max_length=500)
	amount=models.CharField(max_length=150)
	agency=models.CharField(max_length=100)
	link=models.CharField(max_length=100)


class Bfivetwo (models.Model):
	description=models.CharField(max_length=500)
	add_info=models.CharField(max_length=150)
	link=models.CharField(max_length=100)

class Bfivethree(models.Model):
	choice=models.CharField(max_length=1)

class Bfivefour(models.Model):
	choice=models.CharField(max_length=1)

class Bfivefive (models.Model):
	year=models.CharField(max_length=500)
	sl_no=models.CharField(max_length=500)
	student_placed=models.CharField(max_length=150)
	org_placed=models.CharField(max_length=100)
	package=models.CharField(max_length=100)

class Bfivesix (models.Model):
	year=models.CharField(max_length=500)
	sl_no=models.CharField(max_length=500)
	higher_ed=models.CharField(max_length=150)
	org=models.CharField(max_length=100)
	details=models.CharField(max_length=100)

class Bfiveseven (models.Model):
	year=models.CharField(max_length=500)
	name_st=models.CharField(max_length=150)
	year_qual=models.CharField(max_length=100)
	level_exam=models.CharField(max_length=100)
	name_exam=models.CharField(max_length=100)
	link=models.CharField(max_length=100)

class Bfiveeight (models.Model):
	year=models.CharField(max_length=4)
	name_st=models.CharField(max_length=150)
	name_event=models.CharField(max_length=150)
	date_event=models.CharField(max_length=150)
	team_individual=models.CharField(max_length=150)
	type_int=models.CharField(max_length=100)
	position=models.CharField(max_length=100)
	name_org=models.CharField(max_length=100)

class Bfivenine (models.Model):
	description=models.CharField(max_length=500)
	add_info=models.CharField(max_length=150)
	link=models.CharField(max_length=100)

class Bfiveten (models.Model):
	year=models.CharField(max_length=500)
	date_event=models.CharField(max_length=150)
	type_event=models.CharField(max_length=100)
	name_event=models.CharField(max_length=100)
	link=models.CharField(max_length=100)

class Bfiveeleven (models.Model):
	description=models.CharField(max_length=500)
	add_info=models.CharField(max_length=150)
	link=models.CharField(max_length=100)


class Bsixone (models.Model):
	description=models.CharField(max_length=500)
	add_info=models.CharField(max_length=150)
	link=models.CharField(max_length=100)

class Bsixtwo (models.Model):
	description=models.CharField(max_length=500)
	inst_docs=models.CharField(max_length=150)
	add_info=models.CharField(max_length=150)
	link=models.CharField(max_length=100)


class Bsixthree (models.Model):
	area=models.CharField(max_length=500)
	option=models.CharField(max_length=150)
	link=models.CharField(max_length=100)

class Bsixfour (models.Model):
	description=models.CharField(max_length=500)
	add_info=models.CharField(max_length=150)
	link=models.CharField(max_length=100)


class Bsixfive (models.Model):
	date=models.CharField(max_length=500)
	title=models.CharField(max_length=150)
	name_teacher=models.CharField(max_length=100)
	amount_HEI=models.CharField(max_length=100)
	purpose=models.CharField(max_length=100)

class Bsixsix (models.Model):
	year=models.CharField(max_length=500)
	name_faculty=models.CharField(max_length=500)
	type_prog=models.CharField(max_length=150)
	duration=models.CharField(max_length=100)
	start_end_date=models.CharField(max_length=100)
	name_inst=models.CharField(max_length=100)

class Bsixseven (models.Model):
	description=models.CharField(max_length=500)
	add_info=models.CharField(max_length=150)
	link=models.CharField(max_length=100)

class Bsixeight (models.Model):
	year=models.CharField(max_length=500)
	name=models.CharField(max_length=150)
	purpose=models.CharField(max_length=100)
	funds_receive=models.CharField(max_length=100)
	link=models.CharField(max_length=100)


class Bsixnine (models.Model):
	description=models.CharField(max_length=500)
	add_info=models.CharField(max_length=150)
	link=models.CharField(max_length=100)

class Bsixten (models.Model):
	description=models.CharField(max_length=500)
	add_info=models.CharField(max_length=150)
	link=models.CharField(max_length=100)

class Bsixeleven (models.Model):
	description=models.CharField(max_length=500)
	add_info=models.CharField(max_length=150)
	link=models.CharField(max_length=100)

class Bsixtwelve (models.Model):
	qual_insurance=models.CharField(max_length=500)
	option=models.CharField(max_length=150)
	link=models.CharField(max_length=100)

class Bsevenone (models.Model):
	description=models.CharField(max_length=500)
	add_info=models.CharField(max_length=150)
	link=models.CharField(max_length=100)

class Bseventwo (models.Model):
	alt_source=models.CharField(max_length=500)
	option=models.CharField(max_length=150)
	link=models.CharField(max_length=100)

class Bseventhree (models.Model):
	description=models.CharField(max_length=500)
	add_info=models.CharField(max_length=150)
	link=models.CharField(max_length=100)
	photo=models.CharField(max_length=100)

class Bsevenfour (models.Model):
	facilities=models.CharField(max_length=500)
	option=models.CharField(max_length=150)
	link=models.CharField(max_length=100)
	photo=models.CharField(max_length=100)

class Bsevenfive (models.Model):
	description=models.CharField(max_length=1000)
	photo=models.CharField(max_length=100)
	report=models.CharField(max_length=250)
	policy_doc=models.CharField(max_length=250)
	link=models.CharField(max_length=100)

class Bsevensix (models.Model):
	initiative=models.CharField(max_length=500)
	option=models.CharField(max_length=150)
	link=models.CharField(max_length=100)

class Bsevenseven (models.Model):
	description=models.CharField(max_length=500)
	add_info=models.CharField(max_length=150)
	link=models.CharField(max_length=100)

class Bseveneight (models.Model):
	description=models.CharField(max_length=500)
	add_info=models.CharField(max_length=150)
	link=models.CharField(max_length=100)

class Bsevennine (models.Model):
	description=models.CharField(max_length=500)
	details=models.CharField(max_length=250)
	link=models.CharField(max_length=100)

class Bseventen (models.Model):
	code_conduct=models.CharField(max_length=200)
	option=models.CharField(max_length=150)
	link=models.CharField(max_length=100)

class Bseveneleven (models.Model):
	description=models.CharField(max_length=500)
	
class Bseventwelve (models.Model):
	description=models.CharField(max_length=500)
	webpage_link=models.CharField(max_length=150)
	add_info=models.CharField(max_length=100)

class Aoneone (models.Model):
	intro=models.CharField(max_length=500)

class Aonetwo (models.Model):
	cir_aspects=models.CharField(max_length=500)
	evaluation=models.CharField(max_length=500)
	research=models.CharField(max_length=500)
	infra=models.CharField(max_length=500)
	student=models.CharField(max_length=500)
	govt=models.CharField(max_length=500)
	inst_values=models.CharField(max_length=500)
	
class Aonethree (models.Model):
	inst_strength=models.CharField(max_length=500)
	inst_weakness=models.CharField(max_length=500)
	inst_opp=models.CharField(max_length=500)
	inst_chall=models.CharField(max_length=500)

class Aonefour (models.Model):
	add_info=models.CharField(max_length=500)
	
class Aonefive (models.Model):
	functioning=models.CharField(max_length=500)

class Atwoone (models.Model):
	name=models.CharField(max_length=150)
	address=models.CharField(max_length=150)
	city=models.CharField(max_length=100)
	state=models.CharField(max_length=150)
	pin=models.CharField(max_length=50)
	website=models.CharField(max_length=150)

class Atwotwo (models.Model):
	desig=models.CharField(max_length=150)
	name=models.CharField(max_length=150)
	tele=models.CharField(max_length=100)
	mobile=models.CharField(max_length=10)
	fax=models.CharField(max_length=50)
	email=models.CharField(max_length=150)

class Atwothree (models.Model):
	nature=models.CharField(max_length=100)

class Atwofour (models.Model):
	type=models.CharField(max_length=100)
	
class Atwofive (models.Model):
	date_uni=models.CharField(max_length=50)
	status=models.CharField(max_length=150)
	date=models.CharField(max_length=50)
	
class Atwosix (models.Model):
	date_2F=models.CharField(max_length=50)
	date_12B=models.CharField(max_length=50)
	doc_2F=models.CharField(max_length=100)
	doc_12B=models.CharField(max_length=100)
	
class Atwoseven (models.Model):
	UPE=models.CharField(max_length=50)

class Atwoeight (models.Model):
	type=models.CharField(max_length=100)
	address=models.CharField(max_length=150)
	loc=models.CharField(max_length=100)
	area=models.CharField(max_length=150)
	built_area=models.CharField(max_length=50)
	prog=models.CharField(max_length=150)
	date_est=models.CharField(max_length=50)
	date_rec=models.CharField(max_length=50)

class Atwonine (models.Model):
	const=models.CharField(max_length=50)
	aff=models.CharField(max_length=50)
	clg_2F=models.CharField(max_length=50)
	clg_2F_12B=models.CharField(max_length=50)
	naac=models.CharField(max_length=50)
	ugc=models.CharField(max_length=50)
	auto=models.CharField(max_length=50)
	postgrd=models.CharField(max_length=50)
	clg_res=models.CharField(max_length=50)
	uni_res=models.CharField(max_length=50)
	
class Atwoten(models.Model):
	option=models.CharField(max_length=50)
	sra=models.CharField(max_length=50)
	doc=models.CharField(max_length=50)
	
class Atwoeleven(models.Model):
	prof_total_sanc=models.CharField(max_length=250)
	prof_rec_male=models.CharField(max_length=250)
	prof_rec_female=models.CharField(max_length=250)
	prof_rec_others=models.CharField(max_length=250)
	prof_rec_total=models.CharField(max_length=250)
	prof_rec_total_yet=models.CharField(max_length=250)
	prof_con_male=models.CharField(max_length=250)
	prof_con_female=models.CharField(max_length=250)
	prof_con_others=models.CharField(max_length=250)
	prof_con_total=models.CharField(max_length=250)
	assc_total_sanc=models.CharField(max_length=250)
	assc_rec_male=models.CharField(max_length=250)
	assc_rec_female=models.CharField(max_length=250)
	assc_rec_others=models.CharField(max_length=250)
	assc_rec_total=models.CharField(max_length=250)
	assc_rec_total_yet=models.CharField(max_length=250)
	assc_con_male=models.CharField(max_length=250)
	assc_con_female=models.CharField(max_length=250)
	assc_con_others=models.CharField(max_length=250)
	assc_con_total=models.CharField(max_length=250)
	assis_total_sanc=models.CharField(max_length=250)
	assis_rec_male=models.CharField(max_length=250)
	assis_rec_female=models.CharField(max_length=250)
	assis_rec_others=models.CharField(max_length=250)
	assis_rec_total=models.CharField(max_length=250)
	assis_rec_total_yet=models.CharField(max_length=250)
	assis_con_male=models.CharField(max_length=250)
	assis_con_female=models.CharField(max_length=250)
	assis_con_others=models.CharField(max_length=250)
	assis_con_total=models.CharField(max_length=250)

class Atwotwelve(models.Model):
	total_sanc_male=models.CharField(max_length=250)
	total_sanc_female=models.CharField(max_length=250)
	total_sanc_others=models.CharField(max_length=250)
	total_sanc_total=models.CharField(max_length=250)
	rec_male=models.CharField(max_length=250)
	rec_female=models.CharField(max_length=250)
	rec_others=models.CharField(max_length=250)
	rec_total=models.CharField(max_length=250)
	yet_rec_male=models.CharField(max_length=250)
	yet_rec_female=models.CharField(max_length=250)
	yet_rec_others=models.CharField(max_length=250)
	yet_rec_total=models.CharField(max_length=250)
	con_male=models.CharField(max_length=250)
	con_female=models.CharField(max_length=250)
	con_others=models.CharField(max_length=250)
	con_total=models.CharField(max_length=250)
	
class Atwothirteen(models.Model):
	total_sanc_male=models.CharField(max_length=250)
	total_sanc_female=models.CharField(max_length=500)
	total_sanc_others=models.CharField(max_length=500)
	total_sanc_total=models.CharField(max_length=500)
	rec_male=models.CharField(max_length=500)
	rec_female=models.CharField(max_length=500)
	rec_others=models.CharField(max_length=500)
	rec_total=models.CharField(max_length=500)
	yet_rec_male=models.CharField(max_length=500)
	yet_rec_female=models.CharField(max_length=500)
	yet_rec_others=models.CharField(max_length=500)
	yet_rec_total=models.CharField(max_length=500)
	con_male=models.CharField(max_length=500)
	con_female=models.CharField(max_length=500)
	con_others=models.CharField(max_length=500)
	con_total=models.CharField(max_length=500)
	
class Atwofourteen(models.Model):
	prof_highest_qual=models.CharField(max_length=250)
	prof_male=models.CharField(max_length=500)
	prof_female=models.CharField(max_length=500)
	prof_others=models.CharField(max_length=500)
	assc_highest_qual=models.CharField(max_length=250)
	assc_male=models.CharField(max_length=500)
	assc_female=models.CharField(max_length=500)
	assc_others=models.CharField(max_length=500)
	assis_highest_qual=models.CharField(max_length=250)
	assis_male=models.CharField(max_length=500)
	assis_female=models.CharField(max_length=500)
	assis_others=models.CharField(max_length=500)

class Atwofifteen(models.Model):
	prof_highest_qual=models.CharField(max_length=250)
	prof_male=models.CharField(max_length=500)
	prof_female=models.CharField(max_length=500)
	prof_others=models.CharField(max_length=500)
	assc_highest_qual=models.CharField(max_length=250)
	assc_male=models.CharField(max_length=500)
	assc_female=models.CharField(max_length=500)
	assc_others=models.CharField(max_length=500)
	assis_highest_qual=models.CharField(max_length=250)
	assis_male=models.CharField(max_length=500)
	assis_female=models.CharField(max_length=500)
	assis_others=models.CharField(max_length=500)

class Atwosixteen(models.Model):
	prof_highest_qual=models.CharField(max_length=250)
	prof_male=models.CharField(max_length=500)
	prof_female=models.CharField(max_length=500)
	prof_others=models.CharField(max_length=500)
	assc_highest_qual=models.CharField(max_length=250)
	assc_male=models.CharField(max_length=500)
	assc_female=models.CharField(max_length=500)
	assc_others=models.CharField(max_length=500)
	assis_highest_qual=models.CharField(max_length=250)
	assis_male=models.CharField(max_length=500)
	assis_female=models.CharField(max_length=500)
	assis_others=models.CharField(max_length=500)

class Atwoseventeen(models.Model):
	
	emer_prof_male=models.CharField(max_length=500)
	emer_prof_female=models.CharField(max_length=500)
	emer_prof_others=models.CharField(max_length=500)
	emer_prof_total=models.CharField(max_length=250)
	adj_prof_male=models.CharField(max_length=500)
	adj_prof_female=models.CharField(max_length=500)
	adj_prof_others=models.CharField(max_length=500)
	adj_prof_total=models.CharField(max_length=250)
	vis_prof_male=models.CharField(max_length=500)
	vis_prof_female=models.CharField(max_length=500)
	vis_prof_others=models.CharField(max_length=500)
	vis_prof_total=models.CharField(max_length=250)
	
class Atwoeightteen(models.Model):
	
	sl_no=models.CharField(max_length=500)
	name_dept=models.CharField(max_length=500)
	name_chair=models.CharField(max_length=500)
	name_org=models.CharField(max_length=250)

class Atwonineteen(models.Model):
	
	prog_name=models.CharField(max_length=500)
	own_state_male=models.CharField(max_length=500)
	own_state_female=models.CharField(max_length=500)
	own_state_others=models.CharField(max_length=500)
	other_states_male=models.CharField(max_length=500)
	other_states_female=models.CharField(max_length=500)
	other_states_others=models.CharField(max_length=500)
	NRI_stud_male=models.CharField(max_length=500)
	NRI_stud_female=models.CharField(max_length=500)
	NRI_stud_others=models.CharField(max_length=500)
	foreign_male=models.CharField(max_length=500)
	foreign_female=models.CharField(max_length=500)
	foreign_others=models.CharField(max_length=500)
	total_male=models.CharField(max_length=500)
	total_female=models.CharField(max_length=500)
	total_others=models.CharField(max_length=500)

class Atwotwenty(models.Model):
	
	ques=models.CharField(max_length=500)
	total=models.CharField(max_length=500)
	
class Atwotwentyone(models.Model):
	
	own_state_male=models.CharField(max_length=500)
	own_state_female=models.CharField(max_length=500)
	own_state_others=models.CharField(max_length=500)
	other_states_male=models.CharField(max_length=500)
	other_states_female=models.CharField(max_length=500)
	other_states_others=models.CharField(max_length=500)
	NRI_stud_male=models.CharField(max_length=500)
	NRI_stud_female=models.CharField(max_length=500)
	NRI_stud_others=models.CharField(max_length=500)
	foreign_male=models.CharField(max_length=500)
	foreign_female=models.CharField(max_length=500)
	foreign_others=models.CharField(max_length=500)
	total_male=models.CharField(max_length=500)
	total_female=models.CharField(max_length=500)
	total_others=models.CharField(max_length=500)

class Atwotwentytwo(models.Model):
	
	year=models.CharField(max_length=50)
	num_UGC_orien=models.CharField(max_length=500)
	num_UGC_refresher=models.CharField(max_length=500)
	num_uni_prog=models.CharField(max_length=250)
	total_num_prog=models.CharField(max_length=250)

class Atwotwentythree(models.Model):
	
	dept_name=models.CharField(max_length=150)
	report=models.FileField(max_length=1000)
	
class Atwotwentyfour(models.Model):
	
	description=models.CharField(max_length=500)
	
class Atwotwentyfive(models.Model):
	
	description=models.CharField(max_length=500)
	
class Athreeone(models.Model):
	
	year=models.CharField(max_length=50)
	num_stud=models.CharField(max_length=500)
	description=models.FileField(max_length=1000)
	inst_data=models.FileField(max_length=1000)
	
class Athreetwo(models.Model):
	
	year=models.CharField(max_length=50)
	num_stud=models.CharField(max_length=500)
	description=models.FileField(max_length=1000)
	inst_data=models.FileField(max_length=1000)
	
class Athreethree(models.Model):
	
	year=models.CharField(max_length=50)
	num_teacher=models.CharField(max_length=500)
	description=models.FileField(max_length=1000)
	inst_data=models.FileField(max_length=1000)
	
class Athreefour(models.Model):
	
	total=models.CharField(max_length=500)

class Athreefive(models.Model):
	
	year=models.CharField(max_length=150)
	total_exp=models.CharField(max_length=500)
