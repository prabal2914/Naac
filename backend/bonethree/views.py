from django.shortcuts import render

# import view sets from the REST framework
from rest_framework import viewsets

# import the TodoSerializer from the serializer file
from .serializers import BonethreeSerializer,BonetwoSerializer,BoneoneSerializer,BonefourSerializer,BonefiveSerializer,BonesixSerializer,BonesevenSerializer,BtwooneSerializer,BtwotwoSerializer,BtwothreeSerializer,BtwofourSerializer,BtwofiveSerializer,BtwosixSerializer,BtwosevenSerializer,BtwoeightSerializer,BtwonineSerializer,BtwotenSerializer,BthreethreetwoSerializer,BtwoelevenSerializer,BtwotwelveSerializer,BtwothirteenSerializer,BtwofourteenSerializer,BtwofifteenSerializer,BthreeeightSerializer,BthreeelevenSerializer,BthreefiveSerializer,BthreefourSerializer,BthreefourteenSerializer,BthreenineSerializer,BthreeoneSerializer,BthreesevenSerializer,BthreetenSerializer,BthreethirteenSerializer,BthreethreeSerializer,BthreetwelveSerializer,BthreetwoSerializer,BthreesixSerializer,BthreefifteenSerializer,BfouroneSerializer,BfourtwoSerializer,BfourthreeSerializer,BfourfourSerializer,BfourfiveSerializer,BfoursixSerializer,BfoursevenSerializer,BfiveeightSerializer,BfiveelevenSerializer,BfivefiveSerializer,BfivefourSerializer,BfivenineSerializer,BfiveoneSerializer,BfivesevenSerializer,BfivesixSerializer,BfivetenSerializer,BfivethreeSerializer,BfivetwoSerializer,BseventwoSerializer,BseveneightSerializer,BsevenelevenSerializer,BsevenfiveSerializer,BsevenfourSerializer,BsevennineSerializer,BsevenoneSerializer,BsevensixSerializer,BsevensevenSerializer,BseventenSerializer,BseventhreeSerializer,BseventwelveSerializer,BsixeightSerializer,BsixelevenSerializer,BsixfiveSerializer,BsixfourSerializer,BsixnineSerializer,BsixoneSerializer,BsixsevenSerializer,BsixsixSerializer,BsixtenSerializer,BsixthreeSerializer,BsixtwelveSerializer,BsixtwoSerializer,AonefiveSerializer,AonefourSerializer,AoneoneSerializer,AonethreeSerializer,AonetwoSerializer,AthreefiveSerializer,AthreefourSerializer,AthreeoneSerializer,AtwotwoSerializer,AthreethreeSerializer,AthreetwoSerializer,AtwoeightSerializer,AtwoeightteenSerializer,AtwoelevenSerializer,AtwofifteenSerializer,AtwofourSerializer,AtwofourteenSerializer,AtwonineSerializer,AtwonineteenSerializer,AtwofiveSerializer,AtwosixSerializer,AtwooneSerializer,AtwoseventeenSerializer,AtwosevenSerializer,AtwosixteenSerializer,AtwotenSerializer,AtwothirteenSerializer,AtwothreeSerializer,AtwotwelveSerializer,AtwotwentyfiveSerializer,AtwotwentyfourSerializer,AtwotwentyoneSerializer,AtwotwentySerializer,AtwotwentythreeSerializer,AtwotwentytwoSerializer

# import the Todo model from the models file
from .models import Bonethree,Bonetwo,Boneone,Bonefour,Bonefive,Bonesix,Bthreethreetwo,Boneseven,Btwoone,Btwotwo,Btwothree,Btwofour,Btwofive,Btwosix,Btwoseven,Btwoeight,Btwonine,Btwoten,Btwoeleven,Btwotwelve,Btwothirteen,Btwofourteen,Btwofifteen,Bthreefourteen,Bthreefour,Bthreeeight,Bthreeeleven,Bthreefive,Bthreenine,Bthreeone,Bthreeseven,Bthreesix,Bthreeten,Bthreethirteen,Bthreethree,Bthreetwelve,Bthreetwo,Bthreefifteen,Bfourseven,Bfourone,Bfourfive,Bfourfour,Bfoursix,Bfourthree,Bfourtwo,Bfivenine,Bfiveeight,Bfiveeleven,Bfivefive,Bfivefour,Bfiveone,Bfiveseven,Bfivesix,Bfiveten,Bfivethree,Bfivetwo,Bseventwelve,Bseveneight,Bseveneleven,Bsevenfive,Bsevenfour,Bsevennine,Bsevenone,Bsevenseven,Bsevensix,Bseventen,Bseventhree,Bseventwo,Bsixeight,Bsixeleven,Bsixfive,Bsixfour,Bsixnine,Bsixone,Bsixseven,Bsixsix,Bsixten,Bsixthree,Bsixtwelve,Bsixtwo,Athreethree,Atwotwentyfour,Aonefive,Aonefour,Aoneone,Aonethree,Aonetwo,Athreefive,Athreefour,Athreeone,Athreetwo,Atwoeight,Atwoeightteen,Atwoeleven,Atwofifteen,Atwofive,Atwofour,Atwofourteen,Atwonine,Atwonineteen,Atwoone,Atwoseven,Atwoseventeen,Atwosix,Atwosixteen,Atwoten,Atwothirteen,Atwothree,Atwotwelve,Atwotwenty,Atwotwentyfive,Atwotwentyone,Atwotwentythree,Atwotwentytwo,Atwotwo

# create a class for the Todo model viewsets
class BonethreeView(viewsets.ModelViewSet):


	# create a serializer class and
	# assign it to the TodoSerializer class
	serializer_class = BonethreeSerializer

	# define a variable and populate it
	# with the Todo list objects
	queryset = Bonethree.objects.all()

class BonetwoView(viewsets.ModelViewSet):
	serializer_class = BonetwoSerializer
	queryset = Bonetwo.objects.all()

class BoneoneView(viewsets.ModelViewSet):

	serializer_class = BoneoneSerializer

	queryset = Boneone.objects.all()

class BonefourView(viewsets.ModelViewSet):

	serializer_class = BonefourSerializer

	queryset = Bonefour.objects.all()


class BonefiveView(viewsets.ModelViewSet):

	serializer_class = BonefiveSerializer

	queryset = Bonefive.objects.all()

class BonesixView(viewsets.ModelViewSet):

	serializer_class = BonesixSerializer

	queryset = Bonesix.objects.all()	

class BonesevenView(viewsets.ModelViewSet):

	serializer_class = BonesevenSerializer

	queryset = Boneseven.objects.all()		

class BtwooneView(viewsets.ModelViewSet):

	serializer_class = BtwooneSerializer

	queryset = Btwoone.objects.all()	

class BtwotwoView(viewsets.ModelViewSet):

	serializer_class = BtwotwoSerializer

	queryset = Btwotwo.objects.all()			

class BtwothreeView(viewsets.ModelViewSet):

	serializer_class = BtwothreeSerializer

	queryset = Btwothree.objects.all()

class BtwofourView(viewsets.ModelViewSet):

	serializer_class = BtwofourSerializer

	queryset = Btwofour.objects.all()						

class BtwofiveView(viewsets.ModelViewSet):

	serializer_class = BtwofiveSerializer

	queryset = Btwofive.objects.all()	

class BtwosixView(viewsets.ModelViewSet):

	serializer_class = BtwosixSerializer

	queryset = Btwosix.objects.all()					

class BtwosevenView(viewsets.ModelViewSet):

	serializer_class = BtwosevenSerializer

	queryset = Btwoseven.objects.all()					

class BtwoeightView(viewsets.ModelViewSet):

	serializer_class = BtwoeightSerializer

	queryset = Btwoeight.objects.all()		

class BtwonineView(viewsets.ModelViewSet):

	serializer_class = BtwonineSerializer

	queryset = Btwonine.objects.all()		

class BtwotenView(viewsets.ModelViewSet):

	serializer_class = BtwotenSerializer

	queryset = Btwoten.objects.all()	

class BtwoelevenView(viewsets.ModelViewSet):

	serializer_class = BtwoelevenSerializer

	queryset = Btwoeleven.objects.all()		

class BtwotwelveView(viewsets.ModelViewSet):

	serializer_class = BtwotwelveSerializer

	queryset = Btwotwelve.objects.all()			

class BtwothirteenView(viewsets.ModelViewSet):

	serializer_class = BtwothirteenSerializer

	queryset = Btwothirteen.objects.all()			

class BtwofourteenView(viewsets.ModelViewSet):

	serializer_class = BtwofourteenSerializer

	queryset = Btwofourteen.objects.all()		

class BtwofifteenView(viewsets.ModelViewSet):

	serializer_class = BtwofifteenSerializer

	queryset = Btwofifteen.objects.all()			

class BthreeoneView(viewsets.ModelViewSet):

	serializer_class = BthreeoneSerializer

	queryset = Bthreeone.objects.all()		

class BthreetwoView(viewsets.ModelViewSet):

	serializer_class = BthreetwoSerializer

	queryset = Bthreetwo.objects.all()			

class BthreethreeView(viewsets.ModelViewSet):

	serializer_class = BthreethreeSerializer

	queryset = Bthreethree.objects.all()							

class BthreefourView(viewsets.ModelViewSet):

	serializer_class = BthreefourSerializer

	queryset = Bthreefour.objects.all()			

class BthreefiveView(viewsets.ModelViewSet):

	serializer_class = BthreefiveSerializer

	queryset = Bthreefive.objects.all()		

class BthreesixView(viewsets.ModelViewSet):

	serializer_class = BthreesixSerializer

	queryset = Bthreesix.objects.all()		

class BthreethreetwoView(viewsets.ModelViewSet):

	serializer_class = BthreethreetwoSerializer

	queryset = Bthreethreetwo.objects.all()

class BthreesevenView(viewsets.ModelViewSet):

	serializer_class = BthreesevenSerializer

	queryset = Bthreeseven.objects.all()			

class BthreeeightView(viewsets.ModelViewSet):

	serializer_class = BthreeeightSerializer

	queryset = Bthreeeight.objects.all()											

class BthreenineView(viewsets.ModelViewSet):

	serializer_class = BthreenineSerializer

	queryset = Bthreenine.objects.all()	

class BthreetenView(viewsets.ModelViewSet):

	serializer_class = BthreetenSerializer

	queryset = Bthreeten.objects.all()			

class BthreeelevenView(viewsets.ModelViewSet):

	serializer_class = BthreeelevenSerializer

	queryset = Bthreeeleven.objects.all()		

class BthreetwelveView(viewsets.ModelViewSet):

	serializer_class = BthreetwelveSerializer

	queryset = Bthreetwelve.objects.all()		

class BthreethirteenView(viewsets.ModelViewSet):

	serializer_class = BthreethirteenSerializer

	queryset = Bthreethirteen.objects.all()		

class BthreefourteenView(viewsets.ModelViewSet):

	serializer_class = BthreefourteenSerializer

	queryset = Bthreefourteen.objects.all()		

class BthreefifteenView(viewsets.ModelViewSet):

	serializer_class = BthreefifteenSerializer

	queryset = Bthreefifteen.objects.all()		

class BfouroneView(viewsets.ModelViewSet):

	serializer_class = BfouroneSerializer

	queryset = Bfourone.objects.all()	

class BfourtwoView(viewsets.ModelViewSet):

	serializer_class = BfourtwoSerializer

	queryset = Bfourtwo.objects.all()	

class BfourthreeView(viewsets.ModelViewSet):

	serializer_class = BfourthreeSerializer

	queryset = Bfourthree.objects.all()	

class BfourfourView(viewsets.ModelViewSet):

	serializer_class = BfourfourSerializer

	queryset = Bfourfour.objects.all()	

class BfourfiveView(viewsets.ModelViewSet):

	serializer_class = BfourfiveSerializer

	queryset = Bfourfive.objects.all()	

class BfoursixView(viewsets.ModelViewSet):

	serializer_class = BfoursixSerializer

	queryset = Bfoursix.objects.all()	


class BfoursevenView(viewsets.ModelViewSet):

	serializer_class = BfoursevenSerializer

	queryset = Bfourseven.objects.all()	


class BfiveoneView(viewsets.ModelViewSet):

	serializer_class = BfiveoneSerializer

	queryset = Bfiveone.objects.all()	

class BfivetwoView(viewsets.ModelViewSet):

	serializer_class = BfivetwoSerializer

	queryset = Bfivetwo.objects.all()	

class BfivethreeView(viewsets.ModelViewSet):

	serializer_class = BfivethreeSerializer

	queryset = Bfivethree.objects.all()	

class BfivefourView(viewsets.ModelViewSet):

	serializer_class = BfivefourSerializer

	queryset = Bfivefour.objects.all()	

class BfivefiveView(viewsets.ModelViewSet):

	serializer_class = BfivefiveSerializer

	queryset = Bfivefive.objects.all()	

class BfivesixView(viewsets.ModelViewSet):

	serializer_class = BfivesixSerializer

	queryset = Bfivesix.objects.all()	


class BfivesevenView(viewsets.ModelViewSet):

	serializer_class = BfivesevenSerializer

	queryset = Bfiveseven.objects.all()	

class BfiveeightView(viewsets.ModelViewSet):

	serializer_class = BfiveeightSerializer

	queryset = Bfiveeight.objects.all()	

class BfivenineView(viewsets.ModelViewSet):

	serializer_class = BfivenineSerializer

	queryset = Bfivenine.objects.all()	

class BfivetenView(viewsets.ModelViewSet):

	serializer_class = BfivetenSerializer

	queryset = Bfiveten.objects.all()	

class BfiveelevenView(viewsets.ModelViewSet):

	serializer_class = BfiveelevenSerializer

	queryset = Bfiveeleven.objects.all()	

class BsixoneView(viewsets.ModelViewSet):

	serializer_class = BsixoneSerializer

	queryset = Bsixone.objects.all()	


class BsixtwoView(viewsets.ModelViewSet):

	serializer_class = BsixtwoSerializer

	queryset = Bsixtwo.objects.all()	


class BsixthreeView(viewsets.ModelViewSet):

	serializer_class = BsixthreeSerializer

	queryset = Bsixthree.objects.all()	

class BsixfourView(viewsets.ModelViewSet):

	serializer_class = BsixfourSerializer

	queryset = Bsixfour.objects.all()	

class BsixfiveView(viewsets.ModelViewSet):

	serializer_class = BsixfiveSerializer

	queryset = Bsixfive.objects.all()	


class BsixsixView(viewsets.ModelViewSet):

	serializer_class = BsixsixSerializer

	queryset = Bsixsix.objects.all()	



class BsixsevenView(viewsets.ModelViewSet):

	serializer_class = BsixsevenSerializer

	queryset = Bsixseven.objects.all()	

class BsixeightView(viewsets.ModelViewSet):

	serializer_class = BsixeightSerializer

	queryset = Bsixeight.objects.all()	

class BsixnineView(viewsets.ModelViewSet):

	serializer_class = BsixnineSerializer

	queryset = Bsixnine.objects.all()	

class BsixtenView(viewsets.ModelViewSet):

	serializer_class = BsixtenSerializer

	queryset = Bsixten.objects.all()	

class BsixelevenView(viewsets.ModelViewSet):

	serializer_class = BsixelevenSerializer

	queryset = Bsixeleven.objects.all()	

class BsixtwelveView(viewsets.ModelViewSet):

	serializer_class = BsixtwelveSerializer

	queryset = Bsixtwelve.objects.all()	

class BsevenoneView(viewsets.ModelViewSet):

	serializer_class = BsevenoneSerializer

	queryset = Bsevenone.objects.all()	

class BseventwoView(viewsets.ModelViewSet):

	serializer_class = BseventwoSerializer

	queryset = Bseventwo.objects.all()	

class BseventhreeView(viewsets.ModelViewSet):

	serializer_class = BseventhreeSerializer

	queryset = Bseventhree.objects.all()	

class BsevenfourView(viewsets.ModelViewSet):

	serializer_class = BsevenfourSerializer

	queryset = Bsevenfour.objects.all()	

class BsevenfiveView(viewsets.ModelViewSet):

	serializer_class = BsevenfiveSerializer

	queryset = Bsevenfive.objects.all()	

class BsevensixView(viewsets.ModelViewSet):

	serializer_class = BsevensixSerializer

	queryset = Bsevensix.objects.all()	

class BsevensevenView(viewsets.ModelViewSet):

	serializer_class = BsevensevenSerializer

	queryset = Bsevenseven.objects.all()	

class BseveneightView(viewsets.ModelViewSet):

	serializer_class = BseveneightSerializer

	queryset = Bseveneight.objects.all()	

class BsevennineView(viewsets.ModelViewSet):

	serializer_class = BsevennineSerializer

	queryset = Bsevennine.objects.all()	

class BseventwoView(viewsets.ModelViewSet):

	serializer_class = BseventwoSerializer

	queryset = Bseventwo.objects.all()	

class BseventhreeView(viewsets.ModelViewSet):

	serializer_class = BseventhreeSerializer

	queryset = Bseventhree.objects.all()	

class BsevenfourView(viewsets.ModelViewSet):

	serializer_class = BsevenfourSerializer

	queryset = Bsevenfour.objects.all()	

class BsevenfiveView(viewsets.ModelViewSet):

	serializer_class = BsevenfiveSerializer

	queryset = Bsevenfive.objects.all()	

class BsevensixView(viewsets.ModelViewSet):

	serializer_class = BsevensixSerializer

	queryset = Bsevensix.objects.all()	

class BsevensevenView(viewsets.ModelViewSet):

	serializer_class = BsevensevenSerializer

	queryset = Bsevenseven.objects.all()	

class BseveneightView(viewsets.ModelViewSet):

	serializer_class = BseveneightSerializer

	queryset = Bseveneight.objects.all()	

class BsevennineView(viewsets.ModelViewSet):

	serializer_class = BsevennineSerializer

	queryset = Bsevennine.objects.all()	

class BseventenView(viewsets.ModelViewSet):

	serializer_class = BseventenSerializer

	queryset = Bseventen.objects.all()	

class BsevenelevenView(viewsets.ModelViewSet):

	serializer_class = BsevenelevenSerializer

	queryset = Bseveneleven.objects.all()	

class BseventwelveView(viewsets.ModelViewSet):

	serializer_class = BseventwelveSerializer

	queryset = Bseventwelve.objects.all()	


class AoneoneView(viewsets.ModelViewSet):

	serializer_class = AoneoneSerializer

	queryset = Aoneone.objects.all()	

class AonetwoView(viewsets.ModelViewSet):

	serializer_class = AonetwoSerializer

	queryset = Aonetwo.objects.all()	

class AonethreeView(viewsets.ModelViewSet):

	serializer_class = AonethreeSerializer

	queryset = Aonethree.objects.all()	

class AonefourView(viewsets.ModelViewSet):

	serializer_class = AonefourSerializer

	queryset = Aonefour.objects.all()	

class AonefiveView(viewsets.ModelViewSet):

	serializer_class = AonefiveSerializer

	queryset = Aonefive.objects.all()	

class AtwooneView(viewsets.ModelViewSet):

	serializer_class = AtwooneSerializer

	queryset = Atwoone.objects.all()	

class AtwotwoView(viewsets.ModelViewSet):

	serializer_class = AtwotwoSerializer

	queryset = Atwotwo.objects.all()	

class AtwothreeView(viewsets.ModelViewSet):

	serializer_class = AtwothreeSerializer

	queryset = Atwothree.objects.all()

class AtwofourView(viewsets.ModelViewSet):

	serializer_class = AtwofourSerializer

	queryset = Atwofour.objects.all()

class AtwofiveView(viewsets.ModelViewSet):

	serializer_class = AtwofiveSerializer

	queryset = Atwofive.objects.all()

class AtwosixView(viewsets.ModelViewSet):

	serializer_class = AtwosixSerializer

	queryset = Atwosix.objects.all()

class AtwosevenView(viewsets.ModelViewSet):

	serializer_class = AtwosevenSerializer

	queryset = Atwoseven.objects.all()

class AtwoeightView(viewsets.ModelViewSet):

	serializer_class = AtwoeightSerializer

	queryset = Atwoeight.objects.all()

class AtwonineView(viewsets.ModelViewSet):

	serializer_class = AtwonineSerializer

	queryset = Atwonine.objects.all()

class AtwotenView(viewsets.ModelViewSet):

	serializer_class = AtwotenSerializer

	queryset = Atwoten.objects.all()

class AtwoelevenView(viewsets.ModelViewSet):

	serializer_class = AtwoelevenSerializer

	queryset = Atwoeleven.objects.all()

class AtwotwelveView(viewsets.ModelViewSet):

	serializer_class = AtwotwelveSerializer

	queryset = Atwotwelve.objects.all()

class AtwothirteenView(viewsets.ModelViewSet):

	serializer_class = AtwothirteenSerializer

	queryset = Atwothirteen.objects.all()

class AtwofourteenView(viewsets.ModelViewSet):

	serializer_class = AtwofourteenSerializer

	queryset = Atwofourteen.objects.all()

class AtwofifteenView(viewsets.ModelViewSet):

	serializer_class = AtwofifteenSerializer

	queryset = Atwofifteen.objects.all()

class AtwosixteenView(viewsets.ModelViewSet):

	serializer_class = AtwosixteenSerializer

	queryset = Atwosixteen.objects.all()

class AtwoseventeenView(viewsets.ModelViewSet):

	serializer_class = AtwoseventeenSerializer

	queryset = Atwoseventeen.objects.all()

class AtwoeightteenView(viewsets.ModelViewSet):

	serializer_class = AtwoeightteenSerializer

	queryset = Atwoeightteen.objects.all()

class AtwonineteenView(viewsets.ModelViewSet):

	serializer_class = AtwonineteenSerializer

	queryset = Atwonineteen.objects.all()

class AtwotwentyView(viewsets.ModelViewSet):

	serializer_class = AtwotwentySerializer

	queryset = Atwotwenty.objects.all()

class AtwotwentyoneView(viewsets.ModelViewSet):

	serializer_class = AtwotwentyoneSerializer

	queryset = Atwotwentyone.objects.all()

class AtwotwentytwoView(viewsets.ModelViewSet):

	serializer_class = AtwotwentytwoSerializer

	queryset = Atwotwentytwo.objects.all()

class AtwotwentythreeView(viewsets.ModelViewSet):

	serializer_class = AtwotwentythreeSerializer

	queryset = Atwotwentythree.objects.all()

class AtwotwentyfourView(viewsets.ModelViewSet):

	serializer_class = AtwotwentyfourSerializer

	queryset = Atwotwentyfour.objects.all()

class AtwotwentyfiveView(viewsets.ModelViewSet):

	serializer_class = AtwotwentyfiveSerializer

	queryset = Atwotwentyfive.objects.all()

class AthreeoneView(viewsets.ModelViewSet):

	serializer_class = AthreeoneSerializer

	queryset = Athreeone.objects.all()

class AthreetwoView(viewsets.ModelViewSet):

	serializer_class = AthreetwoSerializer

	queryset = Athreetwo.objects.all()

class AthreethreeView(viewsets.ModelViewSet):

	serializer_class = AthreethreeSerializer

	queryset = Athreethree.objects.all()

class AthreefourView(viewsets.ModelViewSet):

	serializer_class = AthreefourSerializer

	queryset = Athreefour.objects.all()

class AthreefiveView(viewsets.ModelViewSet):

	serializer_class = AthreefiveSerializer

	queryset = Athreefive.objects.all()


