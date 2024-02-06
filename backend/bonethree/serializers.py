# import serializers from the REST framework
from rest_framework import serializers

# import the todo data model
from .models import Bonethree,Bonetwo,Boneone,Bonefour,Bonefive,Bonesix,Boneseven,Btwoone,Btwotwo,Btwothree,Btwofour,Btwofive,Btwosix,Btwoseven,Btwoeight,Btwonine,Btwoten,Btwoeleven,Btwotwelve,Btwothirteen,Btwofourteen,Btwofifteen,Bthreeone,Bthreeeight,Bthreeeleven,Bthreefive,Bthreefour,Bthreethreetwo,Bthreefourteen,Bthreenine,Bthreeseven,Bthreesix,Bthreeten,Bthreethirteen,Bthreethree,Bthreetwelve,Bthreetwo,Bthreefifteen,Bfourfive,Bfourfour,Bfourone,Bfourseven,Bfoursix,Bfourthree,Bfourtwo,Bfiveeight,Bfiveeleven,Bfivefive,Bfivefour,Bfivenine,Bfiveone,Bfiveseven,Bfivesix,Bfiveten,Bfivethree,Bfivetwo,Bsixeight,Bsixeleven,Bsixfive,Bsixfour,Bsixnine,Bsixone,Bsixseven,Bsixsix,Bsixten,Bsixthree,Bsixtwelve,Bsixtwo,Bsevenone,Bseventwo,Bseventhree,Bsevenfour,Bsevenfive,Bsevensix,Bsevenseven,Bseveneight,Bsevennine,Bseventen,Bseveneleven,Bseventwelve,Aonefive,Aonefour,Aoneone,Aonethree,Aonetwo,Athreefive,Athreefour,Athreeone,Athreethree,Athreetwo,Atwoeight,Atwoeightteen,Atwoeleven,Atwofifteen,Atwofive,Atwofour,Atwofourteen,Atwonine,Atwonineteen,Atwoone,Atwoseven,Atwoseventeen,Atwosix,Atwosixteen,Atwoten,Atwothirteen,Atwothree,Atwotwelve,Atwotwenty,Atwotwentyfive,Atwotwentyfour,Atwotwentyone,Atwotwentythree,Atwotwentytwo,Atwotwo

# create a serializer class
class BonethreeSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:
		model = Bonethree
		fields = ('id','name','course','course_code','year','link')
		
class BonetwoSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bonetwo
		fields = ('id','description','add_info','link')


class BoneoneSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Boneone
		fields = ('id','description','add_info','link')

class BonefourSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bonefour
		fields = ('id','description','add_info','link')

class BonefiveSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bonefive
		fields = ('id','name','mode_course','course_code','year','hours','st_enrolled','st_completed','link')	


class BonesixSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bonesix
		fields = ('id','name','code','component_choice','component_name','component_code','student','link')	

class BonesevenSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Boneseven
		fields = ('id','year','choice','link')	
class BtwooneSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Btwoone
		fields = ('id','year','program','code','no_sanction','no_admitted')

class BtwotwoSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Btwotwo
		fields = ('id','year','res_sc','res_st','res_obc','res_general','res_others','adm_sc','adm_st','adm_obc','adm_general','adm_others')

class BtwothreeSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Btwothree
		fields = ('id','description','add_info','link')

class BtwofourSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Btwofour
		fields = ('id','description','add_info','link')

class BtwofiveSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Btwofive
		fields = ('id','description','add_info','list_active_mem','link')

class BtwosixSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Btwosix
		fields = ('id','description','add_info','link')

class BtwosevenSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Btwoseven
		fields = ('id','year','prof','associate_prof','assisstant_prof','total','authority','name','designation','year_app','nature','dept_name')

class BtwoeightSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Btwoeight
		fields = ('id','sl_no','name','year_join','qualification','year_qual')

class BtwonineSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Btwonine
		fields = ('id','sl_no','name','year','experience')

class BtwotenSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Btwoten
		fields = ('id','year','programme','date_exam','date_result','gap')

class BtwoelevenSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Btwoeleven
		fields = ('id','name','type_complain')

class BtwotwelveSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Btwotwelve
		fields = ('id','choice')

class BtwothirteenSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Btwothirteen
		fields = ('id','description','add_info','link','PO_CO')

class BtwofourteenSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Btwofourteen
		fields = ('id','year','code','name','name_student','cleared')

class BtwofifteenSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Btwofifteen
		fields = ('id','year','name_student','gender','category','domicile_state','nationality','email','name_program','st_UID','mobile','year_join')

class BthreeoneSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bthreeone
		fields = ('id','description','add_info','link')

class BthreetwoSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bthreetwo
		fields = ('id','sl_no','name','date','amount','link')

class BthreethreeSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bthreethree
		fields = ('id','teacher_name','fellowship_name','financial_support','purpose','status','agency','year','link')

class BthreefourSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bthreefour
		fields = ('id','name','grant','agency','year','period')

class BthreefiveSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bthreefive
		fields = ('id','sl_no','name_person','title','name_agency','duration','year','amount')


class BthreesixSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bthreesix
		fields = ('id','description','add_info','link')

class BthreethreetwoSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bthreethreetwo
		fields = ('id','name_awardee','name_award','name_body','award_category','award_year')


class BthreesevenSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bthreeseven
		fields = ('id','choice')



class BthreeeightSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bthreeeight
		fields = ('id','name','patent_number','date','agency')

class BthreenineSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bthreenine
		fields = ('id','name_scholar','name_superviser','year_reg','year_completed')

class BthreetenSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bthreeten
		fields = ('id','title','name_author','teacher_dept','name_journal','year','issn','link_website','link_article','listed')

class BthreeelevenSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bthreeeleven
		fields = ('id','sl_no','name_teacher','title_book','title_chapter','year','isbn','affiliating_inst','name_publisher')

class BthreetwelveSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bthreetwelve
		fields = ('id','choice')

class BthreethirteenSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bthreethirteen
		fields = ('id','name','org','duration','amount')

class BthreefourteenSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bthreefourteen
		fields = ('id','name','org_unit','date','no_of_students')

class BthreefifteenSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bthreefifteen
		fields = ('id','year','name','duration','purpose','list_activities','date')


class BfouroneSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bfourone
		fields = ('id','description','add_info','link')

class BfourtwoSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bfourtwo
		fields = ('id','head_expenditure','item','infra_expenditure','book_expenditure','physical_expenditure','salary_expenditure','other_expenditure','year')

class BfourthreeSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bfourthree
		fields = ('id','description','add_info','link')

class BfourfourSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bfourfour
		fields = ('id','description','add_info','link')

class BfourfiveSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bfourfive
		fields = ('id','description','add_info','link')

class BfoursixSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bfoursix
		fields = ('id','add_mix_edit','lcs','central_inst','animal_house','museum','business_lab','reasearch','mootcourt','theatre','art','others')

class BfoursevenSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bfourseven
		fields = ('id','description','add_info','link')


class BfiveoneSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bfiveone
		fields = ('id','year','title','no_of_students','amount','agency','link')

class BfivetwoSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bfivetwo
		fields = ('id','description','add_info','link')


class BfivethreeSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bfivethree
		fields = ('id','choice')

class BfivefourSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bfivefour
		fields = ('id','choice')

class BfivefiveSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bfivefive
		fields = ('id','year','sl_no','student_placed','org_placed','package')

class BfivesixSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bfivesix
		fields = ('id','year','sl_no','higher_ed','org','details')

class BfivesevenSerializer(serializers.ModelSerializer):
# create a metyearss
	class Meta:		
		model = Bfiveseven
		fields = ('id','year','name_st','year_qual','level_exam','name_exam','link')

class BfiveeightSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bfiveeight
		fields = ('id','year','name_st','name_event','date_event','team_individual','type_int','position','name_org')

class BfivenineSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bfivenine
		fields = ('id','description','add_info','link')

class BfivetenSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bfiveten
		fields = ('id','year','name_event','date_event','type_event','link')

class BfiveelevenSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bfiveeleven
		fields = ('id','description','add_info','link')

class BsixoneSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bsixone
		fields = ('id','description','add_info','link')

class BsixtwoSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bsixtwo
		fields = ('id','description','inst_docs','add_info','link')

class BsixthreeSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bsixthree
		fields = ('id','area','option','link')

class BsixfourSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bsixfour
		fields = ('id','description','add_info','link')

class BsixfiveSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bsixfive
		fields = ('id','date','title','name_teacher','amount_HEI','purpose')

class BsixsixSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bsixsix
		fields = ('id','year','name_faculty','type_prog','duration','start_end_date','name_inst')

class BsixsevenSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bsixseven
		fields = ('id','description','add_info','link')

class BsixeightSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bsixeight
		fields = ('id','year','name','purpose','funds_receive','link')

class BsixnineSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bsixnine
		fields = ('id','description','add_info','link')

class BsixtenSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bsixten
		fields = ('id','description','add_info','link')

class BsixelevenSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bsixeleven
		fields = ('id','description','add_info','link')

class BsixtwelveSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bsixtwelve
		fields = ('id','qual_insurance','option','link')

class BsevenoneSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bsevenone
		fields = ('id','description','add_info','link')

class BseventwoSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bseventwo
		fields = ('id','alt_source','option','link')

class BseventhreeSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bseventhree
		fields = ('id','description','add_info','link','photo')

class BsevenfourSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bsevenfour
		fields = ('id','facilities','option','link','photo')

class BsevenfiveSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bsevenfive
		fields = ('id','description','photo','report','policy_doc','link')

class BsevensixSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bsevensix
		fields = ('id','initiative','option','link')

class BsevensevenSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bsevenseven
		fields = ('id','description','add_info','link')

class BseveneightSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bseveneight
		fields = ('id','description','add_info','link')

class BsevennineSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bsevennine
		fields = ('id','description','details','link')

class BseventenSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bseventen
		fields = ('id','code_conduct','option','link')

class BsevenelevenSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bseveneleven
		fields = ('id','description')

class BseventwelveSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Bseventwelve
		fields = ('id','description','webpage_link','add_info')


class AoneoneSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Aoneone
		fields = ('id','intro')

class AoneoneSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Aoneone
		fields = ('id','intro')

class AonetwoSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Aonetwo
		fields = ('id','cir_aspects','evaluation','research','infra','student','govt','inst_values')

class AonethreeSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Aonethree
		fields = ('id','inst_strength','inst_weakness','inst_opp','inst_chall')

class AonefourSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Aonefour
		fields = ('id','add_info')

class AonefiveSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Aonefive
		fields = ('id','functioning')

class AtwooneSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Atwoone
		fields = ('id','name','address','city','state','pin','website')


class AtwotwoSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Atwotwo
		fields = ('id','desig','name','tele','mobile','fax','email')


class AtwothreeSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Atwothree
		fields = ('id','nature')

class AtwofourSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Atwofour
		fields = ('id','type')

class AtwofiveSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Atwofive
		fields = ('id','date_uni','status','date')

class AtwosixSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Atwosix
		fields = ('id','date_2F','date_12B','doc_2F','doc_12B')

class AtwosevenSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Atwoseven
		fields = ('id','UPE')

class AtwoeightSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Atwoeight
		fields = ('id','type','address','loc','area','built_area','prog','date_est','date_rec')

class AtwonineSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Atwonine
		fields = ('id','const','aff','clg_2F','clg_2F_12B','naac','ugc','auto','postgrd','clg_res','uni_res')

class AtwotenSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Atwoten
		fields = ('id','option','sra','doc')

class AtwoelevenSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Atwoeleven
		fields = ('id','prof_total_sanc','prof_rec_male','prof_rec_female','prof_rec_others','prof_rec_total','prof_rec_total_yet','prof_con_male','prof_con_female','prof_con_others','prof_con_total','assc_total_sanc','assc_rec_male','assc_rec_female','assc_rec_others','assc_rec_total','assc_rec_total_yet','assc_con_male','assc_con_female','assc_con_others','assc_con_total','assis_total_sanc','assis_rec_male','assis_rec_female','assis_rec_others','assis_rec_total','assis_rec_total_yet','assis_con_male','assis_con_female','assis_con_others','assis_con_total')

class AtwotwelveSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Atwotwelve
		fields = ('id','total_sanc_male','total_sanc_female','total_sanc_others','total_sanc_total','rec_male','rec_female','rec_others','rec_total','yet_rec_male','yet_rec_female','yet_rec_others','yet_rec_total','con_male','con_female','con_others','con_total')

class AtwothirteenSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Atwothirteen
		fields = ('id','total_sanc_male','total_sanc_female','total_sanc_others','total_sanc_total','rec_male','rec_female','rec_others','rec_total','yet_rec_male','yet_rec_female','yet_rec_others','yet_rec_total','con_male','con_female','con_others','con_total')

class AtwofourteenSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Atwofourteen
		fields = ('id','prof_highest_qual','prof_male','prof_female','prof_others','assc_highest_qual','assc_male','assc_female','assc_others','assis_highest_qual','assis_male','assis_female','assis_others')

class AtwofifteenSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Atwofifteen
		fields = ('id','prof_highest_qual','prof_male','prof_female','prof_others','assc_highest_qual','assc_male','assc_female','assc_others','assis_highest_qual','assis_male','assis_female','assis_others')

class AtwosixteenSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Atwosixteen
		fields = ('id','prof_highest_qual','prof_male','prof_female','prof_others','assc_highest_qual','assc_male','assc_female','assc_others','assis_highest_qual','assis_male','assis_female','assis_others')

class AtwoseventeenSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Atwoseventeen
		fields = ('id','emer_prof_male','emer_prof_female','emer_prof_others','emer_prof_total','adj_prof_male','adj_prof_female','adj_prof_others','adj_prof_total','vis_prof_male','vis_prof_female','vis_prof_others','vis_prof_total')

class AtwoeightteenSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Atwoeightteen
		fields = ('id','sl_no','name_dept','name_chair','name_org')

class AtwonineteenSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Atwonineteen
		fields = ('id','prog_name','own_state_male','own_state_female','own_state_others','other_states_male','other_states_female','other_states_others','NRI_stud_male','NRI_stud_female','NRI_stud_others','foreign_male','foreign_female','foreign_others','total_male','total_female','total_others')

class AtwotwentySerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Atwotwenty
		fields = ('id','ques','total')

class AtwotwentyoneSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Atwotwentyone
		fields = ('id','own_state_male','own_state_female','own_state_others','other_states_male','other_states_female','other_states_others','NRI_stud_male','NRI_stud_female','NRI_stud_others','foreign_male','foreign_female','foreign_others','total_male','total_female','total_others')

class AtwotwentytwoSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Atwotwentytwo
		fields = ('id','year','num_UGC_orien','num_UGC_refresher','num_uni_prog','total_num_prog')

class AtwotwentythreeSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Atwotwentythree
		fields = ('id','dept_name','report')

class AtwotwentyfourSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Atwotwentyfour
		fields = ('id','description')

class AtwotwentyfiveSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Atwotwentyfive
		fields = ('id','description')

class AthreeoneSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Athreeone
		fields = ('id','year','num_stud','description','inst_data')

class AthreetwoSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Athreetwo
		fields = ('id','year','num_stud','description','inst_data')


class AthreethreeSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Athreethree
		fields = ('id','year','num_teacher','description','inst_data')

class AthreefourSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Athreefour
		fields = ('id','total')

class AthreefiveSerializer(serializers.ModelSerializer):
# create a meta class
	class Meta:		
		model = Athreefive
		fields = ('id','year','total_exp')