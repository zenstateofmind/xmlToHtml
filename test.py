#!/usr/bin/env python
# encoding: utf-8

import sys
import os
from urllib2 import urlopen	
from xml.dom import minidom
import urllib2 
import httplib 
import urllib
from xml.sax.handler import ContentHandler
import xml.sax


# from lxml import etree
# from lxml import objectify
# import lxml.usedoctest

print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<title>AppServer Info</title>'
print '	<link rel="stylesheet" href="http://dl.dropbox.com/u/1627245/style.css" type="text/css" media="screen" charset="utf-8" />'
print '<script src="http://dl.dropbox.com/u/1627245/jquery.js" type="text/javascript"></script>'
print '<script src="http://dl.dropbox.com/u/1627245/jquery.expander.js" type="text/javascript"></script>'
print '<script type="text/javascript"> $(document).ready(function() {$("tr td div.expandable").expander({ slicePoint:       80,  expandText:         "[Expand]", collapseTimer:    5000,  userCollapseText: "[Collapse]" }); }); </script>'
# print '<script> function showTable(tableid){ document.getElementById(tableid).style.visibility = "visible"; } function hideTable(tableid){ document.getElementById(tableid).style.visibility = "hidden"; } </script>'
# print '<script type="text/javascript">$("td span.expand").click(function() { $(this).parents("tr.main").nextUntil("tr.main").toggle(); }); </script><script  jQuery(".heading").click(function() { jQuery(this).next(".content").slideToggle(500); }); }); </script>'
print '<script type="text/javascript">$("td span.expand").click(function() { $(this).parents("tr.main").nextUntil("tr.main").toggle(); }); </script> <script type="text/javascript"> jQuery(document).ready(function() { jQuery(".content").hide(); jQuery(".heading").click(function() { jQuery(this).next(".content").slideToggle(500); }); }); </script>'
print '</head>'




class countHandler(ContentHandler):
    def __init__(self):
        self.tags={}

    def startElement(self, name, attr):
        if not self.tags.has_key(name):
            self.tags[name] = 0
        self.tags[name] += 1

# NumberOfMbeans = 'http://localhost:8080/JettyTrial/ws/mbeans/'
# xmlNoOfMbeans = minidom.parse(urllib2.urlopen(NumberOfMbeans))
# MbeansNumber = xmlNoOfMbeans.getElementsByTagName('MBean')
# NoOfNodesCounter = 0
# LegitNodes = 0
# for CountMbean in NumberOfMbeans:
# 	noUrl =  MbeansNumber[NoOfNodesCounter].getElementsByTagName("URL")[0].childNodes[0].nodeValue+'/attributes' #TAKE CARE OF SPECIAL CASE OF URLS ENDING WITH /
# 	print '</br>'+noUrl
# 	NoValidity = urllib.urlopen(noUrl)
# 	if(NoValidity.getcode() != 404 and NoValidity.getcode() != 500):
# 		LegitNodes = LegitNodes+1
# 	NoOfNodesCounter = NoOfNodesCounter + 1
# print 'number of nodes : '
# print NoOfNodesCounter

#####################################################################
# DrawTable('http://dl.dropbox.com/u/1627245/cd_catalog.xml')
################# TAKE CARE OF THE CASE WHEN THERE ARE NO MBEAN ATTRIBUTE NAMES BLA BLA BLA, THIS IS WHAT IS STOPPING THE SCRIPT HALF WAY	
#####################################################################

	
####TODO: ######
#1) Put the onload elements for all the tables in the body
#2) Check how you stick classes instead of ids
#3) Put everything together


##################
###########################################################################
count = 0
print '<body>'
# print '<p class="heading">Header-1 </p> <div class="content"><table border = 1><tr><td>hello</td><tr></table></div> <p class="heading">Header-2</p> <div class="content"><table border = 1><tr><td>hello</td><td>asdfasdf</td><tr></table></div></div> <p class="heading">Header-3</p> <div class="content">Lorem ipsum dolor sit amet, consectetuer adipiscing elit orem ipsum dolor sit amet, consectetuer adipiscing elit</div>'

MbeanUrl = 'http://localhost:8080/JettyTrial/ws/mbeans/'
xmlMbeanDoc = minidom.parse(urllib2.urlopen(MbeanUrl))
Mbeans = xmlMbeanDoc.getElementsByTagName('MBean')
# countCheck = 0
# counterCrapCheck = 0
# # print '<h2> hello </h2>'
# for checkMbean in Mbeans:
# 	urlCheck =  Mbeans[counterCrapCheck].getElementsByTagName("URL")[0].childNodes[0].nodeValue+'/attributes' #TAKE CARE OF SPECIAL CASE OF URLS ENDING WITH /
# 	ValidityCheck = urllib.urlopen(urlCheck)
# 	# print '</br>'+ValidityURL+'</br>'
# 	if(ValidityCheck.getcode() != 404 and ValidityCheck.getcode()!=500) :
# 		parserCheck = xml.sax.make_parser()
# 		handlerCheck = countHandler()
# 		parserCheck.setContentHandler(handlerCheck)
# 		parserCheck.parse(urlCheck)
# 		noXMLTagsCheck = len(handlerCheck.tags)
# 	
# 		if noXMLTagsCheck!=1:
# 			countCheck = countCheck+1
# 	counterCrapCheck = counterCrapCheck+1
# print 'counterCrapCheck + '
# print countCheck


legitstuff = 1

for Mbean in Mbeans:
		# print '</br>'+ Mbeans[count].getElementsByTagName("URL")[0].childNodes[0].nodeValue+'/attributes'+'</br>'
	url =  Mbeans[count].getElementsByTagName("URL")[0].childNodes[0].nodeValue+'/attributes' #TAKE CARE OF SPECIAL CASE OF URLS ENDING WITH /
	MbeanObjectName = Mbeans[count].getElementsByTagName("ObjectName")[0].childNodes[0].nodeValue# print '</br>' + ValidityURL 
	Validity = urllib.urlopen(url)
	# print '</br>'+ValidityURL+'</br>'
	if(Validity.getcode() != 404 and Validity.getcode()!=500) :
		
		
		###################################################
		parser = xml.sax.make_parser()
		handler = countHandler()
		parser.setContentHandler(handler)
		parser.parse(url)
		noXMLTags = len(handler.tags)
		# print '</br>' + 'the number of tags are '
		# 	print noXMLTags
		# 	print '</br>'
		########################################################
		print '<p class="heading"></br> MBean: '+MbeanObjectName
		print '<div class="content"><table id="box-table-a">'
		if(noXMLTags != 1):	
			

			xmlAttrDoc = minidom.parse(urllib2.urlopen(url))
			Attribute = xmlAttrDoc.getElementsByTagName('Attribute')
			nodeCount = 0
			nodesItrCounter = 0
			########################find the number of nodes in each attribute page####################
			firstAttribute = Attribute[0].getElementsByTagName('AttributeName')[0].childNodes[0].nodeValue
			for singleAttr in Attribute: 
				nextAttribute = Attribute[nodesItrCounter].getElementsByTagName('AttributeName')[0].childNodes[0].nodeValue
				nodesItrCounter = nodesItrCounter + 1
				if nextAttribute == firstAttribute:
					nodeCount = nodeCount + 1

			# print ' </br> the number of nodes are '
			# print nodeCount
			# 	print '</br>'
			##########################################################################################
			
			
			
			
			# print	'<table id="box-table-a" border = 1>'
			
			
			
			
			
			nodeBasedItr = 0
			print '</br><a href = "'+url+'" target="_blank">'+url+'</a>'
			# print '</br> count '
			# 			print legitstuff
			legitstuff = legitstuff + 1
			
			# print '<tr>'
			headerCounter = 0
			nodeHeaderCounter = Attribute[0].getElementsByTagName('NodeName')[0].childNodes[0].nodeValue
			print '<tr>'
			if(headerCounter == 0):
				print '<th scope = "col"> Node name </th>'
			for everyAttr in Attribute:
				nodeHeaderCurrent = Attribute[headerCounter].getElementsByTagName('NodeName')[0].childNodes[0].nodeValue
				if(nodeHeaderCurrent == nodeHeaderCounter ):
					AttrHeader = Attribute[headerCounter].getElementsByTagName('AttributeName')[0].childNodes[0].nodeValue
					print '<th scope="col">'+ AttrHeader+'</th>'
				headerCounter = headerCounter + 1
			print '</tr>'
			
			
			
			while nodeBasedItr < nodeCount:
				
				NodeCmpr = Attribute[nodeBasedItr].getElementsByTagName('NodeName')[0].childNodes[0].nodeValue
				# print '</br><b>NodeCmpr : '+NodeCmpr + '</b></br>'
				attrCount = 0
				print '<tr>'
				
				if attrCount == 0:
					print '<div class="expandable"><td>'+NodeCmpr+'</td></div>'
				# tableAdderCount = 0
				for indAttr in Attribute:
					# print '</br>tableAdderCount:'
					# 				print tableAdderCount 
					# 				print '</br>'
					currentNode = Attribute[attrCount].getElementsByTagName('NodeName')[0].childNodes[0].nodeValue
					if currentNode == NodeCmpr:
						AttributeName = Attribute[attrCount].getElementsByTagName("AttributeName")[0].childNodes[0].nodeValue
						CurrentObjectName = Attribute[attrCount].getElementsByTagName("ObjectName")[0].childNodes[0].nodeValue
						
						try:
							CurrentValue = Attribute[attrCount].getElementsByTagName("Value")[0].childNodes[0].nodeValue
						except IndexError:
							CurrentValue = 'N/A'
						print '<div class="expandable"><td> Object Name: '+CurrentObjectName+'</br></br></br> Value: '+CurrentValue+'</td></div>'
					attrCount = attrCount + 1
					# tableAdderCount = tableAdderCount +1
				print '</tr>'
				# print '</br>tableAdderCount:'
				# 			print tableAdderCount 
				# 			print '</br>'
				# 			print '</tr>'
				nodeBasedItr = nodeBasedItr + 1
	print '</table></div>'
			
	count = count + 1
	
# print '</br> '
# print count
print '</body>'
print '</html>'
