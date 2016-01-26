import sendgrid
import json
import requests
import datetime


def send_mail(API_KEY,github_stats):
	
	html = '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"> <html xmlns="http://www.w3.org/1999/xhtml" data-dnd="true"> <head> <meta http-equiv="Content-Type" content="text/html; charset=utf-8" /> <meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1" /> <!--[if !mso]><!--> <meta http-equiv="X-UA-Compatible" content="IE=Edge" /> <!--<![endif]--> <!--[if (gte mso 9)|(IE)]><style type="text/css"> table {{border-collapse: collapse;}} table, td {{mso-table-lspace: 0pt;mso-table-rspace: 0pt;}} img {{-ms-interpolation-mode: bicubic;}} </style> <![endif]--> <style type="text/css"> body {{color: #626262; }} body a {{color: #0088cd; text-decoration: none; }} p {{ margin: 0; padding: 0; }} table[class="wrapper"] {{width:100% !important; table-layout: fixed; -webkit-font-smoothing: antialiased; -webkit-text-size-adjust: 100%; -moz-text-size-adjust: 100%; -ms-text-size-adjust: 100%; }} img[class="max-width"] {{max-width: 100% !important; }} @media screen and (max-width:480px) {{.preheader .rightColumnContent, .footer .rightColumnContent {{text-align: left !important; }} .preheader .rightColumnContent div, .preheader .rightColumnContent span, .footer .rightColumnContent div, .footer .rightColumnContent span {{text-align: left !important; }} .preheader .rightColumnContent, .preheader .leftColumnContent {{font-size: 80% !important; padding: 5px 0; }} table[class="wrapper-mobile"] {{width: 100% !important; table-layout: fixed; }} img[class="max-width"] {{height: auto !important; }} a[class="bulletproof-button"] {{display: block !important; width: auto !important; font-size: 80%; padding-left: 0 !important; padding-right: 0 !important; }} // 2 columns #templateColumns{{width:100% !important; }} .templateColumnContainer{{display:block !important; width:100% !important; padding-left: 0 !important; padding-right: 0 !important; }} }} </style> <style> body, p, div {{ font-family: helvetica,arial,sans-serif; }} </style> <style> body, p, div {{ font-size: 18px; }} </style> </head> <body yahoofix="true" style="min-width: 100%; margin: 0; padding: 0; font-size: 18px; font-family: helvetica,arial,sans-serif; color: #626262; background-color: #F4F4F4; color: #626262;" data-attributes="%7B%22dropped%22%3Atrue%2C%22bodybackground%22%3A%22%23F4F4F4%22%2C%22bodyfontname%22%3A%22helvetica%2Carial%2Csans-serif%22%2C%22bodytextcolor%22%3A%22%23626262%22%2C%22bodylinkcolor%22%3A%22%230088cd%22%2C%22bodyfontsize%22%3A18%7D"> <center class="wrapper"> <div class="webkit"> <table cellpadding="0" cellspacing="0" border="0" width="100%" class="wrapper" bgcolor="#F4F4F4"> <tr><td valign="top" bgcolor="#F4F4F4" width="100%"> <!--[if (gte mso 9)|(IE)]> <table width="600" align="center" cellpadding="0" cellspacing="0" border="0"> <tr> <td> <![endif]--> <table width="100%" role="content-container" class="outer" data-attributes="%7B%22dropped%22%3Atrue%2C%22containerpadding%22%3A%220%2C0%2C0%2C0%22%2C%22containerwidth%22%3A600%2C%22containerbackground%22%3A%22%23F4F4F4%22%7D" align="center" cellpadding="0" cellspacing="0" border="0"> <tr> <td width="100%"><table width="100%" cellpadding="0" cellspacing="0" border="0"> <tr> <td> <!--[if (gte mso 9)|(IE)]> <table width="600" align="center" cellpadding="0" cellspacing="0" border="0"> <tr> <td> <![endif]--> <table width="100%" cellpadding="0" cellspacing="0" border="0" style="width: 100%; max-width:600px;" align="center"> <tr><td role="modules-container" style="padding: 0px 0px 0px 0px; color: #626262; text-align: left;" bgcolor="#F4F4F4" width="100%" align="left"> <table border="0" cellpadding="0" cellspacing="0" align="center" width="100%" style="" class="module preheader " role="module" data-type="preheader" data-attributes="%7B%22dropped%22%3Atrue%2C%22hide%22%3Afalse%2C%22columns%22%3A2%2C%22padding%22%3A%2223%2C5%2C5%2C5%22%2C%22containerbackground%22%3A%22%23F4F4F4%22%7D"> <tr><td style="padding: 23px 5px 5px 5px;" bgcolor="#F4F4F4"> <table border="0" cellpadding="0" cellspacing="0" align="center" width="100%"> <tr role="module-content"> <td align="center" valign="top" width="50%" height="100%" class="templateColumnContainer"> <table border="0" cellpadding="0" cellspacing="0" width="100%" height="100%"> <tr> <td class="leftColumnContent" role="column-one" height="100%" style="height:100%;"><table class="module" role="module" data-type="text" border="0" cellpadding="0" cellspacing="0"  width="100%" style="table-layout: fixed;" data-attributes="%7B%22dropped%22%3Atrue%2C%22child%22%3Afalse%2C%22padding%22%3A%220%2C0%2C0%2C0%22%2C%22containerbackground%22%3A%22%22%7D"> <tr> <td role="module-content"  valign="top" height="100%" style="padding: 0px 0px 0px 0px;" bgcolor=""> </td> </tr> </table> </td> </tr> </table> </td> <td align="center" valign="top" width="50%" height="100%" class="templateColumnContainer"> <table border="0" cellpadding="0" cellspacing="0" width="100%" height="100%"> <tr> <td class="rightColumnContent" role="column-two" height="100%" style="height:100%;"><table class="module" role="module" data-type="text" border="0" cellpadding="0" cellspacing="0"  width="100%" style="table-layout: fixed;" data-attributes="%7B%22dropped%22%3Atrue%2C%22child%22%3Afalse%2C%22padding%22%3A%220%2C0%2C0%2C0%22%2C%22containerbackground%22%3A%22%22%7D"> <tr> <td role="module-content"  valign="top" height="100%" style="padding: 0px 0px 0px 0px;" bgcolor=""> </td> </tr> </table> </td> </tr> </table> </td> </tr> </table> </td></tr> </table> <table class="module" role="module" data-type="text" border="0" cellpadding="0" cellspacing="0"  width="100%" style="table-layout: fixed;" data-attributes="%7B%22dropped%22%3Atrue%2C%22child%22%3Afalse%2C%22padding%22%3A%220%2C0%2C0%2C0%22%2C%22containerbackground%22%3A%22%23ffffff%22%7D"> <tr> <td role="module-content"  valign="top" height="100%" style="padding: 0px 0px 0px 0px;" bgcolor="#ffffff"> <p style="text-align: center;"><span style="font-size:11px;"><span style="color: rgb(98, 98, 98); font-family: helvetica, arial, sans-serif; line-height: 14.2857px; text-align: center; background-color: rgb(255, 255, 255);">[The&nbsp;EPoD Analytics Team]</span></span></p> <h1 style="text-align: center;"><span style="color:#000000;"><span style="font-size:72px;">epod.</span></span><span style="color:#FF0000;"><span style="font-size:72px;">io</span></span></h1> </td> </tr> </table> <table role="module" data-type="image" border="0" align="center" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" class="wrapper" data-attributes="%7B%22child%22%3Afalse%2C%22link%22%3A%22%22%2C%22width%22%3A%22176%22%2C%22height%22%3A%22176%22%2C%22imagebackground%22%3A%22%23FFFFFF%22%2C%22url%22%3A%22https%3A//marketing-image-production.s3.amazonaws.com/uploads/e4dc7086d7040a339df5d05752fef1f5d877d1644b6bf8d12f5a80ffdb06f0932739bf46e17df67645b353ff9aa35dfa5863de166f987d462d1f9379f7c756d6.png%22%2C%22alt_text%22%3A%22%22%2C%22dropped%22%3Atrue%2C%22imagemargin%22%3A%220%2C0%2C0%2C0%22%2C%22alignment%22%3A%22center%22%2C%22responsive%22%3Afalse%7D"> <tr> <td style="font-size:6px;line-height:10px;background-color:#FFFFFF;padding: 0px 0px 0px 0px;" valign="top" align="center" role="module-content"> <img class="max-width"  width="176"   height="176"  src="https://marketing-image-production.s3.amazonaws.com/uploads/e4dc7086d7040a339df5d05752fef1f5d877d1644b6bf8d12f5a80ffdb06f0932739bf46e17df67645b353ff9aa35dfa5863de166f987d462d1f9379f7c756d6.png" alt="" border="0" style="display: block; color: #000; text-decoration: none; font-family: Helvetica, arial, sans-serif; font-size: 16px; " /> </td> </tr> </table><table class="module" role="module" data-type="spacer" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-attributes="%7B%22dropped%22%3Atrue%2C%22spacing%22%3A15%2C%22containerbackground%22%3A%22%23ffffff%22%7D"> <tr><td role="module-content" style="padding: 0px 0px 15px 0px;" bgcolor="#ffffff"></td></tr></table> <table border="0" cellpadding="0" cellspacing="0" align="center" width="100%" role="module" data-type="columns" data-attributes="%7B%22dropped%22%3Atrue%2C%22columns%22%3A2%2C%22padding%22%3A%220%2C0%2C0%2C0%22%2C%22cellpadding%22%3A0%2C%22containerbackground%22%3A%22%22%7D"> <tr><td style="padding: 0px 0px 0px 0px;" bgcolor=""> <table class="columns--container-table" border="0" cellpadding="0" cellspacing="0" align="center" width="100%"> <tr role="module-content"> <td style="padding: 0px 0px 0px 0px" role="column-0" align="center" valign="top" width="50%" height="100%" class="templateColumnContainer column-drop-area "> <table class="module" role="module" data-type="text" border="0" cellpadding="0" cellspacing="0"  width="100%" style="table-layout: fixed;" data-attributes="%7B%22dropped%22%3Atrue%2C%22child%22%3Afalse%2C%22padding%22%3A%220%2C0%2C0%2C0%22%2C%22containerbackground%22%3A%22%23ffffff%22%7D"> <tr> <td role="module-content"  valign="top" height="100%" style="padding: 0px 0px 0px 0px;" bgcolor="#ffffff"> <h3 style="text-align: center;">The Akbar "Akhbar"</h3> </td> </tr> </table> </td><td style="padding: 0px 0px 0px 0px" role="column-1" align="center" valign="top" width="50%" height="100%" class="templateColumnContainer column-drop-area "> <table class="module" role="module" data-type="text" border="0" cellpadding="0" cellspacing="0"  width="100%" style="table-layout: fixed;" data-attributes="%7B%22dropped%22%3Atrue%2C%22child%22%3Afalse%2C%22padding%22%3A%220%2C0%2C0%2C0%22%2C%22containerbackground%22%3A%22%23ffffff%22%7D"> <tr> <td role="module-content"  valign="top" height="100%" style="padding: 0px 0px 0px 0px;" bgcolor="#ffffff"> <h3 style="text-align: center;">January 2016 Update</h3> </td> </tr> </table> </td> </tr> </table> </td></tr> </table><table class="module" role="module" data-type="spacer" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-attributes="%7B%22dropped%22%3Atrue%2C%22spacing%22%3A20%2C%22containerbackground%22%3A%22%23FFFFFF%22%7D"> <tr><td role="module-content" style="padding: 0px 0px 20px 0px;" bgcolor="#FFFFFF"></td></tr></table> <table class="module" role="module" data-type="spacer" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-attributes="%7B%22dropped%22%3Atrue%2C%22spacing%22%3A10%2C%22containerbackground%22%3A%22%23f6f6f6%22%7D"> <tr><td role="module-content" style="padding: 0px 0px 10px 0px;" bgcolor="#f6f6f6"></td></tr></table> <table class="module" role="module" data-type="text" border="0" cellpadding="0" cellspacing="0"  width="100%" style="table-layout: fixed;" data-attributes="%7B%22dropped%22%3Atrue%2C%22child%22%3Afalse%2C%22padding%22%3A%2215%2C23%2C34%2C23%22%2C%22containerbackground%22%3A%22%23ffffff%22%7D"> <tr> <td role="module-content"  valign="top" height="100%" style="padding: 15px 23px 34px 23px;" bgcolor="#ffffff"> <h1 style="text-align: center;"><span style="color:#2D2D2D;">What we&#39;ve been coding this month</span></h1> <h3 style="text-align: center;">Lines of code committed on GitHub in January</h3> <div style="text-align: center;"> <table align="center" border="0" cellpadding="1" cellspacing="1" style="width:500px;"> <tbody> \
		<tr> <td>Payment Delay Dashboard (Paydash)</td> <td>+{PAYDASH_A} / -{PAYDASH_D}</td> </tr> \
		<tr> <td>Payment Delay Data Pulls (Paydata)</td> <td>+{PAYDATA_A} / -{PAYDATA_D}</td> </tr> \
		<tr> <td>HRDF</td> <td><span style="color: rgb(98, 98, 98); font-family: helvetica, arial, sans-serif; text-align: center; background-color: rgb(255, 255, 255);">+{HRDF_A} / -{HRDF_D}</span></td> </tr> \
		<tr> <td>MGNREGA BCURE Case</td> <td><span style="color: rgb(98, 98, 98); font-family: helvetica, arial, sans-serif; text-align: center; background-color: rgb(255, 255, 255);">+{MNREGACASE_A} / -{MNREGACASE_D}</span></td> </tr> </tbody> </table> <div>&nbsp;</div> <h3>Lines of code by team member</h3> <div> <table align="center" border="0" cellpadding="1" cellspacing="1" style="width:300px;"> <tbody> \
		<tr> <td>Angela</td> <td><span style="color: rgb(98, 98, 98); font-family: helvetica, arial, sans-serif; text-align: center; background-color: rgb(255, 255, 255);">+{ANGELA_A} / -{ANGELA_D}</span></td> </tr> \
		<tr> <td>Eric</td> <td><span style="color: rgb(98, 98, 98); font-family: helvetica, arial, sans-serif; text-align: center; background-color: rgb(255, 255, 255);">+{ERIC_A} / -{ERIC_D}</span></td> </tr> \
		<tr> <td>Ravi</td> <td><span style="color: rgb(98, 98, 98); font-family: helvetica, arial, sans-serif; text-align: center; background-color: rgb(255, 255, 255);">+{RAVI_A} / -{RAVI_D}</span></td> </tr> \
		<tr> <td>Sarah</td> <td><span style="color: rgb(98, 98, 98); font-family: helvetica, arial, sans-serif; text-align: center; background-color: rgb(255, 255, 255);">+{SARAH_A} / -{SARAH_D}</span></td> </tr> </tbody> </table> </div> </div> </td> </tr> </table> <table class="module" role="module" data-type="spacer" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-attributes="%7B%22dropped%22%3Atrue%2C%22spacing%22%3A10%2C%22containerbackground%22%3A%22%23f6f6f6%22%7D"> <tr><td role="module-content" style="padding: 0px 0px 10px 0px;" bgcolor="#f6f6f6"></td></tr></table> <table class="module" role="module" data-type="text" border="0" cellpadding="0" cellspacing="0"  width="100%" style="table-layout: fixed;" data-attributes="%7B%22dropped%22%3Atrue%2C%22child%22%3Afalse%2C%22padding%22%3A%2215%2C23%2C34%2C23%22%2C%22containerbackground%22%3A%22%23ffffff%22%7D"> <tr> <td role="module-content"  valign="top" height="100%" style="padding: 15px 23px 34px 23px;" bgcolor="#ffffff"> <h1 style="text-align: center;"><span style="color:#2D2D2D;">Research Project Updates</span></h1> <h2 style="text-align: center;">Payment Delays</h2> <div style="text-align: center;"> <div style="color: rgb(98, 98, 98); font-family: helvetica, arial, sans-serif; text-align: center; background-color: rgb(255, 255, 255);">Lorem ipsum dolor sit amet, vix facer virtute conceptam ne. Te qui consul graeco imperdiet, omnes pertinax torquatos eu quo, nam et summo admodum sensibus.</div> <div style="color: rgb(98, 98, 98); font-family: helvetica, arial, sans-serif; text-align: center; background-color: rgb(255, 255, 255);">Et veri ludus petentium eam. Mandamus erroribus ei has, cu his illud veniam.</div> <div style="color: rgb(98, 98, 98); font-family: helvetica, arial, sans-serif; text-align: center; background-color: rgb(255, 255, 255);"> <h2 style="color: rgb(98, 98, 98); text-align: center; background-color: rgb(255, 255, 255);">Bihar Report Cards</h2> <div style="color: rgb(98, 98, 98); font-family: helvetica, arial, sans-serif; text-align: center; background-color: rgb(255, 255, 255);"> <div>Lorem ipsum dolor sit amet, vix facer virtute conceptam ne. Te qui consul graeco imperdiet, omnes pertinax torquatos eu quo, nam et summo admodum sensibus.</div> <div>Et veri ludus petentium eam. Mandamus erroribus ei has, cu his illud veniam.</div> <div> <h2 style="color: rgb(98, 98, 98); text-align: center; background-color: rgb(255, 255, 255);">Statistan / Moodistan</h2> <div style="color: rgb(98, 98, 98); font-family: helvetica, arial, sans-serif; text-align: center; background-color: rgb(255, 255, 255);"> <div>Lorem ipsum dolor sit amet, vix facer virtute conceptam ne. Te qui consul graeco imperdiet, omnes pertinax torquatos eu quo, nam et summo admodum sensibus.</div> <div>Et veri ludus petentium eam. Mandamus erroribus ei has, cu his illud veniam.</div> </div> </div> </div> </div> </div> </td> </tr> </table> <table class="module" role="module" data-type="spacer" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-attributes="%7B%22dropped%22%3Atrue%2C%22spacing%22%3A10%2C%22containerbackground%22%3A%22%23f6f6f6%22%7D"> <tr><td role="module-content" style="padding: 0px 0px 10px 0px;" bgcolor="#f6f6f6"></td></tr></table> <table role="module" data-type="image" border="0" align="center" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" class="wrapper" data-attributes="%7B%22child%22%3Afalse%2C%22link%22%3A%22%22%2C%22width%22%3A%22600%22%2C%22height%22%3A%22400%22%2C%22imagebackground%22%3A%22%23f6f6f6%22%2C%22url%22%3A%22http%3A//static.sendgrid.com.s3.amazonaws.com/emails/internal/Bloco/featuredimage.jpg%22%2C%22alt_text%22%3A%22%22%2C%22dropped%22%3Atrue%2C%22imagemargin%22%3A%220%2C0%2C0%2C0%22%2C%22alignment%22%3A%22%22%2C%22responsive%22%3Afalse%7D"> <tr> <td style="font-size:6px;line-height:10px;background-color:#f6f6f6;padding: 0px 0px 0px 0px;" valign="top" align="" role="module-content"> <img class="max-width"  width="600"   height="400"  src="http://static.sendgrid.com.s3.amazonaws.com/emails/internal/Bloco/featuredimage.jpg" alt="" border="0" style="display: block; color: #000; text-decoration: none; font-family: Helvetica, arial, sans-serif; font-size: 16px; " /> </td> </tr> </table><table class="module" role="module" data-type="text" border="0" cellpadding="0" cellspacing="0"  width="100%" style="table-layout: fixed;" data-attributes="%7B%22dropped%22%3Atrue%2C%22child%22%3Afalse%2C%22padding%22%3A%2234%2C23%2C34%2C23%22%2C%22containerbackground%22%3A%22%23ffffff%22%7D"> <tr> <td role="module-content"  valign="top" height="100%" style="padding: 34px 23px 34px 23px;" bgcolor="#ffffff"> <h1 style="text-align: center;"><span style="color:#2D2D2D;">Featured Activity: HRDF Insight Piece</span></h1> <div style="text-align: center;">Lorem ipsum dolor sit amet, vix facer virtute conceptam ne. Te qui consul graeco imperdiet, omnes pertinax torquatos eu quo, nam et summo admodum sensibus.</div> <div style="text-align: center;">Et veri ludus petentium eam. Mandamus erroribus ei has, cu his illud veniam.</div> </td> </tr> </table> <table class="module" role="module" data-type="spacer" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-attributes="%7B%22dropped%22%3Atrue%2C%22spacing%22%3A10%2C%22containerbackground%22%3A%22%23f6f6f6%22%7D"> <tr><td role="module-content" style="padding: 0px 0px 10px 0px;" bgcolor="#f6f6f6"></td></tr></table> <table class="module" role="module" data-type="text" border="0" cellpadding="0" cellspacing="0"  width="100%" style="table-layout: fixed;" data-attributes="%7B%22dropped%22%3Atrue%2C%22child%22%3Afalse%2C%22padding%22%3A%2215%2C23%2C34%2C23%22%2C%22containerbackground%22%3A%22%23ffffff%22%7D"> <tr> <td role="module-content"  valign="top" height="100%" style="padding: 15px 23px 34px 23px;" bgcolor="#ffffff"> <h1 style="text-align: center;"><span style="color:#2D2D2D;">Data Journalism Updates</span></h1> <h2 style="text-align: center;">What we published this month</h2> <div style="text-align: center;"> <div style="color: rgb(98, 98, 98); font-family: helvetica, arial, sans-serif; text-align: center; background-color: rgb(255, 255, 255);"><a href="http://www.indiaspend.com/cover-story/to-cut-delhis-air-pollution-pinpoint-the-source-40763">"How to pinpoint Delhi"s air pollution sources"</a></div> <div style="color: rgb(98, 98, 98); font-family: helvetica, arial, sans-serif; text-align: center; background-color: rgb(255, 255, 255);">Eric Dodge, January 20, 2016. Indiaspend.</div> <div style="color: rgb(98, 98, 98); font-family: helvetica, arial, sans-serif; text-align: center; background-color: rgb(255, 255, 255);">2379 views on Indiaspend.</div> <div style="color: rgb(98, 98, 98); font-family: helvetica, arial, sans-serif; text-align: center; background-color: rgb(255, 255, 255);">&nbsp;</div> <div style="color: rgb(98, 98, 98); font-family: helvetica, arial, sans-serif; text-align: center; background-color: rgb(255, 255, 255);"> <div style="color: rgb(98, 98, 98); font-family: helvetica, arial, sans-serif; text-align: center; background-color: rgb(255, 255, 255);"><a href="http://www.indiaspend.com/cover-story/how-to-pinpoint-delhis-air-pollution-sources-45985">"To cut Delhi"s air pollution, pinpoint the source"</a></div> <div style="color: rgb(98, 98, 98); font-family: helvetica, arial, sans-serif; text-align: center; background-color: rgb(255, 255, 255);">Eric Dodge and Rohini Pande, January 19, 2016. Indiaspend.</div> <div style="color: rgb(98, 98, 98); font-family: helvetica, arial, sans-serif; text-align: center; background-color: rgb(255, 255, 255);">2888 views on Indiaspend.</div> </div> <div style="color: rgb(98, 98, 98); font-family: helvetica, arial, sans-serif; text-align: center; background-color: rgb(255, 255, 255);"> <h2 style="color: rgb(98, 98, 98); text-align: center; background-color: rgb(255, 255, 255);">Our past pieces</h2> <div> <div style="color: rgb(98, 98, 98); font-family: helvetica, arial, sans-serif; text-align: center;">"<a href="http://indianexpress.com/article/opinion/columns/rti-rti-act-mgnrega/">Impersonal government is good"</a></div> <div style="color: rgb(98, 98, 98); font-family: helvetica, arial, sans-serif; text-align: center;">Rohini Pande, Charity Troyer Moore&nbsp;and Eric Dodge, December 30, 2016. Indian Express.</div> <div style="color: rgb(98, 98, 98); font-family: helvetica, arial, sans-serif; text-align: center;">Pageview data not available.</div> <div style="color: rgb(98, 98, 98); font-family: helvetica, arial, sans-serif; text-align: center;">&nbsp;</div> <a href="http://www.indiaspend.com/cover-story/delhi-had-clean-spring-air-but-it-wont-last-17359">"Delhi had clean spring air -- but it won"t last"</a></div> <div>Eric Dodge and Kevin Rowe, October 19, 2015. Indiaspend.</div> <div>4521 views on Indiaspend.</div> <div>&nbsp;</div> <div>&nbsp;</div> </div> </div> </td> </tr> </table> <table class="module" role="module" data-type="spacer" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-attributes="%7B%22dropped%22%3Atrue%2C%22spacing%22%3A10%2C%22containerbackground%22%3A%22%23f6f6f6%22%7D"> <tr><td role="module-content" style="padding: 0px 0px 10px 0px;" bgcolor="#f6f6f6"></td></tr></table> <table class="module" role="module" data-type="text" border="0" cellpadding="0" cellspacing="0"  width="100%" style="table-layout: fixed;" data-attributes="%7B%22dropped%22%3Atrue%2C%22child%22%3Afalse%2C%22padding%22%3A%2215%2C23%2C34%2C23%22%2C%22containerbackground%22%3A%22%23ffffff%22%7D"> <tr> <td role="module-content"  valign="top" height="100%" style="padding: 15px 23px 34px 23px;" bgcolor="#ffffff"> <h1 style="text-align: center;"><span style="color:#2D2D2D;">Internal support</span></h1> <div style="text-align: center;">Angela helped AmandaR streamline the ODK to Stata to email pipeline in Python. +/- lines of code.</div> <div style="text-align: center;">&nbsp;</div> <div style="text-align: center;">Clearances: Eric helped Sujoy cillum dolore eu fugiat nulla pariatur.</div> <div style="text-align: center;"> <div style="color: rgb(98, 98, 98); font-family: helvetica, arial, sans-serif; text-align: center; background-color: rgb(255, 255, 255);"> <div>&nbsp;</div> </div> </div> </td> </tr> </table> <table class="module" role="module" data-type="spacer" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-attributes="%7B%22dropped%22%3Atrue%2C%22spacing%22%3A10%2C%22containerbackground%22%3A%22%23f6f6f6%22%7D"> <tr><td role="module-content" style="padding: 0px 0px 10px 0px;" bgcolor="#f6f6f6"></td></tr></table> <table class="module" role="module" data-type="text" border="0" cellpadding="0" cellspacing="0"  width="100%" style="table-layout: fixed;" data-attributes="%7B%22dropped%22%3Atrue%2C%22child%22%3Afalse%2C%22padding%22%3A%2215%2C23%2C34%2C23%22%2C%22containerbackground%22%3A%22%23ffffff%22%7D"> <tr> <td role="module-content"  valign="top" height="100%" style="padding: 15px 23px 34px 23px;" bgcolor="#ffffff"> <h1 style="text-align: center;"><span style="color:#2D2D2D;">About Us</span></h1> <div style="text-align: center;">Lorem ipsum dolor sit amet, vix facer virtute conceptam ne. Te qui consul graeco imperdiet, omnes pertinax torquatos eu quo, nam et summo admodum sensibus.</div> <div style="text-align: center;">Et veri ludus petentium eam. Mandamus erroribus ei has, cu his illud veniam.</div> </td> </tr> </table> <table class="module" role="module" data-type="spacer" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-attributes="%7B%22dropped%22%3Atrue%2C%22spacing%22%3A10%2C%22containerbackground%22%3A%22%23f6f6f6%22%7D"> <tr><td role="module-content" style="padding: 0px 0px 10px 0px;" bgcolor="#f6f6f6"></td></tr></table> <table class="module" role="module" data-type="spacer" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-attributes="%7B%22dropped%22%3Atrue%2C%22spacing%22%3A3%2C%22containerbackground%22%3A%22%2332A9D6%22%7D"> <tr><td role="module-content" style="padding: 0px 0px 3px 0px;" bgcolor="#32A9D6"></td></tr></table> <table class="module" role="module" data-type="spacer" border="0" cellpadding="0" cellspacing="0" width="100%" style="table-layout: fixed;" data-attributes="%7B%22dropped%22%3Atrue%2C%22spacing%22%3A3%2C%22containerbackground%22%3A%22%2332A9D6%22%7D"> <tr><td role="module-content" style="padding: 0px 0px 3px 0px;" bgcolor="#32A9D6"></td></tr></table> <table border="0" cellpadding="0" cellspacing="0" align="center" width="100%" class="module footer" role="module" data-type="footer" data-attributes="%7B%22dropped%22%3Atrue%2C%22columns%22%3A%222%22%2C%22padding%22%3A%2248%2C34%2C17%2C34%22%2C%22containerbackground%22%3A%22%2332a9d6%22%7D"> <tr><td style="padding: 48px 34px 17px 34px;" bgcolor="#32a9d6"> <table border="0" cellpadding="0" cellspacing="0" align="center" width="100%"> <tr role="module-content"> <td align="center" valign="top" width="50%" height="100%" class="templateColumnContainer"> <table border="0" cellpadding="0" cellspacing="0" width="100%" height="100%"> <tr> <td class="leftColumnContent" role="column-one" height="100%" style="height:100%;"><table class="module" role="module" data-type="text" border="0" cellpadding="0" cellspacing="0"  width="100%" style="table-layout: fixed;" data-attributes="%7B%22dropped%22%3Atrue%2C%22child%22%3Afalse%2C%22padding%22%3A%220%2C0%2C0%2C0%22%2C%22containerbackground%22%3A%22%22%7D"> <tr> <td role="module-content"  valign="top" height="100%" style="padding: 0px 0px 0px 0px;" bgcolor=""> <div style="font-size: 10px; line-height: 150%; margin: 0px;">&nbsp;</div><div style="font-size: 10px; line-height: 150%; margin: 0px;">&nbsp;</div><div style="font-size: 10px; line-height: 150%; margin: 0px;"><a href="[unsubscribe]"><span style="color:#FFFFFF;">Unsubscribe</span></a><span style="color:#FFFFFF;"> | </span><a href="[Unsubscribe_Preferences]"><span style="color:#FFFFFF;">Update Preferences</span></a></div> </td> </tr> </table> </td> </tr> </table> </td> <td align="center" valign="top" width="50%" height="100%" class="templateColumnContainer"> <table border="0" cellpadding="0" cellspacing="0" width="100%" height="100%"> <tr> <td class="rightColumnContent" role="column-two" height="100%" style="height:100%;"><table class="module" role="module" data-type="text" border="0" cellpadding="0" cellspacing="0"  width="100%" style="table-layout: fixed;" data-attributes="%7B%22dropped%22%3Atrue%2C%22child%22%3Afalse%2C%22padding%22%3A%220%2C0%2C0%2C0%22%2C%22containerbackground%22%3A%22%22%7D"> <tr> <td role="module-content"  valign="top" height="100%" style="padding: 0px 0px 0px 0px;" bgcolor=""> <div style="font-size: 10px; line-height: 150%; margin: 0px; text-align: right;"><span style="color:#ffffff;">[Sender_Name]</span></div><div style="font-size: 10px; line-height: 150%; margin: 0px; text-align: right;"><span style="color:#ffffff;">[Sender_Address]</span></div><div style="font-size: 10px; line-height: 150%; margin: 0px; text-align: right;"><span style="color:#ffffff;">[Sender_City], [Sender_State] [Sender_Zip]</span></div> </td> </tr> </table> </td> </tr> </table> </td> </tr> </table> </td></tr> </table> </tr></td> </table> <!--[if (gte mso 9)|(IE)]> </td> </td> </table> <![endif]--> </td> </tr> </table></td> </tr> </table> <!--[if (gte mso 9)|(IE)]> </td> </tr> </table> <![endif]--> </tr></td> </table> </div> </center> </body> </html>'
	
	html = html.format(
		PAYDASH_A=github_stats['repos']['paydash']['a'],
		PAYDASH_D=github_stats['repos']['paydash']['d'],
		PAYDATA_A=github_stats['repos']['paydata']['a'],
		PAYDATA_D=github_stats['repos']['paydata']['d'],
		HRDF_A=github_stats['repos']['hrdf']['a'],
		HRDF_D=github_stats['repos']['hrdf']['d'],
		MNREGACASE_A=github_stats['repos']['mnrega-case']['a'],
		MNREGACASE_D=github_stats['repos']['mnrega-case']['d'],

		ANGELA_A=github_stats['users']['angelaambroz']['a'],
		ANGELA_D=github_stats['users']['angelaambroz']['d'],
		ERIC_A=github_stats['users']['edodge']['a'],
		ERIC_D=github_stats['users']['edodge']['d'],
		RAVI_A=github_stats['users']['ravisuhag']['a'],
		RAVI_D=github_stats['users']['ravisuhag']['d'],
		SARAH_A=github_stats['users']['sgriffis89']['a'],
		SARAH_D=github_stats['users']['sgriffis89']['d']
	)
	
	sg = sendgrid.SendGridClient(API_KEY, None, raise_errors=True)

	message = sendgrid.Mail()
	message.add_to(['Eric Dodge <eric_dodge@hks.harvard.edu>'])
	message.set_subject('epod.io :: January 2016 TEST')
	message.set_html(html)
	message.set_text('epod.io update for January 2016')
	message.set_from('epod.io <epod.analytics@gmail.com>')
	message.add_category('January 2016 Update')

	try:
		sg.send(message)
		print 'Successfully sent the mail'
	except SendGridClientError as e:
	    print e
	except SendGridServerError as e:
		print e


def get_github_stats(USERNAME,PASSWORD):

	current_month = datetime.datetime.now().month

	repos = ['paydash','paydata','hrdf','mnrega-case']
	repo_lines = {repo: {'a':0,'d':0} for repo in repos}

	users = ['angelaambroz','ravisuhag','edodge','sgriffis89']
	user_lines = {user: {'a':0,'d':0} for user in users}

	for repo in repos:
		r = requests.get('https://api.github.com/repos/hks-epod/'+repo+'/stats/contributors', auth=(USERNAME, PASSWORD))
		contributors = json.loads(r.content)
		for contributor in contributors:
			for week in contributor['weeks']:
				if datetime.datetime.fromtimestamp(week['w']).month == current_month:
					repo_lines[repo]['a'] += week['a']
					repo_lines[repo]['d'] += week['d']
					if contributor['author']['login'] in users:
						user_lines[contributor['author']['login']]['a'] += week['a']
						user_lines[contributor['author']['login']]['d'] += week['d']



	print repo_lines
	print user_lines
	return {'repos':repo_lines,'users':user_lines}

def main():
	
	with open('./secrets.json') as data_file:
		SECRETS = json.load(data_file)

	API_KEY = SECRETS['sendgrid_api_key']
	USERNAME = SECRETS['github_username']
	PASSWORD = SECRETS['github_password']

	github_stats = get_github_stats(USERNAME,PASSWORD)
	send_mail(API_KEY,github_stats)


if __name__ == '__main__':
	main()