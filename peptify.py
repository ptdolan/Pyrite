#peptify.py
#usage: python peptify.py <start> <end> <interval> <length> "allpeptides.txt"
import sys

outfile = sys.argv[3]

sequence="GAQVSSQKVGAHENSNRAYGGSTINYTTINYYRDSASNAASKQDFSQDPSKFTEPIKDVLIKTAPMLNSPNIEACGYSDRVLQLTLGNSTITTQEAANSVVAYGRWPEYLRDSEANPVDQPTEPDVAACRFYTLDTVSWTKESRGWWWKLPDALRDMGLFGQNMYYHYLGRSGYTVHVQCNASKFHQGALGVFAVPEMCLAGDSNTTTMHTSYQNANPGEKGGTFTGTFTPDNNQTSPARRFCPVDYLLGNGTLLGNAFVFPHQIINLRTNNCATLVLPYVNSLSIDSMVKHNNWGIAILPLAPLNFASESSPEIPITLTIAPMCCEFNGLRNITLPRLQGLPVMNTPGSNQYLTADNFQSPCALPEFDVTPPIDIPGEVKNMMELAEIDTMIPFDLSATKKNTMEMYRVRLSDKPHTDDPILCLSLSPASDPRLSHTMLGEILNYYTHWAGSLKFTFLFCGFMMATGKLLVSYAPPGADPPKKRKEAMLGTHVIWDIGLQSSCTMVVPWISNTTYRQTIDDSFTEGGYISVFYQTRIVVPLSTPREMDILGFVSACNDFSVRLLRDTTHIEQKALAQGLGQMLESMIDNTVRETVGAATSRDALPNTEASGPTHSKEIPALTAVETGATNPLVPSDTVQTRHVVQHRSRSESSIESFFARGACVTIMTVDNPASTTNKDKLFAVWKITYKDTVQLRRKLEFFTYSRFDMELTFVVTANFTETNNGHALNQVYQIMYVPPGAPVPEKWDDYTWQTSSNPSIFYTYGTAPARISVPYVGISNAYSHFYDGFSKVPLKDQSAALGDSLYGAASLNDFGILAVRVVNDHNPTKVTSKIRVYLKPKHIRVWCPRPPRAVAYYGPGVDYKDGTLTPLSTKDLTTY"

P1=['VP4','VP2','VP3','VP1']
resCoords=[[0,67],[68,339],[340,577],[578,879]]

INTERVAL=int(sys.argv[1])
PepLength = int(sys.argv[2])
print ("Prot. Length:", len(P1))
print ("Pept. Length:", PepLength)
print ("Overlap:", PepLength-INTERVAL)
counter=0
allpeptides=[]
allpositions=[]
proteins=[]
protPos=[]
for window in resCoords:
	print(P1[counter])
	print("Range:",window)
	length=(window[1]-window[0])
	print ("Selection Length:", length) 
	positions=range(window[0],window[1],INTERVAL)
	protPos.extend(range(0,window[1]-window[0],INTERVAL))
	allpositions.extend(positions)
	peptides=[sequence[res:res+PepLength] for res in positions]
	proteins.extend([P1[counter]]*(len(peptides)))
	allpeptides.extend(peptides)
	Npep=len(set(allpeptides))
	print(Npep)
	counter+=1
count=0
print(proteins)
with open(outfile,'w') as out:
	for line in allpeptides:
		print (line)
		out.write(proteins[count]+"\t"+str(count+1)+"\t"+str(protPos[count]+1)+"\t"+str(allpositions[count]+1)+"\t"+line+"\n")
		count+=1
		#print(count)

print ("Peptides:",len(allpeptides))
print ("Unique:  ",len(set(allpeptides)))