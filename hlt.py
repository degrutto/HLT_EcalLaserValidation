



<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head id="ctl00_ctl00_NICEMasterPageHead"><meta name="viewport" content="width=device-width, target-densityDpi=160dpi, initial-scale=1" /><meta name="MobileOptimized" content="width" /><meta name="HandheldFriendly" content="true" /><meta name="apple-mobile-web-app-capable" content="yes" /><meta http-equiv="cleartype" content="on" /><meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" /><link href="/adfs/ls/MasterPages/framework/2.0/fonts/PTMonoWeb/PTM55Fstylesheet.css" rel="Stylesheet" type="text/css" /><link href="/adfs/ls/MasterPages/framework/2.0/fonts/PTSansWeb/PTSansWeb.css" rel="Stylesheet" type="text/css" /><link href="/adfs/ls/MasterPages/framework/2.0/fonts/PTSerifWeb/PTSerifWeb.css" rel="Stylesheet" type="text/css" />

    
    <link href="/adfs/ls/MasterPages/toolbar/css/toolbar.css" rel="stylesheet" type="text/css" />
    <!--[if lt IE 8]>
        <link href="/adfs/ls/MasterPages/toolbar/css/toolbar-ie.css" rel="stylesheet" type="text/css" />
    <![endif]-->

    
    <title>Cern Authentication</title>
    <link href="/adfs/ls/favicon.ico" rel="ICON" type="image/x-icon" />
    <link href="/adfs/ls/favicon.ico" rel="SHORTCUT ICON" type="image/x-icon" />
    <meta name="application-name" content="sso-management" />
    
  <script language="javascript" type="text/javascript">
    function showhide2fa() {
      if (document.getElementById('ctl00_ctl00_NICEMasterPageBodyContent_SiteContentPlaceholder_div2FAAuthSystems').style.display == 'inline') {
        document.getElementById('ctl00_ctl00_NICEMasterPageBodyContent_SiteContentPlaceholder_div2FAAuthSystems').style.display = 'none';
        document.getElementById('ctl00_ctl00_NICEMasterPageBodyContent_SiteContentPlaceholder_href2FAAuthSystems').textContent = '[show]';
      } else {
        document.getElementById('ctl00_ctl00_NICEMasterPageBodyContent_SiteContentPlaceholder_div2FAAuthSystems').style.display = 'inline';
        document.getElementById('ctl00_ctl00_NICEMasterPageBodyContent_SiteContentPlaceholder_href2FAAuthSystems').textContent = '[hide]';
      }
    }
    function showhidedebug() {
      document.getElementById('ctl00_ctl00_NICEMasterPageBodyContent_SiteContentPlaceholder_divDebug').style.display = 'block';
      document.getElementById('ctl00_ctl00_NICEMasterPageBodyContent_SiteContentPlaceholder_hrefShowDebug').style.display = 'none';
    }
  </script>

  <script type="text/javascript" src="js/jquery.min.js"></script>
  

  <script type="text/javascript" src="js/improvedDropDown.js"></script>


<link href="App_Themes/Default/01-CernWeb-General.css" type="text/css" rel="stylesheet" /><link href="App_Themes/Default/02-CernWeb-Header.css" type="text/css" rel="stylesheet" /><link href="App_Themes/Default/03-CernWeb-OISStyle.css" type="text/css" rel="stylesheet" /><link href="App_Themes/Default/06-CustomStyle.css" type="text/css" rel="stylesheet" /><link href="App_Themes/Default/07-default-ImprovedDropDown.css" type="text/css" rel="stylesheet" /><link href="App_Themes/Default/10-CernWeb-SmallDevices.css" type="text/css" rel="stylesheet" /><meta name="robots" content="noindex, nofollow, noarchive" /><title>

</title></head>

   


<body id="ctl00_ctl00_NICEMasterPageBody">
  <form name="aspnetForm" method="post" action="/adfs/ls/?wa=wsignin1.0&amp;wreply=https%3A%2F%2Fsharper.web.cern.ch%2FShibboleth.sso%2FADFS&amp;wct=2022-06-15T17%3A09%3A44Z&amp;wtrealm=https%3A%2F%2Fsharper.web.cern.ch%2FShibboleth.sso%2FADFS&amp;wctx=cookie%3A1655312984_2bec" id="aspnetForm">
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="/wEPDwUKLTcwMDIwMTIzOA8WAh4TVmFsaWRhdGVSZXF1ZXN0TW9kZQIBZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WAQVNY3RsMDAkY3RsMDAkTklDRU1hc3RlclBhZ2VCb2R5Q29udGVudCRTaXRlQ29udGVudFBsYWNlaG9sZGVyJGNoa1JlbWVtYmVyTG9naW55zGggmjUO9MyY8SuFAsq3+JmijA==" />

<input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="0EE29E36" /><input type="hidden" name="__db" value="14" />

    
    <div id="ctl00_ctl00_pnlToolbar">
	

	 <div id="cern-toolbar">
		    <h1><a href="http://cern.ch" title="CERN">CERN <span>Accelerating science</span></a></h1>
		    <ul class="cern-signedin">
                <li class="cern-accountlinks active"><a class="cern-account" title="Sign in to your CERN account">Sign in</a></li>
			    <li><a class="cern-directory" href="http://cern.ch/directory" title="Search CERN resources and browse the directory">Directory</a></li>
		    </ul>
	    </div>

	
</div>
      
    
    <div id="ctl00_ctl00_pnlHeader">
	
        <div id="header" >
            <div id="ctl00_ctl00_HeaderTitle" class="bgHeaderImage page">
                <h2 id="site-name">
    <a href="/" title="Home" rel="home">CERN Single Sign-On</a>
</h2>
                <h3 id="site-slogan">
    Sign in with a CERN account, a Federation account or a public service account
</h3>
	        </div>

            <div id="main-navigation" class="page">
                

            </div>
        </div>
    
</div>

    
    <div id="page">
        
    
    

  
  

  
  

  
  <div id="ctl00_ctl00_NICEMasterPageBodyContent_SiteContentPlaceholder_pnlCernAuthentication">
	
    <div class="box_auth">
      <div class="signinwith fullWidth">Sign in with your CERN account</div>
      <div class="smaller note important">Reminder: you have agreed to comply with the 
        <a href="http://cern.ch/ComputingRules">CERN computing rules</a>, in particular OC5. CERN implements the 
        measures necessary to ensure compliance.</div>
      <div id="ctl00_ctl00_NICEMasterPageBodyContent_SiteContentPlaceholder_pnlForm">
		
        <div class="oneAuthType">Use credentials</div>
        <div class="oneAuth">
          <table>
            <tr>
              <td class="box_login smaller" style="color: gray;">Username or Email address</td>
              <td class="box_password smaller" style="color: gray;">Password</td>
              <td class="box_signinbutton"></td>
            </tr>
            <tr>
              <td class="box_login">
                <input name="ctl00$ctl00$NICEMasterPageBodyContent$SiteContentPlaceholder$txtFormsLogin" type="text" id="ctl00_ctl00_NICEMasterPageBodyContent_SiteContentPlaceholder_txtFormsLogin" title="Enter your Username or Email Address" /></td>
              <td class="box_password">
                <input name="ctl00$ctl00$NICEMasterPageBodyContent$SiteContentPlaceholder$txtFormsPassword" type="password" id="ctl00_ctl00_NICEMasterPageBodyContent_SiteContentPlaceholder_txtFormsPassword" /></td>
              <td class="box_signinbutton">
                <input type="submit" name="ctl00$ctl00$NICEMasterPageBodyContent$SiteContentPlaceholder$btnFormsLogin" value="Sign in" onclick="javascript:WebForm_DoPostBackWithOptions(new WebForm_PostBackOptions(&quot;ctl00$ctl00$NICEMasterPageBodyContent$SiteContentPlaceholder$btnFormsLogin&quot;, &quot;&quot;, true, &quot;credentials&quot;, &quot;&quot;, false, false))" id="ctl00_ctl00_NICEMasterPageBodyContent_SiteContentPlaceholder_btnFormsLogin" class="button_signin" /></td>
            </tr>

            <tr>
              <td class="box_login smaller">
                <div id="ctl00_ctl00_NICEMasterPageBodyContent_SiteContentPlaceholder_pnlForm1">
			
                  <span class="subtle"><input id="ctl00_ctl00_NICEMasterPageBodyContent_SiteContentPlaceholder_chkRememberLogin" type="checkbox" name="ctl00$ctl00$NICEMasterPageBodyContent$SiteContentPlaceholder$chkRememberLogin" /><label for="ctl00_ctl00_NICEMasterPageBodyContent_SiteContentPlaceholder_chkRememberLogin">Remember Username or Email Address</label></span>
                
		</div>
              </td>
              <td class="box_password smaller" style="vertical-align: bottom;"><a href="https://account.cern.ch/account/Help/?kbid=021010" target="_blank">Need password help ?</a></td>
              <td class="box_signinbutton"></td>
            </tr>

            <tr>
              <td colspan="3" class="message error">
                <span id="ctl00_ctl00_NICEMasterPageBodyContent_SiteContentPlaceholder_lblFormsError"></span>
                &nbsp;
                &nbsp;
              </td>
            </tr>
          </table>
        </div>
      
	</div>

      <div id="ctl00_ctl00_NICEMasterPageBodyContent_SiteContentPlaceholder_pnlOneClickAuthentication">
		
        <div class="oneAuthType">Use one-click authentication</div>

        <div id="ctl00_ctl00_NICEMasterPageBodyContent_SiteContentPlaceholder_pnlNTLM">
			

          <div class="oneAuth">
            <table>
              <tr>
                <td rowspan="2" class="fedicon">
                  <img src="/adfs/ls/images/federation/ieff2.png" alt="Kerberos based authentication" /></td>
                <td class="fedtitle">
                  <a id="ctl00_ctl00_NICEMasterPageBodyContent_SiteContentPlaceholder_hlNTLM2" href="auth/integrated/?wa=wsignin1.0&amp;wreply=https%3A%2F%2Fsharper.web.cern.ch%2FShibboleth.sso%2FADFS&amp;wct=2022-06-15T17%3A09%3A44Z&amp;wtrealm=https%3A%2F%2Fsharper.web.cern.ch%2FShibboleth.sso%2FADFS&amp;wctx=cookie%3A1655312984_2bec">Sign in using your current Windows/Kerberos credentials</a>
                  <a id="ctl00_ctl00_NICEMasterPageBodyContent_SiteContentPlaceholder_hlNTLMAutologon" title="Enables Autologon with current Windows/Kerberos Credentials. Click Logout in the Application to disable." href="javascript:__doPostBack(&#39;ctl00$ctl00$NICEMasterPageBodyContent$SiteContentPlaceholder$hlNTLMAutologon&#39;,&#39;&#39;)">[autologon]</a>
                </td>
              </tr>
              <tr>
                <td class="fedtext">Use your current authentication token. You need Internet Explorer on CERN Windows or 
                    Firefox on SLC (<a href="http://linux.web.cern.ch/linux/scientific5/docs/rhel/Deployment_Guide/sso-config-firefox.html" target="_blank" style="color: #777777;">Firefox help here</a>).</td>
              </tr>
            </table>
          </div>

        
		</div>

        <div id="ctl00_ctl00_NICEMasterPageBodyContent_SiteContentPlaceholder_pnlCertificates">
			
          <div class="oneAuth">
            <table>
              <tr>
                <td rowspan="2" class="fedicon">
                  <img src="/adfs/ls/images/federation/cern_25x25.gif" border="0" alt="Certificate authentication" /></td>
                <td class="fedtitle">
                  <a id="ctl00_ctl00_NICEMasterPageBodyContent_SiteContentPlaceholder_hlCertificateAuth" title="You can get a CERN certificate on http://cern.ch/ca" href="auth/sslclient/?wa=wsignin1.0&amp;wreply=https%3A%2F%2Fsharper.web.cern.ch%2FShibboleth.sso%2FADFS&amp;wct=2022-06-15T17%3A09%3A44Z&amp;wtrealm=https%3A%2F%2Fsharper.web.cern.ch%2FShibboleth.sso%2FADFS&amp;wctx=cookie%3A1655312984_2bec">Sign in using your CERN Certificate</a>
                  <a onclick="javascript:return confirm(&#39;Warning: please ensure you successfully authenticated with your Certificate by clicking on \&#39;Sign in using your Certificate\&#39; before enabling autologon.\r\nIf autologon is enabled with a bad Certificate your will have to Clear your Browser\&#39;s cookies to disable the feature.\r\nClick Ok to proceed with autologon enabling or Cancel if you are unsure or don\&#39;t understand this message.&#39;);" id="ctl00_ctl00_NICEMasterPageBodyContent_SiteContentPlaceholder_hlCertificateAutologon" title="Enables Autologon with Certificate. Click Logout in the Application to disable. You can get a CERN certificate on http://cern.ch/ca." href="javascript:__doPostBack(&#39;ctl00$ctl00$NICEMasterPageBodyContent$SiteContentPlaceholder$hlCertificateAutologon&#39;,&#39;&#39;)">[autologon]</a>
                </td>
              </tr>
              <tr>
                <td class="fedtext">You can get a CERN certificate on the 
                    <a href="http://cern.ch/ca">CERN Certification Authority website</a>.</td>
              </tr>
            </table>
          </div>
        
		</div>
      
	</div>

      

      <div id="ctl00_ctl00_NICEMasterPageBodyContent_SiteContentPlaceholder_pnl2FAsystems">
		
        <div class="oneAuthType">
          Use strong two factor authentication 
                <a href="javascript:showhide2fa();" id="ctl00_ctl00_NICEMasterPageBodyContent_SiteContentPlaceholder_href2FAAuthSystems" style="font-weight:normal;color:#777777;display:inline;">[show]</a>
        </div>
        <div id="ctl00_ctl00_NICEMasterPageBodyContent_SiteContentPlaceholder_div2FAAuthSystems" class="oneAuth" style="display:none;">
          <table id="ctl00_ctl00_NICEMasterPageBodyContent_SiteContentPlaceholder_tbl2FAsystems" border="0" width="100%">
			<tr>
				<td class="fedrow"><table class="fedtable" border="0">
					<tr>
						<td class="fedicon" rowspan="2"><a href="javascript:__doPostBack(&#39;ctl00$ctl00$NICEMasterPageBodyContent$SiteContentPlaceholder$ctl02&#39;,&#39;&#39;)"><img src="/adfs/ls/images/federation/fingerprint.png" border="0" ></a></td><td class="fedtitle"><a href="javascript:__doPostBack(&#39;ctl00$ctl00$NICEMasterPageBodyContent$SiteContentPlaceholder$ctl03&#39;,&#39;&#39;)">Two Factor Authentication</a></td>
					</tr><tr>
						<td class="fedtext">Two factor authentication using your CERN credentials and a verification code like SMS code or Google Authenticator, a device like Yubikeys or Smartcards or biometry.</td>
					</tr>
				</table></td>
			</tr>
		</table>
        </div>
      
	</div>
    </div>
  
</div>

  
  <div id="ctl00_ctl00_NICEMasterPageBodyContent_SiteContentPlaceholder_pnlPublicService">
	
    <div class="box_auth">
      <div class="signinwith fullWidth">Sign in with a public service account</div>
	  <div>Some social account providers, e.g. Facebook, may use knowledge about your access to CERN for purposes such as profiling.</div>
      <div id="ctl00_ctl00_NICEMasterPageBodyContent_SiteContentPlaceholder_pnlPublicServiceList">
		
        <div class="oneAuth">
          <table id="ctl00_ctl00_NICEMasterPageBodyContent_SiteContentPlaceholder_tblPublicServices" border="0" width="100%">
			<tr>
				<td class="fedrow"><table class="fedtable" border="0">
					<tr>
						<td class="fedicon" rowspan="2"><a href="javascript:__doPostBack(&#39;ctl00$ctl00$NICEMasterPageBodyContent$SiteContentPlaceholder$ctl05&#39;,&#39;&#39;)"><img src="/adfs/ls/images/federation/fbgl.png" border="0" ></a></td><td class="fedtitle"><a href="javascript:__doPostBack(&#39;ctl00$ctl00$NICEMasterPageBodyContent$SiteContentPlaceholder$ctl06&#39;,&#39;&#39;)">Facebook, Google, Live, etc.</a></td>
					</tr><tr>
						<td class="fedtext">Authenticate using an external account provider such as Facebook, Google, Live, Yahoo, Orange.</td>
					</tr>
				</table></td>
			</tr>
		</table>
        </div>
      
	</div>
    </div>
  
</div>

  
  <div id="ctl00_ctl00_NICEMasterPageBodyContent_SiteContentPlaceholder_pnlFederation">
	
    <div class="box_auth">
      <div class="signinwith fullWidth">Sign in with your organization or institution account</div>

      <div class="oneAuth" style="margin-top: 2px;">
        <table>
          <tr>
            <td class="fedicon">
              <img src="/adfs/ls/images/federation/eduGAIN50.png" border="0" alt="Federation authentication" /></td>

            <td>
              <select name="ctl00$ctl00$NICEMasterPageBodyContent$SiteContentPlaceholder$drpFederation" id="ctl00_ctl00_NICEMasterPageBodyContent_SiteContentPlaceholder_drpFederation" class="improvedDropDown-dropdownlist">
		<option value="-">Enter the name of the organisation you are affiliated with...</option>
		<option value="http://adfs.act.edu.om/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://adfs.act.edu.om/adfs/services/trust</option>
		<option value="http://adfs.amnh.org/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://adfs.amnh.org/adfs/services/trust</option>
		<option value="http://adfs.asu.edu.om/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://adfs.asu.edu.om/adfs/services/trust</option>
		<option value="http://adfs.bayancollege.edu.om/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://adfs.bayancollege.edu.om/adfs/services/trust</option>
		<option value="http://adfs.brm-vtc.edu.om/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://adfs.brm-vtc.edu.om/adfs/services/trust</option>
		<option value="http://adfs.du.edu.om/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://adfs.du.edu.om/adfs/services/trust</option>
		<option value="http://adfs.ftik.edu.om/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://adfs.ftik.edu.om/adfs/services/trust</option>
		<option value="http://adfs.gcet.edu.om/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://adfs.gcet.edu.om/adfs/services/trust</option>
		<option value="http://adfs.gutech.edu.om/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://adfs.gutech.edu.om/adfs/services/trust</option>
		<option value="http://Adfs.hct.edu.om/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://Adfs.hct.edu.om/adfs/services/trust</option>
		<option value="http://adfs.ibrivtc.edu.om/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://adfs.ibrivtc.edu.om/adfs/services/trust</option>
		<option value="http://adfs.ict.edu.om/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://adfs.ict.edu.om/adfs/services/trust</option>
		<option value="http://adfs.imco.edu.om/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://adfs.imco.edu.om/adfs/services/trust</option>
		<option value="http://adfs.lsuhsc.edu/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://adfs.lsuhsc.edu/adfs/services/trust</option>
		<option value="http://adfs.majancollege.edu.om/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://adfs.majancollege.edu.om/adfs/services/trust</option>
		<option value="http://adfs.mcbs.edu.om/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://adfs.mcbs.edu.om/adfs/services/trust</option>
		<option value="http://adfs.msoe.edu/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://adfs.msoe.edu/adfs/services/trust</option>
		<option value="http://adfs.mtc.edu.om/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://adfs.mtc.edu.om/adfs/services/trust</option>
		<option value="http://adfs.muscatcollege.edu.om/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://adfs.muscatcollege.edu.om/adfs/services/trust</option>
		<option value="http://adfs.muscatuniversity.edu.om/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://adfs.muscatuniversity.edu.om/adfs/services/trust</option>
		<option value="http://adfs.nct.edu.om/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://adfs.nct.edu.om/adfs/services/trust</option>
		<option value="http://adfs.ndc.edu.om/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://adfs.ndc.edu.om/adfs/services/trust</option>
		<option value="http://adfs.nic.edu/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://adfs.nic.edu/adfs/services/trust</option>
		<option value="http://adfs.nsf.gov/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://adfs.nsf.gov/adfs/services/trust</option>
		<option value="http://adfs.nu.edu.om/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://adfs.nu.edu.om/adfs/services/trust</option>
		<option value="http://adfs.omren.om/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://adfs.omren.om/adfs/services/trust</option>
		<option value="http://adfs.otc.edu.om/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://adfs.otc.edu.om/adfs/services/trust</option>
		<option value="http://adfs.otc.edu/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://adfs.otc.edu/adfs/services/trust</option>
		<option value="http://adfs.philau.edu/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://adfs.philau.edu/adfs/services/trust</option>
		<option value="http://adfs.ppd.com/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://adfs.ppd.com/adfs/services/trust</option>
		<option value="http://adfs.sahamvtc.edu.om/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://adfs.sahamvtc.edu.om/adfs/services/trust</option>
		<option value="http://adfs.sct.edu.om/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://adfs.sct.edu.om/adfs/services/trust</option>
		<option value="http://adfs.seebvc.edu.om/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://adfs.seebvc.edu.om/adfs/services/trust</option>
		<option value="http://adfs.shct.edu.om/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://adfs.shct.edu.om/adfs/services/trust</option>
		<option value="http://adfs.shinasvc.edu.om/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://adfs.shinasvc.edu.om/adfs/services/trust</option>
		<option value="http://adfs.squ.edu.om/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://adfs.squ.edu.om/adfs/services/trust</option>
		<option value="http://adfs.sso.passhe.edu/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://adfs.sso.passhe.edu/adfs/services/trust</option>
		<option value="http://adfs.suc.edu.om/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://adfs.suc.edu.om/adfs/services/trust</option>
		<option value="http://adfs.survc.edu.om/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://adfs.survc.edu.om/adfs/services/trust</option>
		<option value="http://adfs.umu.se/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://adfs.umu.se/adfs/services/trust</option>
		<option value="http://adfs.unco.edu/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://adfs.unco.edu/adfs/services/trust</option>
		<option value="http://adfs.uob.edu.om/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://adfs.uob.edu.om/adfs/services/trust</option>
		<option value="http://adfs.uwsp.edu/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://adfs.uwsp.edu/adfs/services/trust</option>
		<option value="http://adfs3.fmi.ch/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://adfs3.fmi.ch/adfs/services/trust</option>
		<option value="http://adfs-omr.manpower.gov.om/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://adfs-omr.manpower.gov.om/adfs/services/trust</option>
		<option value="http://bcadfs.bridgewater.edu/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://bcadfs.bridgewater.edu/adfs/services/trust</option>
		<option value="http://fca-caf.uottawa.ca/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://fca-caf.uottawa.ca/adfs/services/trust</option>
		<option value="http://fed.lit.edu/adfs/ls" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://fed.lit.edu/adfs/ls</option>
		<option value="http://federate.bsu.edu/sso" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://federate.bsu.edu/sso</option>
		<option value="http://fs.albmolecular.com/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://fs.albmolecular.com/adfs/services/trust</option>
		<option value="http://fs.bth.se/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://fs.bth.se/adfs/services/trust</option>
		<option value="http://fs.carilionclinic.org/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://fs.carilionclinic.org/adfs/services/trust</option>
		<option value="http://fs.css.edu.om/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://fs.css.edu.om/adfs/services/trust</option>
		<option value="http://fs.liu.se/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://fs.liu.se/adfs/services/trust</option>
		<option value="http://fs.mazcol.edu.om/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://fs.mazcol.edu.om/adfs/services/trust</option>
		<option value="http://fs.su.edu.om/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://fs.su.edu.om/adfs/services/trust</option>
		<option value="http://fs.trc.gov.om/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://fs.trc.gov.om/adfs/services/trust</option>
		<option value="http://fs.unilasalle.fr/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://fs.unilasalle.fr/adfs/services/trust</option>
		<option value="http://fs.unizwa.edu.om/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://fs.unizwa.edu.om/adfs/services/trust</option>
		<option value="http://fs.uqac.ca/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://fs.uqac.ca/adfs/services/trust</option>
		<option value="http://fs.uwlax.edu/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://fs.uwlax.edu/adfs/services/trust</option>
		<option value="http://fs.uwp.edu/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://fs.uwp.edu/adfs/services/trust</option>
		<option value="http://fs.wcu.edu/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://fs.wcu.edu/adfs/services/trust</option>
		<option value="http://iam.auckland.ac.nz/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://iam.auckland.ac.nz/idp</option>
		<option value="http://idp.chalmers.se/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://idp.chalmers.se/adfs/services/trust</option>
		<option value="http://i-idd.silab.cea.fr/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://i-idd.silab.cea.fr/adfs/services/trust</option>
		<option value="http://login.mayo.edu/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://login.mayo.edu/adfs/services/trust</option>
		<option value="http://lync.mec.edu.om/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://lync.mec.edu.om/adfs/services/trust</option>
		<option value="http://msauth.kent.edu/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://msauth.kent.edu/adfs/services/trust</option>
		<option value="http://proxy.safire.ac.za/birk.php/federate.sun.ac.za/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://proxy.safire.ac.za/birk.php/federate.sun.ac.za/adfs/services/trust</option>
		<option value="http://sso.davidson.edu/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://sso.davidson.edu/adfs/services/trust</option>
		<option value="http://sso.inrs.fr/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://sso.inrs.fr/adfs/services/trust</option>
		<option value="http://sso.oit.edu/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://sso.oit.edu/idp</option>
		<option value="http://sso.quinnipiac.edu/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://sso.quinnipiac.edu/adfs/services/trust</option>
		<option value="http://ssologin.cei.edu/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://ssologin.cei.edu/adfs/services/trust</option>
		<option value="http://sts.ait.dtu.dk/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://sts.ait.dtu.dk/adfs/services/trust</option>
		<option value="http://sts.clackamas.edu/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://sts.clackamas.edu/adfs/services/trust</option>
		<option value="http://sts1.vib.be/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://sts1.vib.be/adfs/services/trust</option>
		<option value="http://wap.nddl-lca.fr/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_http://wap.nddl-lca.fr/adfs/services/trust</option>
		<option value="https://aaf.unsw.edu.au/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://aaf.unsw.edu.au/idp/shibboleth</option>
		<option value="https://aaf1-idp.its.utas.edu.au/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://aaf1-idp.its.utas.edu.au/idp/shibboleth</option>
		<option value="https://aai.eawag.ch/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://aai.eawag.ch/idp/shibboleth</option>
		<option value="https://aai.empa.ch/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://aai.empa.ch/idp/shibboleth</option>
		<option value="https://aai.helmholtz-muenchen.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://aai.helmholtz-muenchen.de/idp/shibboleth</option>
		<option value="https://aai.unil.ch/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://aai.unil.ch/idp/shibboleth</option>
		<option value="https://aai.zhaw.ch/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://aai.zhaw.ch/idp/shibboleth</option>
		<option value="https://aaidp.academicanalytics.com/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://aaidp.academicanalytics.com/idp/shibboleth</option>
		<option value="https://aai-idp.unibe.ch/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://aai-idp.unibe.ch/idp/shibboleth</option>
		<option value="https://aai-idp.uzh.ch/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://aai-idp.uzh.ch/idp/shibboleth</option>
		<option value="https://aai-login.fhgr.ch/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://aai-login.fhgr.ch/idp/shibboleth</option>
		<option value="https://aai-login.hepl.ch/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://aai-login.hepl.ch/idp/shibboleth</option>
		<option value="https://aai-login.hsr.ch/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://aai-login.hsr.ch/idp/shibboleth</option>
		<option value="https://aai-login.pmodwrc.ch/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://aai-login.pmodwrc.ch/idp/shibboleth</option>
		<option value="https://aai-login.unine.ch/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://aai-login.unine.ch/idp/shibboleth</option>
		<option value="https://aai-logon.ethz.ch/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://aai-logon.ethz.ch/idp/shibboleth</option>
		<option value="https://aai-logon.fh-hwz.ch/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://aai-logon.fh-hwz.ch/idp/shibboleth</option>
		<option value="https://aai-logon.hes-so.ch/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://aai-logon.hes-so.ch/idp/shibboleth</option>
		<option value="https://aai-logon.ost.ch/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://aai-logon.ost.ch/idp/shibboleth</option>
		<option value="https://aai-logon.psi.ch/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://aai-logon.psi.ch/idp/shibboleth</option>
		<option value="https://aai-logon.switch.ch/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://aai-logon.switch.ch/idp/shibboleth</option>
		<option value="https://aai-logon.unibas.ch/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://aai-logon.unibas.ch/idp/shibboleth</option>
		<option value="https://aai-logon.vho-switchaai.ch/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://aai-logon.vho-switchaai.ch/idp/shibboleth</option>
		<option value="https://academica.aws.wayne.edu/saml2/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://academica.aws.wayne.edu/saml2/trust</option>
		<option value="https://access.research.cchmc.org/fed/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://access.research.cchmc.org/fed/idp</option>
		<option value="https://account.vcccd.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://account.vcccd.edu</option>
		<option value="https://accounts.google.com/o/saml2?idpid=C01l49spm" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://accounts.google.com/o/saml2?idpid=C01l49spm</option>
		<option value="https://accounts.google.com/o/saml2?idpid=C02afc2g7" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://accounts.google.com/o/saml2?idpid=C02afc2g7</option>
		<option value="https://accounts.ulbsibiu.ro/myaccount-provider/saml2/idp/metadata.php" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://accounts.ulbsibiu.ro/myaccount-provider/saml2/idp/metadata.php</option>
		<option value="https://acesso.ufabc.edu.br/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://acesso.ufabc.edu.br/idp/shibboleth</option>
		<option value="http://adfs.ad.und.edu/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://adfs.ad.und.edu/adfs/services/trust</option>
		<option value="https://adfs.ibrict.edu.om/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://adfs.ibrict.edu.om/adfs/services/trust</option>
		<option value="https://adfs.nygenome.org/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://adfs.nygenome.org/adfs/services/trust</option>
		<option value="https://adfs.otc.edu/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://adfs.otc.edu/adfs/services/trust</option>
		<option value="https://adfs.slac.stanford.edu/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://adfs.slac.stanford.edu/adfs/services/trust</option>
		<option value="https://ak.sso.litnet.lt/auth/saml2/idp/metadata.php" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://ak.sso.litnet.lt/auth/saml2/idp/metadata.php</option>
		<option value="https://alumidp.princeton.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://alumidp.princeton.edu/idp/shibboleth</option>
		<option value="https://auth.cnous.fr/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://auth.cnous.fr/idp/shibboleth</option>
		<option value="https://auth.dickinson.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://auth.dickinson.edu/idp/shibboleth</option>
		<option value="https://auth.geneseo.edu/simplesaml/saml2/idp/metadata.php" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://auth.geneseo.edu/simplesaml/saml2/idp/metadata.php</option>
		<option value="https://auth.ibs.re.kr/idp/simplesamlphp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://auth.ibs.re.kr/idp/simplesamlphp</option>
		<option value="https://auth.id.sorbonne-universite.fr/saml/metadata" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://auth.id.sorbonne-universite.fr/saml/metadata</option>
		<option value="https://auth.it.marist.edu/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://auth.it.marist.edu/idp</option>
		<option value="https://auth.lmu.edu/idpb/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://auth.lmu.edu/idpb/shibboleth</option>
		<option value="https://auth.manhattan.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://auth.manhattan.edu/idp/shibboleth</option>
		<option value="https://auth.owens.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://auth.owens.edu</option>
		<option value="https://auth.svako.lt/sso/saml2/idp/metadata.php" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://auth.svako.lt/sso/saml2/idp/metadata.php</option>
		<option value="https://auth.ulb.be/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://auth.ulb.be/idp</option>
		<option value="https://auth.unk.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://auth.unk.edu/idp/shibboleth</option>
		<option value="https://auth.unomaha.edu/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://auth.unomaha.edu/idp</option>
		<option value="https://auth.yale.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://auth.yale.edu/idp/shibboleth</option>
		<option value="https://auth-cobia.siu.edu/auth/realms/siu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://auth-cobia.siu.edu/auth/realms/siu</option>
		<option value="https://authentic.txstate.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://authentic.txstate.edu/idp/shibboleth</option>
		<option value="https://authentication.ubc.ca" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://authentication.ubc.ca</option>
		<option value="https://authidp.shsu.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://authidp.shsu.edu/idp/shibboleth</option>
		<option value="https://auth-incommon.siu.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://auth-incommon.siu.edu</option>
		<option value="https://awsanubis.ringling.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://awsanubis.ringling.edu/idp/shibboleth</option>
		<option value="https://bertrix.usaintlouis.be/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://bertrix.usaintlouis.be/idp/shibboleth</option>
		<option value="https://birk.wayf.dk/birk.php/sso.sdu.dk/wayf" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://birk.wayf.dk/birk.php/sso.sdu.dk/wayf</option>
		<option value="https://caneid.miami.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://caneid.miami.edu/idp/shibboleth</option>
		<option value="https://cas.byu.edu/cas/idp/metadata" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://cas.byu.edu/cas/idp/metadata</option>
		<option value="https://cas.cbs.dk/saml/saml2/idp/metadata.php" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://cas.cbs.dk/saml/saml2/idp/metadata.php</option>
		<option value="https://cas.cgcent.miami.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://cas.cgcent.miami.edu/idp/shibboleth</option>
		<option value="https://cas.conncoll.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://cas.conncoll.edu/idp/shibboleth</option>
		<option value="https://cas.kumc.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://cas.kumc.edu/idp/shibboleth</option>
		<option value="https://certify.skidmore.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://certify.skidmore.edu/idp/shibboleth</option>
		<option value="https://cma-shibboleth.csum.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://cma-shibboleth.csum.edu/idp/shibboleth</option>
		<option value="https://coreen-idp.kreonet.net/idp/simplesamlphp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://coreen-idp.kreonet.net/idp/simplesamlphp</option>
		<option value="https://csupidp.csupueblo.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://csupidp.csupueblo.edu/idp/shibboleth</option>
		<option value="https://cumin.plu.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://cumin.plu.edu/idp/shibboleth</option>
		<option value="https://dfnaai.charite.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://dfnaai.charite.de/idp/shibboleth</option>
		<option value="https://discovery.omren.om/simplesaml/saml2/idp/metadata.php" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://discovery.omren.om/simplesaml/saml2/idp/metadata.php</option>
		<option value="https://dkfzshib.inet.dkfz-heidelberg.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://dkfzshib.inet.dkfz-heidelberg.de/idp/shibboleth</option>
		<option value="https://duo.emerson.edu/dag/saml2/idp/metadata.php" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://duo.emerson.edu/dag/saml2/idp/metadata.php</option>
		<option value="https://duo.famu.edu/dag/saml2/idp/metadata.php" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://duo.famu.edu/dag/saml2/idp/metadata.php</option>
		<option value="https://edugain-proxy.igtf.net/simplesaml/saml2/idp/metadata.php" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://edugain-proxy.igtf.net/simplesaml/saml2/idp/metadata.php</option>
		<option value="https://eduid.ch/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://eduid.ch/idp/shibboleth</option>
		<option value="https://eduid.prigo.cz/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://eduid.prigo.cz/idp/shibboleth</option>
		<option value="https://eidp.llnl.gov" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://eidp.llnl.gov</option>
		<option value="https://enterprise.login.utexas.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://enterprise.login.utexas.edu/idp/shibboleth</option>
		<option value="https://falconidp.uwrf.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://falconidp.uwrf.edu/idp/shibboleth</option>
		<option value="https://fca-caf.uottawa.ca/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://fca-caf.uottawa.ca/idp</option>
		<option value="https://fed.huit.harvard.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://fed.huit.harvard.edu/idp/shibboleth</option>
		<option value="https://fed.nebraska.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://fed.nebraska.edu/idp/shibboleth</option>
		<option value="https://fedauth.colorado.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://fedauth.colorado.edu/idp/shibboleth</option>
		<option value="https://fedcnam.cnam.fr/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://fedcnam.cnam.fr/idp/shibboleth</option>
		<option value="https://federation.ens.psl.eu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://federation.ens.psl.eu/idp/shibboleth</option>
		<option value="https://federation.sydney.edu.au/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://federation.sydney.edu.au/idp/shibboleth</option>
		<option value="https://federation.unimes.fr/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://federation.unimes.fr/idp/shibboleth</option>
		<option value="https://federation-identite.univ-paris13.fr/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://federation-identite.univ-paris13.fr/idp/shibboleth</option>
		<option value="https://fedi.ku.lt/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://fedi.ku.lt/idp/shibboleth</option>
		<option value="https://fedidp.bcm.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://fedidp.bcm.edu/idp/shibboleth</option>
		<option value="https://fedidp.uh.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://fedidp.uh.edu/idp/shibboleth</option>
		<option value="https://fed-uat.it.northwestern.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://fed-uat.it.northwestern.edu/idp/shibboleth</option>
		<option value="https://fim.temple.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://fim.temple.edu/idp/shibboleth</option>
		<option value="https://fiuidp.fiu.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://fiuidp.fiu.edu/idp/shibboleth</option>
		<option value="https://fs.tti.tamu.edu/adfs/services/trust" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://fs.tti.tamu.edu/adfs/services/trust</option>
		<option value="https://hartnell.edu/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://hartnell.edu/idp</option>
		<option value="https://hkafidp.hku.hk/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://hkafidp.hku.hk/idp/shibboleth</option>
		<option value="https://hosted-login.tuakiri.ac.nz/hosting/malaghan.org.nz/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://hosted-login.tuakiri.ac.nz/hosting/malaghan.org.nz/idp/shibboleth</option>
		<option value="https://hosted-login.tuakiri.ac.nz/hosting/reannz.co.nz/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://hosted-login.tuakiri.ac.nz/hosting/reannz.co.nz/idp/shibboleth</option>
		<option value="https://hub.mta.hu/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://hub.mta.hu/idp</option>
		<option value="https://huc.idp.knaw.nl/simplesaml/saml2/idp/metadata.php" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://huc.idp.knaw.nl/simplesaml/saml2/idp/metadata.php</option>
		<option value="https://iam.kiom.re.kr/idp/simplesamlphp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://iam.kiom.re.kr/idp/simplesamlphp</option>
		<option value="https://iam.kiost.ac.kr/idp/simplesamlphp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://iam.kiost.ac.kr/idp/simplesamlphp</option>
		<option value="https://iam.kisti.re.kr/idp/simplesamlphp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://iam.kisti.re.kr/idp/simplesamlphp</option>
		<option value="https://iam.kmu.ac.kr/idp/simplesamlphp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://iam.kmu.ac.kr/idp/simplesamlphp</option>
		<option value="https://iam.knou.ac.kr/idp/simplesamlphp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://iam.knou.ac.kr/idp/simplesamlphp</option>
		<option value="https://iam.kribb.re.kr/idp/simplesamlphp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://iam.kribb.re.kr/idp/simplesamlphp</option>
		<option value="https://iam.kriso.re.kr/idp/simplesamlphp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://iam.kriso.re.kr/idp/simplesamlphp</option>
		<option value="https://iam.nnfc.re.kr/idp/simplesamlphp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://iam.nnfc.re.kr/idp/simplesamlphp</option>
		<option value="https://iam.stepi.re.kr/idp/simplesamlphp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://iam.stepi.re.kr/idp/simplesamlphp</option>
		<option value="https://icarus.sdstate.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://icarus.sdstate.edu/idp/shibboleth</option>
		<option value="https://icidp.osrhe.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://icidp.osrhe.edu/idp/shibboleth</option>
		<option value="https://id.ecoledulouvre.fr/simplesaml/saml2/idp/metadata.php" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://id.ecoledulouvre.fr/simplesaml/saml2/idp/metadata.php</option>
		<option value="https://id.ku.dk/nidp/saml2/metadata" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://id.ku.dk/nidp/saml2/metadata</option>
		<option value="https://id.nps.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://id.nps.edu/idp/shibboleth</option>
		<option value="https://id.tecnico.ulisboa.pt/saml" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://id.tecnico.ulisboa.pt/saml</option>
		<option value="https://id.uakron.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://id.uakron.edu/idp/shibboleth</option>
		<option value="https://id.viko.lt/auth/saml2/idp/metadata.php" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://id.viko.lt/auth/saml2/idp/metadata.php</option>
		<option value="https://idcs-6dfbdd810afa4d509f6cfc191d612acd.identity.oraclecloud.com:443/fed" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idcs-6dfbdd810afa4d509f6cfc191d612acd.identity.oraclecloud.com:443/fed</option>
		<option value="https://idem.ced.inaf.it/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idem.ced.inaf.it/idp/shibboleth</option>
		<option value="https://idem.polito.it/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idem.polito.it/idp/shibboleth</option>
		<option value="https://identity.colgate.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://identity.colgate.edu/idp/shibboleth</option>
		<option value="https://identity.gettysburg.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://identity.gettysburg.edu/idp/shibboleth</option>
		<option value="https://identity.hmc.edu/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://identity.hmc.edu/idp</option>
		<option value="https://identity.research.gov/sso" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://identity.research.gov/sso</option>
		<option value="https://identity.ugent.be/simplesaml/saml2/idp/metadata.php" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://identity.ugent.be/simplesaml/saml2/idp/metadata.php</option>
		<option value="https://identity.unamur.be/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://identity.unamur.be/idp/shibboleth</option>
		<option value="https://identityprovider.anl.gov/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://identityprovider.anl.gov/idp/shibboleth</option>
		<option value="https://idp.aalto.fi/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.aalto.fi/idp/shibboleth</option>
		<option value="https://idp.acad-ciencias.pt/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.acad-ciencias.pt/idp/shibboleth</option>
		<option value="https://idp.actorscentreaustralia.com.au/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.actorscentreaustralia.com.au/idp/shibboleth</option>
		<option value="https://idp.admin.grnet.gr/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.admin.grnet.gr/idp/shibboleth</option>
		<option value="https://idp.agreenium.fr/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.agreenium.fr/idp</option>
		<option value="https://idp.agresearch.co.nz/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.agresearch.co.nz/idp/shibboleth</option>
		<option value="https://idp.alliancecan.ca/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.alliancecan.ca/idp/shibboleth</option>
		<option value="https://idp.american.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.american.edu/idp/shibboleth</option>
		<option value="https://idp.ameslab.gov/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.ameslab.gov/idp/shibboleth</option>
		<option value="https://idp.ap-hm.fr/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.ap-hm.fr/idp/shibboleth</option>
		<option value="https://idp.apu.edu/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.apu.edu/shibboleth</option>
		<option value="https://idp.aub.edu.lb/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.aub.edu.lb/idp/shibboleth</option>
		<option value="https://idp.aut.ac.nz/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.aut.ac.nz/idp/shibboleth</option>
		<option value="https://idp.bham.ac.uk/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.bham.ac.uk/shibboleth</option>
		<option value="https://idp.biochem.mpg.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.biochem.mpg.de/idp/shibboleth</option>
		<option value="https://idp.bnl.gov/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.bnl.gov/idp/shibboleth</option>
		<option value="https://idp.boisestate.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.boisestate.edu/idp/shibboleth</option>
		<option value="https://idp.bridgeport.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.bridgeport.edu/idp/shibboleth</option>
		<option value="https://idp.brynmawr.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.brynmawr.edu/idp/shibboleth</option>
		<option value="https://idp.calpoly.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.calpoly.edu/idp/shibboleth</option>
		<option value="https://idp.caltech.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.caltech.edu/idp/shibboleth</option>
		<option value="https://idp.canarie.ca/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.canarie.ca/idp/shibboleth</option>
		<option value="https://idp.cardiff.ac.uk/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.cardiff.ac.uk/shibboleth</option>
		<option value="https://idp.caudit.edu.au/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.caudit.edu.au/idp/shibboleth</option>
		<option value="https://idp.cc.binghamton.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.cc.binghamton.edu/idp/shibboleth</option>
		<option value="https://idp.cc.swin.edu.au/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.cc.swin.edu.au/idp/shibboleth</option>
		<option value="https://idp.chapman.edu/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.chapman.edu/idp</option>
		<option value="https://idp.chop.edu/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.chop.edu/idp</option>
		<option value="https://idp.cing.ac.cy/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.cing.ac.cy/idp/shibboleth</option>
		<option value="https://idp.cirrusidentity.com/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.cirrusidentity.com/idp</option>
		<option value="https://idp.citruscollege.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.citruscollege.edu/idp/shibboleth</option>
		<option value="https://idp.clarion.edu/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.clarion.edu/idp</option>
		<option value="https://idp.cloud.unizin.org/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.cloud.unizin.org/idp/shibboleth</option>
		<option value="https://idp.cmccd.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.cmccd.edu/idp/shibboleth</option>
		<option value="https://idp.computecanada.ca/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.computecanada.ca/idp/shibboleth</option>
		<option value="https://idp.cos.edu/" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.cos.edu/</option>
		<option value="https://idp.cpp.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.cpp.edu/idp/shibboleth</option>
		<option value="https://idp.cpsp.edu.pk/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.cpsp.edu.pk/idp/shibboleth</option>
		<option value="https://idp.csc.fi/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.csc.fi/idp/shibboleth</option>
		<option value="https://idp.csudh.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.csudh.edu/idp/shibboleth</option>
		<option value="https://idp.csus.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.csus.edu/idp/shibboleth</option>
		<option value="https://idp.csusb.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.csusb.edu/idp/shibboleth</option>
		<option value="https://idp.csusm.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.csusm.edu/idp/shibboleth</option>
		<option value="https://idp.csustan.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.csustan.edu/idp/shibboleth</option>
		<option value="https://idp.cut.ac.cy/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.cut.ac.cy/idp/shibboleth</option>
		<option value="https://idp.cwu.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.cwu.edu/idp/shibboleth</option>
		<option value="https://idp.desy.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.desy.de/idp/shibboleth</option>
		<option value="https://idp.dfn.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.dfn.de/idp/shibboleth</option>
		<option value="https://idp.dfn-cert.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.dfn-cert.de/idp/shibboleth</option>
		<option value="https://idp.dias.ie/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.dias.ie/idp/shibboleth</option>
		<option value="https://idp.dir.garr.it/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.dir.garr.it/idp/shibboleth</option>
		<option value="https://idp.dit.ie/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.dit.ie/idp/shibboleth</option>
		<option value="https://idp.dkrz.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.dkrz.de/idp/shibboleth</option>
		<option value="https://idp.dsm.museum/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.dsm.museum/idp/shibboleth</option>
		<option value="https://idp.du.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.du.edu/idp/shibboleth</option>
		<option value="https://idp.dundee.ac.uk/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.dundee.ac.uk/shibboleth</option>
		<option value="https://idp.duq.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.duq.edu/idp/shibboleth</option>
		<option value="https://idp.ebi.ac.uk/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.ebi.ac.uk/idp/shibboleth</option>
		<option value="https://idp.ed.ac.uk/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.ed.ac.uk/shibboleth</option>
		<option value="https://idp.educause.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.educause.edu/idp/shibboleth</option>
		<option value="https://idp.eduid.hu/kifuteszt.sulinet.hu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.eduid.hu/kifuteszt.sulinet.hu</option>
		<option value="https://idp.eduid.lk/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.eduid.lk/idp/shibboleth</option>
		<option value="https://idp.ego-gw.it/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.ego-gw.it/idp/shibboleth</option>
		<option value="https://idp.elon.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.elon.edu/idp/shibboleth</option>
		<option value="https://idp.emse.fr/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.emse.fr/idp/shibboleth</option>
		<option value="https://idp.enpc.fr/saml/metadata" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.enpc.fr/saml/metadata</option>
		<option value="https://idp.ens2m.fr/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.ens2m.fr/idp/shibboleth</option>
		<option value="https://idp.ensae.fr/saml2/idp/metadata.php" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.ensae.fr/saml2/idp/metadata.php</option>
		<option value="https://idp.epfl.ch/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.epfl.ch/idp/shibboleth</option>
		<option value="https://idp.epita.fr/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.epita.fr/idp/shibboleth</option>
		<option value="https://idp.es.net/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.es.net/idp/shibboleth</option>
		<option value="https://idp.esigelec.fr/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.esigelec.fr/idp/shibboleth</option>
		<option value="https://idp.esme.fr/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.esme.fr/idp/shibboleth</option>
		<option value="https://idp.eso.org/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.eso.org/idp/shibboleth</option>
		<option value="https://idp.eup.edinboro.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.eup.edinboro.edu/idp/shibboleth</option>
		<option value="https://idp.famu.edu:443/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.famu.edu:443/idp/shibboleth</option>
		<option value="https://idp.fccn.pt/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.fccn.pt/idp/shibboleth</option>
		<option value="https://idp.fct.pt/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.fct.pt/idp/shibboleth</option>
		<option value="https://idp.fdu.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.fdu.edu/idp/shibboleth</option>
		<option value="https://idp.fhi-berlin.mpg.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.fhi-berlin.mpg.de/idp/shibboleth</option>
		<option value="https://idp.fh-trier.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.fh-trier.de/idp/shibboleth</option>
		<option value="https://idp.fnal.gov/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.fnal.gov/idp/shibboleth</option>
		<option value="https://idp.fraunhofer.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.fraunhofer.de/idp/shibboleth</option>
		<option value="https://idp.frederick.ac.cy/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.frederick.ac.cy/idp/shibboleth</option>
		<option value="https://idp.fsu.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.fsu.edu</option>
		<option value="https://idp.gatech.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.gatech.edu/idp/shibboleth</option>
		<option value="https://idp.getinclusive.com/simplesaml/saml2/idp/metadata.php" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.getinclusive.com/simplesaml/saml2/idp/metadata.php</option>
		<option value="https://idp.getty.edu/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.getty.edu/idp</option>
		<option value="https://idp.giga-hamburg.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.giga-hamburg.de/idp/shibboleth</option>
		<option value="https://idp.gla.ac.uk/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.gla.ac.uk/shibboleth</option>
		<option value="https://idp.gmit.ie/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.gmit.ie/idp/shibboleth</option>
		<option value="https://idp.greatplains.net" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.greatplains.net</option>
		<option value="https://idp.grid.arn.dz/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.grid.arn.dz/idp/shibboleth</option>
		<option value="https://idp.grinnell.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.grinnell.edu/idp/shibboleth</option>
		<option value="https://idp.gsu.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.gsu.edu/idp/shibboleth</option>
		<option value="https://idp.haverford.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.haverford.edu/idp/shibboleth</option>
		<option value="https://idp.hawaii.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.hawaii.edu/idp/shibboleth</option>
		<option value="https://idp.hdm-stuttgart.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.hdm-stuttgart.de/idp/shibboleth</option>
		<option value="https://idp.heanet.ie/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.heanet.ie/idp/shibboleth</option>
		<option value="https://idp.hec.gov.pk/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.hec.gov.pk/idp/shibboleth</option>
		<option value="https://idp.helmholtz.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.helmholtz.de/idp/shibboleth</option>
		<option value="https://idp.helmholtz-berlin.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.helmholtz-berlin.de/idp/shibboleth</option>
		<option value="https://idp.hh.se/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.hh.se/idp/shibboleth</option>
		<option value="https://idp.hkr.se/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.hkr.se/idp/shibboleth</option>
		<option value="https://idp.hs-bremerhaven.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.hs-bremerhaven.de/idp/shibboleth</option>
		<option value="https://idp.hs-esslingen.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.hs-esslingen.de/idp/shibboleth</option>
		<option value="https://idp.hs-karlsruhe.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.hs-karlsruhe.de/idp/shibboleth</option>
		<option value="https://idp.hs-wismar.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.hs-wismar.de/idp/shibboleth</option>
		<option value="https://idp.huc.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.huc.edu/idp/shibboleth</option>
		<option value="https://idp.hzdr.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.hzdr.de/idp/shibboleth</option>
		<option value="https://idp.ias.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.ias.edu/idp/shibboleth</option>
		<option value="https://idp.iastate.edu/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.iastate.edu/shibboleth</option>
		<option value="https://idp.icm-institute.org/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.icm-institute.org/idp/shibboleth</option>
		<option value="https://idp.iit.edu/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.iit.edu/idp</option>
		<option value="https://idp.incommonfederation.org/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.incommonfederation.org/idp/shibboleth</option>
		<option value="https://idp.inesctec.pt/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.inesctec.pt/idp/shibboleth</option>
		<option value="https://idp.infn.it/saml2/idp/metadata.php" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.infn.it/saml2/idp/metadata.php</option>
		<option value="https://idp.inp-greifswald.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.inp-greifswald.de/idp/shibboleth</option>
		<option value="https://idp.inra.fr/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.inra.fr/idp/shibboleth</option>
		<option value="https://idp.inrim.it/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.inrim.it/idp/shibboleth</option>
		<option value="https://idp.ipsa.fr/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.ipsa.fr/idp/shibboleth</option>
		<option value="https://idp.ipu-berlin.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.ipu-berlin.de/idp/shibboleth</option>
		<option value="https://idp.ist.ac.at/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.ist.ac.at/idp/shibboleth</option>
		<option value="https://idp.it.su.se/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.it.su.se/idp/shibboleth</option>
		<option value="https://idp.its.fz-juelich.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.its.fz-juelich.de/idp/shibboleth</option>
		<option value="https://idp.itum.mrt.ac.lk/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.itum.mrt.ac.lk/idp/shibboleth</option>
		<option value="https://idp.iub.edu.pk/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.iub.edu.pk/idp/shibboleth</option>
		<option value="https://idp.iwm-tuebingen.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.iwm-tuebingen.de/idp/shibboleth</option>
		<option value="https://idp.jefferson.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.jefferson.edu/idp/shibboleth</option>
		<option value="https://idp.jisc.ac.uk/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.jisc.ac.uk/idp/shibboleth</option>
		<option value="https://idp.kigam.re.kr/idp/simplesamlphp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.kigam.re.kr/idp/simplesamlphp</option>
		<option value="https://idp.kln.ac.lk/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.kln.ac.lk/idp/shibboleth</option>
		<option value="https://idp.kutztown.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.kutztown.edu/idp/shibboleth</option>
		<option value="https://idp.lboro.ac.uk/simplesaml/saml2/idp/metadata.php" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.lboro.ac.uk/simplesaml/saml2/idp/metadata.php</option>
		<option value="https://idp.learn.ac.lk/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.learn.ac.lk/idp/shibboleth</option>
		<option value="https://idp.lhup.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.lhup.edu/idp/shibboleth</option>
		<option value="https://idp.ligo-india.in/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.ligo-india.in/idp/shibboleth</option>
		<option value="https://idp.lincoln.ac.nz/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.lincoln.ac.nz/idp/shibboleth</option>
		<option value="https://idp.linea.gov.br/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.linea.gov.br/idp/shibboleth</option>
		<option value="https://idp.login.iu.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.login.iu.edu/idp/shibboleth</option>
		<option value="https://idp.louisville.edu/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.louisville.edu/idp</option>
		<option value="https://idp.lrz.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.lrz.de/idp/shibboleth</option>
		<option value="https://idp.lsuhs.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.lsuhs.edu</option>
		<option value="https://idp.ltcc.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.ltcc.edu/idp/shibboleth</option>
		<option value="https://idp.ltu.se/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.ltu.se/idp/shibboleth</option>
		<option value="https://idp.maeen.sa/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.maeen.sa/idp/shibboleth</option>
		<option value="https://idp.maine.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.maine.edu/idp/shibboleth</option>
		<option value="https://idp.marquette.edu/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.marquette.edu/idp</option>
		<option value="https://idp.marseille.archi.fr/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.marseille.archi.fr/idp/shibboleth</option>
		<option value="https://idp.marshall.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.marshall.edu/idp/shibboleth</option>
		<option value="https://idp.mbl.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.mbl.edu/idp/shibboleth</option>
		<option value="https://idp.merit.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.merit.edu</option>
		<option value="https://idp.mica.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.mica.edu/idp/shibboleth</option>
		<option value="https://idp.mines.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.mines.edu/idp/shibboleth</option>
		<option value="https://idp.miracosta.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.miracosta.edu/idp/shibboleth</option>
		<option value="https://idp.monash.edu.au/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.monash.edu.au/idp/shibboleth</option>
		<option value="https://idp.morgan.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.morgan.edu/idp/shibboleth</option>
		<option value="https://idp.mtsac.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.mtsac.edu/idp/shibboleth</option>
		<option value="https://idp.murdoch.edu.au/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.murdoch.edu.au/idp/shibboleth</option>
		<option value="https://idp.nantes.archi.fr/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.nantes.archi.fr/idp/shibboleth</option>
		<option value="https://idp.nbu.cz/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.nbu.cz/idp/shibboleth</option>
		<option value="https://idp.nccu.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.nccu.edu/idp/shibboleth</option>
		<option value="https://idp.ncsa.illinois.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.ncsa.illinois.edu/idp/shibboleth</option>
		<option value="https://idp.ndsu.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.ndsu.edu/idp/shibboleth</option>
		<option value="https://idp.neduet.edu.pk/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.neduet.edu.pk/idp/shibboleth</option>
		<option value="https://idp.newcastle.edu.au/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.newcastle.edu.au/idp/shibboleth</option>
		<option value="https://idp.niif.hu/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.niif.hu/shibboleth</option>
		<option value="https://idp.niu.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.niu.edu/idp/shibboleth</option>
		<option value="https://idp.nss.udel.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.nss.udel.edu/idp/shibboleth</option>
		<option value="https://idp.oar.net/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.oar.net/idp/shibboleth</option>
		<option value="https://idp.ohsu.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.ohsu.edu/idp/shibboleth</option>
		<option value="https://idp.oh-tech.org/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.oh-tech.org/idp/shibboleth</option>
		<option value="https://idp.okstate.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.okstate.edu/idp/shibboleth</option>
		<option value="https://idp.omren.om/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.omren.om/idp</option>
		<option value="https://idp.onecampus.com/saml" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.onecampus.com/saml</option>
		<option value="https://idp.ornl.gov/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.ornl.gov/idp</option>
		<option value="https://idp.osc.edu/auth/realms/osc" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.osc.edu/auth/realms/osc</option>
		<option value="https://idp.otago.ac.nz/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.otago.ac.nz/idp/shibboleth</option>
		<option value="https://idp.pasteur.fr/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.pasteur.fr/idp/shibboleth</option>
		<option value="https://idp.pct.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.pct.edu/idp/shibboleth</option>
		<option value="https://idp.pennkey.upenn.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.pennkey.upenn.edu/idp/shibboleth</option>
		<option value="https://idp.ph-freiburg.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.ph-freiburg.de/idp/shibboleth</option>
		<option value="https://idp.pima.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.pima.edu/idp/shibboleth</option>
		<option value="https://idp.plantandfood.co.nz/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.plantandfood.co.nz/idp/shibboleth</option>
		<option value="https://idp.princeton.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.princeton.edu/idp/shibboleth</option>
		<option value="https://idp.pub.ro/saml2/idp/metadata.php" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.pub.ro/saml2/idp/metadata.php</option>
		<option value="https://idp.pugetsound.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.pugetsound.edu/idp/shibboleth</option>
		<option value="https://idp.purdue.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.purdue.edu/idp/shibboleth</option>
		<option value="https://idp.qatar-weill.cornell.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.qatar-weill.cornell.edu/idp/shibboleth</option>
		<option value="https://idp.qut.edu.au/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.qut.edu.au/idp/shibboleth</option>
		<option value="https://idp.radford.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.radford.edu/idp/shibboleth</option>
		<option value="https://idp.rcpi.ie/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.rcpi.ie/idp/shibboleth</option>
		<option value="https://idp.reed.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.reed.edu/idp/shibboleth</option>
		<option value="https://idp.rice.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.rice.edu/idp/shibboleth</option>
		<option value="https://idp.rnp.br/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.rnp.br/idp/shibboleth</option>
		<option value="https://idp.roedu.net/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.roedu.net/idp/shibboleth</option>
		<option value="https://idp.rrz.uni-koeln.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.rrz.uni-koeln.de/idp/shibboleth</option>
		<option value="https://idp.sarh.om/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.sarh.om/idp</option>
		<option value="https://idp.sbcc.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.sbcc.edu/idp/shibboleth</option>
		<option value="https://idp.sbccd.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.sbccd.edu</option>
		<option value="https://idp.scc.kit.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.scc.kit.edu/idp/shibboleth</option>
		<option value="https://idp.scccd.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.scccd.edu/idp/shibboleth</option>
		<option value="https://idp.sdcc.bnl.gov/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.sdcc.bnl.gov/idp</option>
		<option value="https://idp.sdsu.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.sdsu.edu/idp/shibboleth</option>
		<option value="https://idp.sfsu.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.sfsu.edu/idp/shibboleth</option>
		<option value="https://idp.sfu.ca/entity" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.sfu.ca/entity</option>
		<option value="https://idp.shibboleth.ttu.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.shibboleth.ttu.edu/idp/shibboleth</option>
		<option value="https://idp.ship.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.ship.edu/idp/shibboleth</option>
		<option value="https://idp.shom.fr/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.shom.fr/idp</option>
		<option value="https://idp.si.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.si.edu/idp/shibboleth</option>
		<option value="https://idp.sigma-clermont.fr/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.sigma-clermont.fr/idp/shibboleth</option>
		<option value="https://idp.simmons.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.simmons.edu/idp/shibboleth</option>
		<option value="https://idp.sissa.it/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.sissa.it/idp/shibboleth</option>
		<option value="https://idp.smu.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.smu.edu/idp/shibboleth</option>
		<option value="https://idp.srecarilionclinic.org/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.srecarilionclinic.org/idp/shibboleth</option>
		<option value="https://idp.sssup.it/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.sssup.it/idp/shibboleth</option>
		<option value="https://idp.st-andrews.ac.uk/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.st-andrews.ac.uk/shibboleth</option>
		<option value="https://idp.sulross.edu/simplesaml/saml2/idp/metadata.php" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.sulross.edu/simplesaml/saml2/idp/metadata.php</option>
		<option value="https://idp.supbiotech.fr/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.supbiotech.fr/idp/shibboleth</option>
		<option value="https://idp.symplicity.com/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.symplicity.com/idp/shibboleth</option>
		<option value="https://idp.tacc.utexas.edu/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.tacc.utexas.edu/idp</option>
		<option value="https://idp.tamucc.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.tamucc.edu/idp/shibboleth</option>
		<option value="https://idp.tamusa.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.tamusa.edu/idp/shibboleth</option>
		<option value="https://idp.tcu.edu/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.tcu.edu/idp</option>
		<option value="https://idp.touro.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.touro.edu/idp/shibboleth</option>
		<option value="https://idp.tudublin.ie/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.tudublin.ie/idp/shibboleth</option>
		<option value="https://idp.tulane.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.tulane.edu/idp/shibboleth</option>
		<option value="https://idp.ua.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.ua.edu/idp/shibboleth</option>
		<option value="https://idp.uaic.ro/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.uaic.ro/idp/shibboleth</option>
		<option value="https://idp.uaic.ro/simplesaml/saml2/idp/metadata.php" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.uaic.ro/simplesaml/saml2/idp/metadata.php</option>
		<option value="https://idp.uark.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.uark.edu/idp/shibboleth</option>
		<option value="https://idp.ub.ro/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.ub.ro/idp/shibboleth</option>
		<option value="https://idp.ubalt.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.ubalt.edu/idp/shibboleth</option>
		<option value="https://idp.uca.fr/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.uca.fr/idp/shibboleth</option>
		<option value="https://idp.uclouvain.be/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.uclouvain.be/idp/shibboleth</option>
		<option value="https://idp.ucy.ac.cy/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.ucy.ac.cy/idp/shibboleth</option>
		<option value="https://idp.uhd.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.uhd.edu/idp/shibboleth</option>
		<option value="https://idp.ulb.ac.be/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.ulb.ac.be/idp/shibboleth</option>
		<option value="https://idp.umassd.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.umassd.edu/idp/shibboleth</option>
		<option value="https://idp.une.edu.au/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.une.edu.au/idp/shibboleth</option>
		<option value="https://idp.uni-bremen.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.uni-bremen.de/idp/shibboleth</option>
		<option value="https://idp.unica.it/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.unica.it/idp/shibboleth</option>
		<option value="https://idp.unical.it/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.unical.it/idp/shibboleth</option>
		<option value="https://idp.unicon.net/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.unicon.net/idp/shibboleth</option>
		<option value="https://idp.uni-duesseldorf.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.uni-duesseldorf.de/idp/shibboleth</option>
		<option value="https://idp.unige.ch/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.unige.ch/idp/shibboleth</option>
		<option value="https://idp.uni-heidelberg.de" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.uni-heidelberg.de</option>
		<option value="https://idp.unimc.it/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.unimc.it/idp/shibboleth</option>
		<option value="https://idp.unimelb.edu.au/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.unimelb.edu.au/idp/shibboleth</option>
		<option value="https://idp.unimore.it/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.unimore.it/idp/shibboleth</option>
		<option value="https://idp.uninettunouniversity.net/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.uninettunouniversity.net/idp/shibboleth</option>
		<option value="https://idp.uni-oldenburg.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.uni-oldenburg.de/idp/shibboleth</option>
		<option value="https://idp.uni-paderborn.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.uni-paderborn.de/idp/shibboleth</option>
		<option value="https://idp.uniparthenope.it/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.uniparthenope.it/idp/shibboleth</option>
		<option value="https://idp.uni-potsdam.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.uni-potsdam.de/idp/shibboleth</option>
		<option value="https://idp.unistra.fr/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.unistra.fr/idp/shibboleth</option>
		<option value="https://idp.uni-stuttgart.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.uni-stuttgart.de/idp/shibboleth</option>
		<option value="https://idp.uni-tuebingen.de/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.uni-tuebingen.de/shibboleth</option>
		<option value="https://idp.uni-ulm.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.uni-ulm.de/idp/shibboleth</option>
		<option value="https://idp.univ-corse.fr/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.univ-corse.fr/idp/shibboleth</option>
		<option value="https://idp.univ-eiffel.fr/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.univ-eiffel.fr/idp/shibboleth</option>
		<option value="https://idp.univ-lemans.fr/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.univ-lemans.fr/idp/shibboleth</option>
		<option value="https://idp.univ-paris13.fr/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.univ-paris13.fr/idp/shibboleth</option>
		<option value="https://idp.univ-tln.fr/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.univ-tln.fr/idp/shibboleth</option>
		<option value="https://idp.uni-wuppertal.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.uni-wuppertal.de/idp/shibboleth</option>
		<option value="https://idp.unmc.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.unmc.edu/idp/shibboleth</option>
		<option value="https://idp.uos.edu.pk/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.uos.edu.pk/idp/shibboleth</option>
		<option value="https://idp.uow.edu.au/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.uow.edu.au/idp/shibboleth</option>
		<option value="https://idp.uprm.edu/saml2/idp/metadata.php" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.uprm.edu/saml2/idp/metadata.php</option>
		<option value="https://idp.u-psud.fr/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.u-psud.fr/idp</option>
		<option value="https://idp.usask.ca/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.usask.ca/idp/shibboleth</option>
		<option value="https://idp.usm.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.usm.edu/idp/shibboleth</option>
		<option value="https://idp.ust.hk/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.ust.hk/idp/shibboleth</option>
		<option value="https://idp.utdallas.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.utdallas.edu/idp/shibboleth</option>
		<option value="https://idp.utk.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.utk.edu/idp/shibboleth</option>
		<option value="https://idp.utmb.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.utmb.edu/idp/shibboleth</option>
		<option value="https://idp.utsystem.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.utsystem.edu/idp/shibboleth</option>
		<option value="https://idp.uttyler.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.uttyler.edu/idp/shibboleth</option>
		<option value="https://idp.uvic.ca/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.uvic.ca/idp/shibboleth</option>
		<option value="https://idp.uvm.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.uvm.edu/idp/shibboleth</option>
		<option value="https://idp.uwa.edu.au/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.uwa.edu.au/idp/shibboleth</option>
		<option value="https://idp.uwaterloo.ca/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.uwaterloo.ca/idp/shibboleth</option>
		<option value="https://idp.uwf.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.uwf.edu/idp/shibboleth</option>
		<option value="https://idp.uwm.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.uwm.edu/idp/shibboleth</option>
		<option value="https://idp.vsb.cz/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.vsb.cz/idp/shibboleth</option>
		<option value="https://idp.vub.ac.be/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.vub.ac.be/idp/shibboleth</option>
		<option value="https://idp.vub.be/idp/sso" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.vub.be/idp/sso</option>
		<option value="https://idp.vuw.ac.nz/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.vuw.ac.nz/idp/shibboleth</option>
		<option value="https://idp.vu-wien.ac.at/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.vu-wien.ac.at/idp/shibboleth</option>
		<option value="https://idp.waikato.ac.nz/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.waikato.ac.nz/idp/shibboleth</option>
		<option value="https://idp.warwick.ac.uk/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.warwick.ac.uk/idp/shibboleth</option>
		<option value="https://idp.weber.edu/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.weber.edu/idp</option>
		<option value="https://idp.wehi.edu.au/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.wehi.edu.au/idp/shibboleth</option>
		<option value="https://idp.whitman.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.whitman.edu/idp/shibboleth</option>
		<option value="https://idp.willamette.edu/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.willamette.edu/idp</option>
		<option value="https://idp.williams.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.williams.edu/idp/shibboleth</option>
		<option value="https://idp.wm.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.wm.edu/idp/shibboleth</option>
		<option value="https://idp.wmich.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.wmich.edu/idp/shibboleth</option>
		<option value="https://idp.wooster.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.wooster.edu/idp/shibboleth</option>
		<option value="https://idp.wpunj.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.wpunj.edu/idp/shibboleth</option>
		<option value="https://idp.wvu.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.wvu.edu/idp/shibboleth</option>
		<option value="https://idp.xsede.org/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.xsede.org/idp/shibboleth</option>
		<option value="https://idp.zid.tuwien.ac.at/saml2" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp.zid.tuwien.ac.at/saml2</option>
		<option value="https://idp01.broadinstitute.org/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp01.broadinstitute.org/idp/shibboleth</option>
		<option value="https://idp01.sjsu.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp01.sjsu.edu/idp/shibboleth</option>
		<option value="https://idp01.stfc.ac.uk/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp01.stfc.ac.uk/shibboleth</option>
		<option value="https://idp1.agroparistech.fr/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp1.agroparistech.fr/idp/shibboleth</option>
		<option value="https://idp1.desy.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp1.desy.de/idp/shibboleth</option>
		<option value="https://idp1.griffith.edu.au/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp1.griffith.edu.au/idp/shibboleth</option>
		<option value="https://idp1.ufz.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp1.ufz.de/idp/shibboleth</option>
		<option value="https://idp2.anu.edu.au/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp2.anu.edu.au/idp/shibboleth</option>
		<option value="https://idp2.bth.se/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp2.bth.se/idp/shibboleth</option>
		<option value="https://idp2.condorcet.be/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp2.condorcet.be/idp/shibboleth</option>
		<option value="https://idp2.dcu.ie/idp/profile/Metadata/SAML" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp2.dcu.ie/idp/profile/Metadata/SAML</option>
		<option value="https://idp2.duf.hu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp2.duf.hu/idp/shibboleth</option>
		<option value="https://idp2.eduhainaut.be/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp2.eduhainaut.be/idp/shibboleth</option>
		<option value="https://idp2.emse.fr/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp2.emse.fr/idp/shibboleth</option>
		<option value="https://idp2.enssib.fr/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp2.enssib.fr/idp/shibboleth</option>
		<option value="https://idp2.hainaut-promsoc.be/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp2.hainaut-promsoc.be/idp/shibboleth</option>
		<option value="https://idp2.ics.muni.cz/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp2.ics.muni.cz/idp/shibboleth</option>
		<option value="https://idp2.jacobs-university.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp2.jacobs-university.de/idp/shibboleth</option>
		<option value="https://idp2.pern.edu.pk/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp2.pern.edu.pk/idp/shibboleth</option>
		<option value="https://idp2.univ-paris8.fr/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp2.univ-paris8.fr/idp/shibboleth</option>
		<option value="https://idp2.unr.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp2.unr.edu/idp/shibboleth</option>
		<option value="https://idp3.hig.se/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp3.hig.se/idp/shibboleth</option>
		<option value="https://idp3.it.gu.se/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp3.it.gu.se/idp/shibboleth</option>
		<option value="https://idpass.postech.ac.kr/idp/simplesamlphp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idpass.postech.ac.kr/idp/simplesamlphp</option>
		<option value="https://idp-co.calstate.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp-co.calstate.edu/idp/shibboleth</option>
		<option value="https://idpdev.bham.ac.uk/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idpdev.bham.ac.uk/idp/shibboleth</option>
		<option value="https://idp-dev.warwick.ac.uk/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp-dev.warwick.ac.uk/idp/shibboleth</option>
		<option value="https://idp-fed.hech.be/simplesaml/saml2/idp/metadata.php" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp-fed.hech.be/simplesaml/saml2/idp/metadata.php</option>
		<option value="https://idp-fed.hers.be/simplesaml/saml2/idp/metadata.php" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp-fed.hers.be/simplesaml/saml2/idp/metadata.php</option>
		<option value="https://idp-fed.uliege.be/simplesaml/saml2/idp/metadata.php" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp-fed.uliege.be/simplesaml/saml2/idp/metadata.php</option>
		<option value="https://idp-ieo.irccs.garr.it/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp-ieo.irccs.garr.it/idp/shibboleth</option>
		<option value="https://idp-lab.martinique.univ-antilles.fr/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp-lab.martinique.univ-antilles.fr/idp/shibboleth</option>
		<option value="https://idp-live.intercollege.ac.cy/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp-live.intercollege.ac.cy/idp/shibboleth</option>
		<option value="https://idp-live.unic.ac.cy/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp-live.unic.ac.cy/idp/shibboleth</option>
		<option value="https://idpp.bcit.ca/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idpp.bcit.ca/idp/shibboleth</option>
		<option value="https://idpp.calstatela.edu/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idpp.calstatela.edu/idp</option>
		<option value="https://idpp1.curtin.edu.au/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idpp1.curtin.edu.au/idp/shibboleth</option>
		<option value="https://idp-prod.cc.ucf.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp-prod.cc.ucf.edu/idp/shibboleth</option>
		<option value="https://idps.ulg.ac.be/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idps.ulg.ac.be/idp/shibboleth</option>
		<option value="https://idp-samlprod3.kennesaw.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp-samlprod3.kennesaw.edu</option>
		<option value="https://idp-shib.wou.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp-shib.wou.edu</option>
		<option value="https://idpshibboleth.irf.se/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idpshibboleth.irf.se/idp/shibboleth</option>
		<option value="https://idptest.ciep.fr/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idptest.ciep.fr/idp/shibboleth</option>
		<option value="https://idp-test.warwick.ac.uk/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp-test.warwick.ac.uk/idp/shibboleth</option>
		<option value="https://idp-ubx.u-bordeaux.fr/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp-ubx.u-bordeaux.fr/idp/shibboleth</option>
		<option value="https://idp-unito-prod.cineca.it/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idp-unito-prod.cineca.it/idp/shibboleth</option>
		<option value="https://idpv3.lu.se/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idpv3.lu.se/idp/shibboleth</option>
		<option value="https://idpv3.univ-amu.fr/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idpv3.univ-amu.fr/idp/shibboleth</option>
		<option value="https://idpv4.lu.se/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idpv4.lu.se/idp/shibboleth</option>
		<option value="https://idpweb1.vu.edu.au/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idpweb1.vu.edu.au/idp/shibboleth</option>
		<option value="https://idpx.ua.ac.be/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idpx.ua.ac.be/idp/shibboleth</option>
		<option value="https://idpz.utorauth.utoronto.ca/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://idpz.utorauth.utoronto.ca/shibboleth</option>
		<option value="https://ids.dgist.ac.kr/idp/simplesamlphp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://ids.dgist.ac.kr/idp/simplesamlphp</option>
		<option value="https://ids.gist.ac.kr/idp/simplesamlphp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://ids.gist.ac.kr/idp/simplesamlphp</option>
		<option value="https://i-id.cea.fr/fed" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://i-id.cea.fr/fed</option>
		<option value="https://iif-ng.iucc.ac.il/sp/saml2/idp/metadata.php" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://iif-ng.iucc.ac.il/sp/saml2/idp/metadata.php</option>
		<option value="https://incommon.coloradomesa.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://incommon.coloradomesa.edu</option>
		<option value="https://incommon.esu.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://incommon.esu.edu/idp/shibboleth</option>
		<option value="https://incommon.sunycnse.com/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://incommon.sunycnse.com/idp/shibboleth</option>
		<option value="https://ism.sso.litnet.lt/auth/saml2/idp/metadata.php" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://ism.sso.litnet.lt/auth/saml2/idp/metadata.php</option>
		<option value="https://its.longwood.edu/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://its.longwood.edu/idp</option>
		<option value="https://its-shib.its.csulb.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://its-shib.its.csulb.edu/idp/shibboleth</option>
		<option value="https://janus.cnrs.fr/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://janus.cnrs.fr/idp</option>
		<option value="https://jidp.jlab.org/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://jidp.jlab.org/idp/shibboleth</option>
		<option value="https://junebug2.mcc.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://junebug2.mcc.edu/idp/shibboleth</option>
		<option value="https://kafe.kaist.ac.kr/idp/simplesamlphp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://kafe.kaist.ac.kr/idp/simplesamlphp</option>
		<option value="https://kafe.kasi.re.kr/idp/simplesamlphp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://kafe.kasi.re.kr/idp/simplesamlphp</option>
		<option value="https://kafe.krict.re.kr/idp/simplesamlphp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://kafe.krict.re.kr/idp/simplesamlphp</option>
		<option value="https://kafe.unist.ac.kr/idp/simplesamlphp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://kafe.unist.ac.kr/idp/simplesamlphp</option>
		<option value="https://kafegw.snu.ac.kr/idp/simplesamlphp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://kafegw.snu.ac.kr/idp/simplesamlphp</option>
		<option value="https://kafeid.cnu.ac.kr/idp/simplesamlphp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://kafeid.cnu.ac.kr/idp/simplesamlphp</option>
		<option value="https://kauko.sso.litnet.lt/auth/saml2/idp/metadata.php" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://kauko.sso.litnet.lt/auth/saml2/idp/metadata.php</option>
		<option value="https://keycloak.tacc.utexas.edu/auth/realms/tacc-ldap" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://keycloak.tacc.utexas.edu/auth/realms/tacc-ldap</option>
		<option value="https://l-aai.sztaki.hu/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://l-aai.sztaki.hu/idp</option>
		<option value="https://lammc.sso.litnet.lt/auth/saml2/idp/metadata.php" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://lammc.sso.litnet.lt/auth/saml2/idp/metadata.php</option>
		<option value="https://libraryidp.iisc.ac.in/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://libraryidp.iisc.ac.in/idp/shibboleth</option>
		<option value="https://lka.sso.litnet.lt/auth/saml2/idp/metadata.php" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://lka.sso.litnet.lt/auth/saml2/idp/metadata.php</option>
		<option value="https://llng-auth.insa-lyon.fr/saml/metadata" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://llng-auth.insa-lyon.fr/saml/metadata</option>
		<option value="https://lmuidp.lrz.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://lmuidp.lrz.de/idp/shibboleth</option>
		<option value="https://login.aaiedu.hr/edugain/saml2/idp/metadata.php" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.aaiedu.hr/edugain/saml2/idp/metadata.php</option>
		<option value="https://login.ace.ac.ug/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.ace.ac.ug/idp/shibboleth</option>
		<option value="https://login.aus.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.aus.edu/idp/shibboleth</option>
		<option value="https://login.auth.gr/saml2/idp/metadata.php" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.auth.gr/saml2/idp/metadata.php</option>
		<option value="https://login.bard.edu/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.bard.edu/idp</option>
		<option value="https://login.bc.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.bc.edu/idp/shibboleth</option>
		<option value="https://login.brockport.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.brockport.edu</option>
		<option value="https://login.cmu.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.cmu.edu/idp/shibboleth</option>
		<option value="https://login.du.edu/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.du.edu/idp</option>
		<option value="https://login.emory.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.emory.edu/idp/shibboleth</option>
		<option value="https://login.helsinki.fi/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.helsinki.fi/shibboleth</option>
		<option value="https://login.hfmt-hamburg.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.hfmt-hamburg.de/idp/shibboleth</option>
		<option value="https://login.iasa.gr/auth/saml2/idp/metadata.php" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.iasa.gr/auth/saml2/idp/metadata.php</option>
		<option value="https://login.icermali.org/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.icermali.org/idp/shibboleth</option>
		<option value="https://login.iceruganda.org/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.iceruganda.org/idp/shibboleth</option>
		<option value="https://login.idp.eduid.se/idp.xml" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.idp.eduid.se/idp.xml</option>
		<option value="https://login.it.liu.se/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.it.liu.se/idp/shibboleth</option>
		<option value="https://login.ithaca.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.ithaca.edu/idp/shibboleth</option>
		<option value="https://login.ki.se/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.ki.se/idp/shibboleth</option>
		<option value="https://login.ktu.lt/simplesaml/saml2/idp/metadata.php" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.ktu.lt/simplesaml/saml2/idp/metadata.php</option>
		<option value="https://login.kvk.lt/simplesaml/saml2/idp/metadata.php" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.kvk.lt/simplesaml/saml2/idp/metadata.php</option>
		<option value="https://login.lemoyne.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.lemoyne.edu</option>
		<option value="https://login.ligo.org/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.ligo.org/idp/shibboleth</option>
		<option value="https://login.montana.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.montana.edu/idp/shibboleth</option>
		<option value="https://login.mruni.eu/sso/saml2/idp/metadata.php" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.mruni.eu/sso/saml2/idp/metadata.php</option>
		<option value="https://login.msjc.edu/sso/" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.msjc.edu/sso/</option>
		<option value="https://login.mtholyoke.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.mtholyoke.edu/idp/shibboleth</option>
		<option value="https://login.nd.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.nd.edu/idp/shibboleth</option>
		<option value="https://login.ntua.gr/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.ntua.gr/idp/shibboleth</option>
		<option value="https://login.nyumc.org/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.nyumc.org/idp/shibboleth</option>
		<option value="https://login.ohlone.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.ohlone.edu/idp/shibboleth</option>
		<option value="https://login.oregonstate.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.oregonstate.edu/idp/shibboleth</option>
		<option value="https://login.queensu.ca/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.queensu.ca/idp/shibboleth</option>
		<option value="https://login.rz.rwth-aachen.de/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.rz.rwth-aachen.de/shibboleth</option>
		<option value="https://login.scu.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.scu.edu/idp/shibboleth</option>
		<option value="https://login.smith.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.smith.edu/idp/shibboleth</option>
		<option value="https://login.sonoma.edu/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.sonoma.edu/shibboleth</option>
		<option value="https://login.stolaf.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.stolaf.edu/idp/shibboleth</option>
		<option value="https://login.ualberta.ca/saml2/idp/metadata.php" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.ualberta.ca/saml2/idp/metadata.php</option>
		<option value="https://login.uc.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.uc.edu/idp/shibboleth</option>
		<option value="https://login.ufl.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.ufl.edu/idp/shibboleth</option>
		<option value="https://login.ufrgs.br/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.ufrgs.br/idp/shibboleth</option>
		<option value="https://login.umt.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.umt.edu/idp/shibboleth</option>
		<option value="https://login.uni-hamburg.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.uni-hamburg.de/idp/shibboleth</option>
		<option value="https://login.unlv.edu/FIM/sps/MyShib/saml20" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.unlv.edu/FIM/sps/MyShib/saml20</option>
		<option value="https://login.uwec.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.uwec.edu/idp/shibboleth</option>
		<option value="https://login.weill.cornell.edu/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.weill.cornell.edu/idp</option>
		<option value="https://login.wisc.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.wisc.edu/idp/shibboleth</option>
		<option value="https://login.wustl.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://login.wustl.edu/idp/shibboleth</option>
		<option value="https://logindev.rowan.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://logindev.rowan.edu</option>
		<option value="https://loginp.fordham.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://loginp.fordham.edu/idp/shibboleth</option>
		<option value="https://logintest.wustl.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://logintest.wustl.edu/idp/shibboleth</option>
		<option value="https://logon.hancockcollege.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://logon.hancockcollege.edu</option>
		<option value="https://lsmu.sso.litnet.lt/auth/saml2/idp/metadata.php" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://lsmu.sso.litnet.lt/auth/saml2/idp/metadata.php</option>
		<option value="https://lsu.sso.litnet.lt/auth/saml2/idp/metadata.php" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://lsu.sso.litnet.lt/auth/saml2/idp/metadata.php</option>
		<option value="https://mamiwata.du.edu/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://mamiwata.du.edu/idp</option>
		<option value="https://marko.sso.litnet.lt/auth/saml2/idp/metadata.php" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://marko.sso.litnet.lt/auth/saml2/idp/metadata.php</option>
		<option value="https://mckinley.csuci.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://mckinley.csuci.edu/idp/shibboleth</option>
		<option value="https://med-idp.arn.dz/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://med-idp.arn.dz/idp/shibboleth</option>
		<option value="https://my.atsu.edu/swPublicSSO/SAML/incommon" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://my.atsu.edu/swPublicSSO/SAML/incommon</option>
		<option value="https://my.edhec.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://my.edhec.edu</option>
		<option value="https://mycomidp.marin.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://mycomidp.marin.edu</option>
		<option value="https://myid.vsc.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://myid.vsc.edu/idp/shibboleth</option>
		<option value="https://myidp.nmsu.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://myidp.nmsu.edu</option>
		<option value="https://mylogin.unh.edu/secureauth74" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://mylogin.unh.edu/secureauth74</option>
		<option value="https://myqlidp.otis.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://myqlidp.otis.edu</option>
		<option value="https://myresearchid.idp.cirrusidentity.com/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://myresearchid.idp.cirrusidentity.com/idp</option>
		<option value="https://namid.fairfield.edu:8443/nidp/saml2/metadata" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://namid.fairfield.edu:8443/nidp/saml2/metadata</option>
		<option value="https://nbi-sso.nbi.ac.uk/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://nbi-sso.nbi.ac.uk/idp/shibboleth</option>
		<option value="https://nerckwshibba.nerc.ac.uk/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://nerckwshibba.nerc.ac.uk/idp/shibboleth</option>
		<option value="https://netid.uwosh.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://netid.uwosh.edu/idp/shibboleth</option>
		<option value="https://neuidmsso.neu.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://neuidmsso.neu.edu/idp/shibboleth</option>
		<option value="https://nup-edgnstd.nup.ac.cy/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://nup-edgnstd.nup.ac.cy/idp/shibboleth</option>
		<option value="https://oneaccess.lehman.edu/CloudAccessManager/RPSTS" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://oneaccess.lehman.edu/CloudAccessManager/RPSTS</option>
		<option value="https://papi.kfki.hu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://papi.kfki.hu/idp/shibboleth</option>
		<option value="https://passport.escience.cn/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://passport.escience.cn/idp/shibboleth</option>
		<option value="https://passport.pitt.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://passport.pitt.edu/idp/shibboleth</option>
		<option value="https://passport.ucdenver.edu/oam/fed" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://passport.ucdenver.edu/oam/fed</option>
		<option value="https://passport-dev.pitt.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://passport-dev.pitt.edu/idp/shibboleth</option>
		<option value="https://peridot.truman.edu/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://peridot.truman.edu/idp</option>
		<option value="https://peridot.truman.edu:8443/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://peridot.truman.edu:8443/idp</option>
		<option value="https://pgsso.cccd.edu/sso" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://pgsso.cccd.edu/sso</option>
		<option value="https://portal.uwsuper.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://portal.uwsuper.edu</option>
		<option value="https://poseidon.springfield.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://poseidon.springfield.edu/idp/shibboleth</option>
		<option value="https://prdidp.uncg.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://prdidp.uncg.edu/idp/shibboleth</option>
		<option value="https://prod-sa.granite.edu/SecureAuth10/" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://prod-sa.granite.edu/SecureAuth10/</option>
		<option value="https://proxy.eduteams.org/proxy" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://proxy.eduteams.org/proxy</option>
		<option value="https://proxy.safire.ac.za/birk.php/googleidp.sanren.ac.za/simplesaml/saml2/idp/metadata.php" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://proxy.safire.ac.za/birk.php/googleidp.sanren.ac.za/simplesaml/saml2/idp/metadata.php</option>
		<option value="https://proxy.safire.ac.za/birk.php/idp-01.tenet.ac.za/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://proxy.safire.ac.za/birk.php/idp-01.tenet.ac.za/idp/shibboleth</option>
		<option value="https://proxy.safire.ac.za/birk.php/saml.uwc.ac.za/simplesaml/saml2/idp/metadata.php" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://proxy.safire.ac.za/birk.php/saml.uwc.ac.za/simplesaml/saml2/idp/metadata.php</option>
		<option value="https://proxy.safire.ac.za/birk.php/srvslsfed001.uct.ac.za/simplesaml/saml2/idp/metadata.php" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://proxy.safire.ac.za/birk.php/srvslsfed001.uct.ac.za/simplesaml/saml2/idp/metadata.php</option>
		<option value="https://qub.ac.uk/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://qub.ac.uk/shibboleth</option>
		<option value="https://rec7login.essec.fr/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://rec7login.essec.fr/idp/shibboleth</option>
		<option value="https://rushib.rockefeller.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://rushib.rockefeller.edu/idp/shibboleth</option>
		<option value="https://sac.ecam.fr/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sac.ecam.fr/idp/shibboleth</option>
		<option value="https://saml.adu.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://saml.adu.edu</option>
		<option value="https://saml.dhbw-stuttgart.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://saml.dhbw-stuttgart.de/idp/shibboleth</option>
		<option value="https://saml.nelnet.net" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://saml.nelnet.net</option>
		<option value="https://saml-idp.wou.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://saml-idp.wou.edu</option>
		<option value="https://scbhvidp1.wncc.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://scbhvidp1.wncc.edu/idp/shibboleth</option>
		<option value="https://secure.stevenson.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://secure.stevenson.edu/idp/shibboleth</option>
		<option value="https://secureauth.plymouth.edu/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://secureauth.plymouth.edu/idp</option>
		<option value="https://share-sso.korea.ac.kr/sso" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://share-sso.korea.ac.kr/sso</option>
		<option value="https://shfed.augusta.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shfed.augusta.edu/idp/shibboleth</option>
		<option value="https://shib.auth.usf.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shib.auth.usf.edu/idp/shibboleth</option>
		<option value="https://shib.bu.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shib.bu.edu/idp/shibboleth</option>
		<option value="https://shib.bucknell.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shib.bucknell.edu/idp/shibboleth</option>
		<option value="https://shib.calu.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shib.calu.edu/idp/shibboleth</option>
		<option value="https://shib.ccbcmd.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shib.ccbcmd.edu/idp/shibboleth</option>
		<option value="https://shib.csub.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shib.csub.edu/idp/shibboleth</option>
		<option value="https://shib.e-science.pl/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shib.e-science.pl/idp/shibboleth</option>
		<option value="https://shib.euc.ac.cy/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shib.euc.ac.cy/idp/shibboleth</option>
		<option value="https://shib.fortlewis.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shib.fortlewis.edu/idp/shibboleth</option>
		<option value="https://shib.is.depaul.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shib.is.depaul.edu/idp/shibboleth</option>
		<option value="https://shib.marymount.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shib.marymount.edu/idp/shibboleth</option>
		<option value="https://shib.mcw.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shib.mcw.edu/idp/shibboleth</option>
		<option value="https://shib.mdanderson.org/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shib.mdanderson.org/idp/shibboleth</option>
		<option value="https://shib.med.cornell.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shib.med.cornell.edu/idp/shibboleth</option>
		<option value="https://shib.ou.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shib.ou.edu/idp/shibboleth</option>
		<option value="https://shib.pwr.edu.pl/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shib.pwr.edu.pl/idp/shibboleth</option>
		<option value="https://shib.sou.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shib.sou.edu/idp/shibboleth</option>
		<option value="https://shib.svc.ulaval.ca/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shib.svc.ulaval.ca/idp/shibboleth</option>
		<option value="https://shib.towson.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shib.towson.edu/idp/shibboleth</option>
		<option value="https://shib.unf.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shib.unf.edu/idp/shibboleth</option>
		<option value="https://shib.uni.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shib.uni.edu/idp/shibboleth</option>
		<option value="https://shib.uni-mainz.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shib.uni-mainz.de/idp/shibboleth</option>
		<option value="https://shib.unl.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shib.unl.edu/idp/shibboleth</option>
		<option value="https://shib.uthscsa.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shib.uthscsa.edu/idp/shibboleth</option>
		<option value="https://shib.uvu.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shib.uvu.edu/idp/shibboleth</option>
		<option value="https://shib.wichita.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shib.wichita.edu/idp/shibboleth</option>
		<option value="https://shib.wit.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shib.wit.edu/idp/shibboleth</option>
		<option value="https://shib.wsc.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shib.wsc.edu/idp/shibboleth</option>
		<option value="https://shib01.vassar.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shib01.vassar.edu/idp/shibboleth</option>
		<option value="https://shib1.coastal.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shib1.coastal.edu/idp/shibboleth</option>
		<option value="https://shib1.univ-nc.nc/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shib1.univ-nc.nc/idp/shibboleth</option>
		<option value="https://shib1.uwplatt.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shib1.uwplatt.edu/idp/shibboleth</option>
		<option value="https://shib2.its.rochester.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shib2.its.rochester.edu/idp/shibboleth</option>
		<option value="https://shib2.swmed.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shib2.swmed.edu/idp/shibboleth</option>
		<option value="https://shib2.unc.nc/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shib2.unc.nc/idp/shibboleth</option>
		<option value="https://shib2.utep.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shib2.utep.edu/idp/shibboleth</option>
		<option value="https://shibb.ensait.fr/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibb.ensait.fr/idp/shibboleth</option>
		<option value="https://shibb.its.appstate.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibb.its.appstate.edu/idp/shibboleth</option>
		<option value="https://shibb.utpb.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibb.utpb.edu/idp/shibboleth</option>
		<option value="https://shibb-ctles.u-pem.fr/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibb-ctles.u-pem.fr/idp/shibboleth</option>
		<option value="https://shibbi.pki.itc.u-tokyo.ac.jp/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibbi.pki.itc.u-tokyo.ac.jp/idp/shibboleth</option>
		<option value="https://shibb-idp.georgetown.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibb-idp.georgetown.edu/idp/shibboleth</option>
		<option value="https://shibbo.tul.cz/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibbo.tul.cz/idp/shibboleth</option>
		<option value="https://shibboleth.aarnet.edu.au/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth.aarnet.edu.au/idp/shibboleth</option>
		<option value="https://shibboleth.aws.eckerd.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth.aws.eckerd.edu/idp/shibboleth</option>
		<option value="https://shibboleth.brandeis.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth.brandeis.edu/idp/shibboleth</option>
		<option value="https://shibboleth.clermont-fd.archi.fr/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth.clermont-fd.archi.fr/idp/shibboleth</option>
		<option value="https://shibboleth.cmich.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth.cmich.edu/idp/shibboleth</option>
		<option value="https://shibboleth.csuchico.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth.csuchico.edu/idp/shibboleth</option>
		<option value="https://shibboleth.csustan.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth.csustan.edu/idp/shibboleth</option>
		<option value="https://shibboleth.ens2m.fr/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth.ens2m.fr/idp/shibboleth</option>
		<option value="https://shibboleth.fullerton.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth.fullerton.edu/idp/shibboleth</option>
		<option value="https://shibboleth.gmu.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth.gmu.edu/idp/shibboleth</option>
		<option value="https://shibboleth.greatplains.net/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth.greatplains.net/idp/shibboleth</option>
		<option value="https://shibboleth.hamilton.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth.hamilton.edu/idp/shibboleth</option>
		<option value="https://shibboleth.ict-toulouse.fr/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth.ict-toulouse.fr/idp/shibboleth</option>
		<option value="https://shibboleth.imperial.ac.uk/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth.imperial.ac.uk/idp/shibboleth</option>
		<option value="https://shibboleth.imperial.ac.uk/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth.imperial.ac.uk/shibboleth</option>
		<option value="https://shibboleth.its.msstate.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth.its.msstate.edu/idp/shibboleth</option>
		<option value="https://shibboleth.lib.uh.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth.lib.uh.edu/idp/shibboleth</option>
		<option value="https://shibboleth.liberty.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth.liberty.edu/idp/shibboleth</option>
		<option value="https://shibboleth.liberty.edu/idpv4" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth.liberty.edu/idpv4</option>
		<option value="https://shibboleth.louisville.edu/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth.louisville.edu/idp</option>
		<option value="https://shibboleth.main.ad.rit.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth.main.ad.rit.edu/idp/shibboleth</option>
		<option value="https://shibboleth.mcgill.ca/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth.mcgill.ca/idp/shibboleth</option>
		<option value="https://shibboleth.mzk.cz/simplesaml/metadata.xml" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth.mzk.cz/simplesaml/metadata.xml</option>
		<option value="https://shibboleth.pace.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth.pace.edu/idp/shibboleth</option>
		<option value="https://shibboleth.rush.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth.rush.edu/idp/shibboleth</option>
		<option value="https://shibboleth.salisbury.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth.salisbury.edu/idp/shibboleth</option>
		<option value="https://shibboleth.trincoll.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth.trincoll.edu/idp/shibboleth</option>
		<option value="https://shibboleth.twu.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth.twu.edu/idp/shibboleth</option>
		<option value="https://shibboleth.uams.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth.uams.edu/idp/shibboleth</option>
		<option value="https://shibboleth.ucalgary.ca/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth.ucalgary.ca/idp/shibboleth</option>
		<option value="https://shibboleth.uchastings.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth.uchastings.edu/idp/shibboleth</option>
		<option value="https://shibboleth.uconn.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth.uconn.edu/idp/shibboleth</option>
		<option value="https://shibboleth.uic.edu/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth.uic.edu/shibboleth</option>
		<option value="https://shibboleth.umich.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth.umich.edu/idp/shibboleth</option>
		<option value="https://shibboleth.uni-bielefeld.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth.uni-bielefeld.de/idp/shibboleth</option>
		<option value="https://shibboleth.univ-grenoble-alpes.fr/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth.univ-grenoble-alpes.fr/idp/shibboleth</option>
		<option value="https://shibboleth.uog.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth.uog.edu/idp/shibboleth</option>
		<option value="https://shibboleth.uoregon.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth.uoregon.edu/idp/shibboleth</option>
		<option value="https://shibboleth.usu.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth.usu.edu/idp/shibboleth</option>
		<option value="https://shibboleth.uwyo.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth.uwyo.edu/idp/shibboleth</option>
		<option value="https://shibboleth.vbc.ac.at/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth.vbc.ac.at/idp/shibboleth</option>
		<option value="https://shibboleth.vcu.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth.vcu.edu/idp/shibboleth</option>
		<option value="https://shibboleth.wesleyan.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth.wesleyan.edu/idp/shibboleth</option>
		<option value="https://shibboleth03.chartes.psl.eu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth03.chartes.psl.eu/idp/shibboleth</option>
		<option value="https://shibboleth-2.baylor.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth-2.baylor.edu/idp/shibboleth</option>
		<option value="https://shibboleth3.obspm.fr/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth3.obspm.fr/idp/shibboleth</option>
		<option value="https://shibboleth-idp.collegenet.com/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth-idp.collegenet.com/idp/shibboleth</option>
		<option value="https://shibboleth-idp.gwdg.de/gwdg/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth-idp.gwdg.de/gwdg/shibboleth</option>
		<option value="https://shibboleth-idp.mpg.de/mpg/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth-idp.mpg.de/mpg/shibboleth</option>
		<option value="https://shibbolethidp.musc.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibbolethidp.musc.edu/idp/shibboleth</option>
		<option value="https://shibboleth-idp.uni-goettingen.de/uni/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth-idp.uni-goettingen.de/uni/shibboleth</option>
		<option value="https://shibboleth-idp.uni-regensburg.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth-idp.uni-regensburg.de/idp/shibboleth</option>
		<option value="https://shibboleth-idp.uni-wuerzburg.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibboleth-idp.uni-wuerzburg.de/idp/shibboleth</option>
		<option value="https://shibidp.amherst.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibidp.amherst.edu/idp/shibboleth</option>
		<option value="https://shib-idp.awi.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shib-idp.awi.de/idp/shibboleth</option>
		<option value="https://shibidp.bates.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibidp.bates.edu/idp/shibboleth</option>
		<option value="https://shibidp.bloomu.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibidp.bloomu.edu/idp/shibboleth</option>
		<option value="https://shibidp.cit.cornell.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibidp.cit.cornell.edu/idp/shibboleth</option>
		<option value="https://shibidp.colostate.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibidp.colostate.edu/idp/shibboleth</option>
		<option value="https://shibidp.ipm.ir/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibidp.ipm.ir/idp/shibboleth</option>
		<option value="https://shib-idp.its.csufresno.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shib-idp.its.csufresno.edu/idp/shibboleth</option>
		<option value="https://shibidp.ku.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibidp.ku.edu/idp/shibboleth</option>
		<option value="https://shibidp.llu.edu/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibidp.llu.edu/idp</option>
		<option value="https://shibidp.luc.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibidp.luc.edu/idp/shibboleth</option>
		<option value="https://shib-idp.rpi.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shib-idp.rpi.edu/idp/shibboleth</option>
		<option value="https://shib-idp.siu.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shib-idp.siu.edu/idp/shibboleth</option>
		<option value="https://shibidp.syr.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibidp.syr.edu/idp/shibboleth</option>
		<option value="https://shib-idp.tufts.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shib-idp.tufts.edu/idp/shibboleth</option>
		<option value="https://shib-idp.ucl.ac.uk/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shib-idp.ucl.ac.uk/shibboleth</option>
		<option value="https://shib-idp.umsystem.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shib-idp.umsystem.edu/idp/shibboleth</option>
		<option value="https://shib-idp.uni-osnabrueck.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shib-idp.uni-osnabrueck.de/idp/shibboleth</option>
		<option value="https://shibidp.utrgv.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibidp.utrgv.edu/idp/shibboleth</option>
		<option value="https://shibidp.uwgb.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibidp.uwgb.edu/idp/shibboleth</option>
		<option value="https://shibidp.uwo.ca/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibidp.uwo.ca/idp/shibboleth</option>
		<option value="https://shibidp.wcupa.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibidp.wcupa.edu/idp/shibboleth</option>
		<option value="https://shibidp.whoi.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibidp.whoi.edu/idp/shibboleth</option>
		<option value="https://shib-idp2.uth.tmc.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shib-idp2.uth.tmc.edu/idp/shibboleth</option>
		<option value="https://shibprodapp.loyola.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibprodapp.loyola.edu/idp/shibboleth</option>
		<option value="https://shibsso.sandiego.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shibsso.sandiego.edu/idp/shibboleth</option>
		<option value="https://shib-uat-idp.ucl.ac.uk/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://shib-uat-idp.ucl.ac.uk/shibboleth</option>
		<option value="https://sid.swarthmore.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sid.swarthmore.edu/idp/shibboleth</option>
		<option value="https://sidp.wwu.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sidp.wwu.edu/idp/shibboleth</option>
		<option value="https://signin.cedarville.edu/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://signin.cedarville.edu/idp</option>
		<option value="https://signin.k-state.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://signin.k-state.edu/idp/shibboleth</option>
		<option value="https://signon.deakin.edu.au/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://signon.deakin.edu.au/idp/shibboleth</option>
		<option value="https://singlesignon.gwu.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://singlesignon.gwu.edu/idp/shibboleth</option>
		<option value="https://smidp.uwstout.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://smidp.uwstout.edu/idp/shibboleth</option>
		<option value="https://sonny.furman.edu/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sonny.furman.edu/idp</option>
		<option value="https://srv-aai01.daad.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://srv-aai01.daad.de/idp/shibboleth</option>
		<option value="https://sso.athena-institute.net/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.athena-institute.net/idp</option>
		<option value="https://sso.augsburg.edu/simplesaml/saml2/idp/metadata.php" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.augsburg.edu/simplesaml/saml2/idp/metadata.php</option>
		<option value="https://sso.bergen.edu/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.bergen.edu/idp</option>
		<option value="https://sso.brown.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.brown.edu/idp/shibboleth</option>
		<option value="https://sso.cc.lehigh.edu/sso/saml2/idp/metadata.php" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.cc.lehigh.edu/sso/saml2/idp/metadata.php</option>
		<option value="https://sso.cc.uga.edu/cas/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.cc.uga.edu/cas/idp</option>
		<option value="https://sso.cccmypath.org/simplesaml/saml2/idp/metadata.php" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.cccmypath.org/simplesaml/saml2/idp/metadata.php</option>
		<option value="https://sso.cnes.fr" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.cnes.fr</option>
		<option value="https://sso.coh.org/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.coh.org/idp</option>
		<option value="https://sso.csumb.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.csumb.edu/idp/shibboleth</option>
		<option value="https://sso.delval.edu/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.delval.edu/idp</option>
		<option value="https://sso.ecu.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.ecu.edu/idp/shibboleth</option>
		<option value="https://sso.edhec.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.edhec.edu/idp/shibboleth</option>
		<option value="https://sso.ewu.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.ewu.edu/idp/shibboleth</option>
		<option value="https://sso.fau.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.fau.edu/idp/shibboleth</option>
		<option value="https://sso.fgcu.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.fgcu.edu/idp/shibboleth</option>
		<option value="https://sso.gac.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.gac.edu/idp/shibboleth</option>
		<option value="https://sso.gc.cuny.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.gc.cuny.edu/idp/shibboleth</option>
		<option value="https://sso.h-da.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.h-da.de/idp/shibboleth</option>
		<option value="https://sso.humboldt.edu/idp/metadata" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.humboldt.edu/idp/metadata</option>
		<option value="https://sso.idm.uni-hannover.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.idm.uni-hannover.de/idp/shibboleth</option>
		<option value="https://sso.it.utsa.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.it.utsa.edu/idp/shibboleth</option>
		<option value="https://sso.kenyon.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.kenyon.edu/idp/shibboleth</option>
		<option value="https://sso.mansfield.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.mansfield.edu/idp/shibboleth</option>
		<option value="https://sso.mcmaster.ca/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.mcmaster.ca/idp/shibboleth</option>
		<option value="https://sso.memphis.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.memphis.edu/idp/shibboleth</option>
		<option value="https://sso.msoe.edu/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.msoe.edu/idp</option>
		<option value="https://sso.mssm.edu/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.mssm.edu/idp</option>
		<option value="https://sso.mtu.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.mtu.edu/idp/shibboleth</option>
		<option value="https://sso.noirlab.edu/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.noirlab.edu/idp</option>
		<option value="https://sso.nygenome.org/auth/" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.nygenome.org/auth/</option>
		<option value="https://sso.nygenome.org/auth/realms/nygenome" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.nygenome.org/auth/realms/nygenome</option>
		<option value="https://sso.oakland.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.oakland.edu/idp/shibboleth</option>
		<option value="https://sso.oktaedu.com/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.oktaedu.com/idp/shibboleth</option>
		<option value="https://sso.pacificu.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.pacificu.edu/idp/shibboleth</option>
		<option value="https://sso.pdx.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.pdx.edu/idp/shibboleth</option>
		<option value="https://sso.sjeccd.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.sjeccd.edu</option>
		<option value="https://sso.tarleton.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.tarleton.edu/idp/shibboleth</option>
		<option value="https://sso.trinity.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.trinity.edu/idp/shibboleth</option>
		<option value="https://sso.tu-bs.de" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.tu-bs.de</option>
		<option value="https://sso.tugraz.at/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.tugraz.at/idp/shibboleth</option>
		<option value="https://sso.tuiasi.ro/auth/realms/TUIASI" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.tuiasi.ro/auth/realms/TUIASI</option>
		<option value="https://sso.uah.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.uah.edu/idp/shibboleth</option>
		<option value="https://sso.ucd.ie/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.ucd.ie/idp/shibboleth</option>
		<option value="https://sso.udmercy.edu/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.udmercy.edu/idp</option>
		<option value="https://sso.umgc.edu/gateway" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.umgc.edu/gateway</option>
		<option value="https://sso.unco.edu/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.unco.edu/idp</option>
		<option value="https://sso.ung.edu/simplesaml2" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.ung.edu/simplesaml2</option>
		<option value="https://sso.union.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.union.edu/idp/shibboleth</option>
		<option value="https://sso.unt.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.unt.edu/idp/shibboleth</option>
		<option value="https://sso.uri.edu/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.uri.edu/idp</option>
		<option value="https://sso.ut.edu/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.ut.edu/idp</option>
		<option value="https://sso.vai.org/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.vai.org/idp</option>
		<option value="https://sso.yc.edu/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso.yc.edu/idp</option>
		<option value="https://ssofed.naz.edu/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://ssofed.naz.edu/idp</option>
		<option value="https://sso-login.vanderbilt.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso-login.vanderbilt.edu</option>
		<option value="https://sso-login-uat.vanderbilt.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sso-login-uat.vanderbilt.edu</option>
		<option value="https://ssoportal.stsci.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://ssoportal.stsci.edu/idp/shibboleth</option>
		<option value="https://ssoserver.hs-worms.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://ssoserver.hs-worms.de/idp/shibboleth</option>
		<option value="https://ssoshib.fhda.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://ssoshib.fhda.edu/idp/shibboleth</option>
		<option value="https://ssosw.losrios.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://ssosw.losrios.edu/idp/shibboleth</option>
		<option value="https://ssov3.institutoptique.fr/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://ssov3.institutoptique.fr/idp/shibboleth</option>
		<option value="https://sts.windows.net/2d714a65-b97f-41a9-8ff1-ec2cdf7df5cd/" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sts.windows.net/2d714a65-b97f-41a9-8ff1-ec2cdf7df5cd/</option>
		<option value="https://sts.windows.net/517085ff-c1f1-4b90-8a7f-ed8816109cfe/" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sts.windows.net/517085ff-c1f1-4b90-8a7f-ed8816109cfe/</option>
		<option value="https://sts.windows.net/695b7ca8-2da8-4545-a2da-42d03784e585/" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sts.windows.net/695b7ca8-2da8-4545-a2da-42d03784e585/</option>
		<option value="https://sts.windows.net/88bc3da8-1f31-4852-ae88-6d08c88a70f7/" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sts.windows.net/88bc3da8-1f31-4852-ae88-6d08c88a70f7/</option>
		<option value="https://sts.windows.net/b78d03e6-f6a2-4cff-83be-847d1a6453f9/" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://sts.windows.net/b78d03e6-f6a2-4cff-83be-847d1a6453f9/</option>
		<option value="https://test-idps.rutgers.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://test-idps.rutgers.edu/idp/shibboleth</option>
		<option value="https://thelonious.campusguard.com/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://thelonious.campusguard.com/idp/shibboleth</option>
		<option value="https://ucanridp.ucanr.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://ucanridp.ucanr.edu/idp/shibboleth</option>
		<option value="https://ucoshib.uco.fr/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://ucoshib.uco.fr/idp/shibboleth</option>
		<option value="https://uisshibb1.uis.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://uisshibb1.uis.edu/idp/shibboleth</option>
		<option value="https://ukidp.uky.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://ukidp.uky.edu/idp/shibboleth</option>
		<option value="https://umshibp.olemiss.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://umshibp.olemiss.edu/idp/shibboleth</option>
		<option value="https://unisa.edu.au/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://unisa.edu.au/idp/shibboleth</option>
		<option value="https://unmpidp.unm.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://unmpidp.unm.edu/idp/shibboleth</option>
		<option value="https://usd-shibboleth.usd.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://usd-shibboleth.usd.edu/idp/shibboleth</option>
		<option value="https://vdu.sso.litnet.lt/auth/saml2/idp/metadata.php" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://vdu.sso.litnet.lt/auth/saml2/idp/metadata.php</option>
		<option value="https://vho.aaf.edu.au/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://vho.aaf.edu.au/idp/shibboleth</option>
		<option value="https://vince.csueastbay.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://vince.csueastbay.edu/idp/shibboleth</option>
		<option value="https://virtualhome.tuakiri.ac.nz/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://virtualhome.tuakiri.ac.nz/idp/shibboleth</option>
		<option value="https://vmpidp.universcience.fr/idp/" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://vmpidp.universcience.fr/idp/</option>
		<option value="https://vm-shibboleth.umb.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://vm-shibboleth.umb.edu/idp/shibboleth</option>
		<option value="https://wap.nddl-lca.fr/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://wap.nddl-lca.fr/idp/shibboleth</option>
		<option value="https://wayf.au.dk" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://wayf.au.dk</option>
		<option value="https://webapp.bgsu.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://webapp.bgsu.edu/idp/shibboleth</option>
		<option value="https://webauth.auburn.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://webauth.auburn.edu/idp/shibboleth</option>
		<option value="https://webauth.cedarcrest.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://webauth.cedarcrest.edu/idp/shibboleth</option>
		<option value="https://webauth.cgu.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://webauth.cgu.edu/idp/shibboleth</option>
		<option value="https://webauth.cmc.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://webauth.cmc.edu/idp/shibboleth</option>
		<option value="https://webauth.cuc.claremont.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://webauth.cuc.claremont.edu/idp/shibboleth</option>
		<option value="https://webauth.kgi.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://webauth.kgi.edu/idp/shibboleth</option>
		<option value="https://webauth.meredith.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://webauth.meredith.edu/idp/shibboleth</option>
		<option value="https://webauth.northern.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://webauth.northern.edu/idp/shibboleth</option>
		<option value="https://webauth.pitzer.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://webauth.pitzer.edu/idp/shibboleth</option>
		<option value="https://webauth.scrippscollege.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://webauth.scrippscollege.edu/idp/shibboleth</option>
		<option value="https://webauth.shib.lsu.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://webauth.shib.lsu.edu/idp/shibboleth</option>
		<option value="https://webauth.umaryland.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://webauth.umaryland.edu/idp/shibboleth</option>
		<option value="https://webauth.umass.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://webauth.umass.edu/idp/shibboleth</option>
		<option value="https://webauth.uncc.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://webauth.uncc.edu/idp/shibboleth</option>
		<option value="https://webauth.wfunet.wfu.edu/saml/saml2/idp/metadata.php" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://webauth.wfunet.wfu.edu/saml/saml2/idp/metadata.php</option>
		<option value="https://webauth2.shib.lsu.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://webauth2.shib.lsu.edu/idp/shibboleth</option>
		<option value="https://weblogin.albany.edu/shibboleth/idp2" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://weblogin.albany.edu/shibboleth/idp2</option>
		<option value="https://weblogin.htw-berlin.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://weblogin.htw-berlin.de/idp/shibboleth</option>
		<option value="https://weblogin.kau.se/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://weblogin.kau.se/idp/shibboleth</option>
		<option value="https://weblogin.uu.se/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://weblogin.uu.se/idp/shibboleth</option>
		<option value="https://webso.iup.edu/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://webso.iup.edu/idp/shibboleth</option>
		<option value="https://websso.esrf.fr/auth/realms/ESRF" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://websso.esrf.fr/auth/realms/ESRF</option>
		<option value="https://websso.pomona.edu/" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://websso.pomona.edu/</option>
		<option value="https://whoami.cesnet.cz/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://whoami.cesnet.cz/idp/shibboleth</option>
		<option value="https://wpkfl-shibidp.fullsail.com/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://wpkfl-shibidp.fullsail.com/idp/shibboleth</option>
		<option value="https://www.rediris.es/sir/cemfiidp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://www.rediris.es/sir/cemfiidp</option>
		<option value="https://www.rediris.es/sir/ifaeidp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://www.rediris.es/sir/ifaeidp</option>
		<option value="https://www.rediris.es/sir/picidp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://www.rediris.es/sir/picidp</option>
		<option value="https://www.sso.uni-erlangen.de/simplesaml/saml2/idp/metadata.php" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://www.sso.uni-erlangen.de/simplesaml/saml2/idp/metadata.php</option>
		<option value="https://www.vutbr.cz/SSO/saml2/idp" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://www.vutbr.cz/SSO/saml2/idp</option>
		<option value="https://zividp.uni-muenster.de/idp/shibboleth" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_https://zividp.uni-muenster.de/idp/shibboleth</option>
		<option value="urn:mace:cru.fr:federation:uhb.fr" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:cru.fr:federation:uhb.fr</option>
		<option value="urn:mace:cru.fr:federation:univ-lyon1.fr" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:cru.fr:federation:univ-lyon1.fr</option>
		<option value="urn:mace:eduserv.org.uk:athens:provider:liv.ac.uk" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:eduserv.org.uk:athens:provider:liv.ac.uk</option>
		<option value="urn:mace:federation.org.au:testfed:au-idp.adelaide.edu.au" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:federation.org.au:testfed:au-idp.adelaide.edu.au</option>
		<option value="urn:mace:federation.org.au:testfed:mq.edu.au" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:federation.org.au:testfed:mq.edu.au</option>
		<option value="urn:mace:federation.org.au:testfed:uq.edu.au" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:federation.org.au:testfed:uq.edu.au</option>
		<option value="urn:mace:incommon:alaska.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:alaska.edu</option>
		<option value="urn:mace:incommon:arizona.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:arizona.edu</option>
		<option value="urn:mace:incommon:asu.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:asu.edu</option>
		<option value="urn:mace:incommon:berkeley.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:berkeley.edu</option>
		<option value="urn:mace:incommon:buffalo.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:buffalo.edu</option>
		<option value="urn:mace:incommon:carleton.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:carleton.edu</option>
		<option value="urn:mace:incommon:case.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:case.edu</option>
		<option value="urn:mace:incommon:clemson.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:clemson.edu</option>
		<option value="urn:mace:incommon:columbia.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:columbia.edu</option>
		<option value="urn:mace:incommon:csun.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:csun.edu</option>
		<option value="urn:mace:incommon:dartmouth.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:dartmouth.edu</option>
		<option value="urn:mace:incommon:duke.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:duke.edu</option>
		<option value="urn:mace:incommon:humboldt.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:humboldt.edu</option>
		<option value="urn:mace:incommon:internet2.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:internet2.edu</option>
		<option value="urn:mace:incommon:jmu.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:jmu.edu</option>
		<option value="urn:mace:incommon:johnshopkins.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:johnshopkins.edu</option>
		<option value="urn:mace:incommon:lafayette.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:lafayette.edu</option>
		<option value="urn:mace:incommon:lbl.gov" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:lbl.gov</option>
		<option value="urn:mace:incommon:mcnc.org" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:mcnc.org</option>
		<option value="urn:mace:incommon:mit.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:mit.edu</option>
		<option value="urn:mace:incommon:mlml.calstate.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:mlml.calstate.edu</option>
		<option value="urn:mace:incommon:msu.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:msu.edu</option>
		<option value="urn:mace:incommon:muohio.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:muohio.edu</option>
		<option value="urn:mace:incommon:nau.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:nau.edu</option>
		<option value="urn:mace:incommon:ncsu.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:ncsu.edu</option>
		<option value="urn:mace:incommon:nih.gov" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:nih.gov</option>
		<option value="urn:mace:incommon:nmu.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:nmu.edu</option>
		<option value="urn:mace:incommon:northwestern.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:northwestern.edu</option>
		<option value="urn:mace:incommon:nyu.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:nyu.edu</option>
		<option value="urn:mace:incommon:odu.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:odu.edu</option>
		<option value="urn:mace:incommon:ohio.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:ohio.edu</option>
		<option value="urn:mace:incommon:ohiolink.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:ohiolink.edu</option>
		<option value="urn:mace:incommon:osu.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:osu.edu</option>
		<option value="urn:mace:incommon:psu.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:psu.edu</option>
		<option value="urn:mace:incommon:richmond.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:richmond.edu</option>
		<option value="urn:mace:incommon:rutgers.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:rutgers.edu</option>
		<option value="urn:mace:incommon:sc.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:sc.edu</option>
		<option value="urn:mace:incommon:stanford.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:stanford.edu</option>
		<option value="urn:mace:incommon:starkstate.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:starkstate.edu</option>
		<option value="urn:mace:incommon:stevens.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:stevens.edu</option>
		<option value="urn:mace:incommon:stonybrook.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:stonybrook.edu</option>
		<option value="urn:mace:incommon:tamu.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:tamu.edu</option>
		<option value="urn:mace:incommon:uab.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:uab.edu</option>
		<option value="urn:mace:incommon:ucdavis.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:ucdavis.edu</option>
		<option value="urn:mace:incommon:uchicago.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:uchicago.edu</option>
		<option value="urn:mace:incommon:uci.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:uci.edu</option>
		<option value="urn:mace:incommon:ucla.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:ucla.edu</option>
		<option value="urn:mace:incommon:ucmerced.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:ucmerced.edu</option>
		<option value="urn:mace:incommon:ucop.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:ucop.edu</option>
		<option value="urn:mace:incommon:ucr.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:ucr.edu</option>
		<option value="urn:mace:incommon:ucsb.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:ucsb.edu</option>
		<option value="urn:mace:incommon:ucsc.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:ucsc.edu</option>
		<option value="urn:mace:incommon:ucsd.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:ucsd.edu</option>
		<option value="urn:mace:incommon:ucsf.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:ucsf.edu</option>
		<option value="urn:mace:incommon:udayton.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:udayton.edu</option>
		<option value="urn:mace:incommon:uiowa.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:uiowa.edu</option>
		<option value="urn:mace:incommon:uiuc.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:uiuc.edu</option>
		<option value="urn:mace:incommon:umbc.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:umbc.edu</option>
		<option value="urn:mace:incommon:umd.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:umd.edu</option>
		<option value="urn:mace:incommon:umn.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:umn.edu</option>
		<option value="urn:mace:incommon:unc.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:unc.edu</option>
		<option value="urn:mace:incommon:usc.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:usc.edu</option>
		<option value="urn:mace:incommon:usf.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:usf.edu</option>
		<option value="urn:mace:incommon:utah.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:utah.edu</option>
		<option value="urn:mace:incommon:uww.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:uww.edu</option>
		<option value="urn:mace:incommon:virginia.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:virginia.edu</option>
		<option value="urn:mace:incommon:vt.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:vt.edu</option>
		<option value="urn:mace:incommon:washington.edu" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:incommon:washington.edu</option>
		<option value="urn:mace:kuleuven.be:kulassoc:kuleuven.be" logo="/adfs/ls/images/federation/blank.gif" data-category="Other">EduGain_urn:mace:kuleuven.be:kulassoc:kuleuven.be</option>
		<option value="https://www.egi.eu/idp/shibboleth" logo="/adfs/ls/images/federation/egi.png" data-category="Other">EGI</option>

	</select>
            </td>
            <td>
              <input type="submit" name="ctl00$ctl00$NICEMasterPageBodyContent$SiteContentPlaceholder$btnSelectFederation" value="Go" id="ctl00_ctl00_NICEMasterPageBodyContent_SiteContentPlaceholder_btnSelectFederation" class="improvedDropDown-button" /></td>
          </tr>
        </table>

        <script language="javascript" type="text/javascript">
          // Handle optgroups 
          var groups = {};
          $("select option[data-category]").each(function () {
            groups[$.trim($(this).attr("data-category"))] = true;
          });
          $.each(groups, function (c) {
            $("select option[data-category='" + c + "']").wrapAll('<optgroup label="' + c + '">');
          });

          // Apply the improvedDropDown styling
          $('#ctl00_ctl00_NICEMasterPageBodyContent_SiteContentPlaceholder_drpFederation').improveDropDown({
            iconPath: '/adfs/ls/images/drop_icon.png',
            noMatchesText: 'No organisation found for this search text',
            noItemsText: 'No organisation available'
          });

        </script>
      </div>
      <div>
        <a href="http://sirtfi.cern.ch?sp=cern" target="_blank">Why is my organisation not listed?</a>
      </div>
    </div>
  
</div>

  <a href="javascript:showhidedebug();" id="ctl00_ctl00_NICEMasterPageBodyContent_SiteContentPlaceholder_hrefShowDebug" style="font-weight: normal; color: white; font-size: smaller;">[show debug information]</a>
  <div id="ctl00_ctl00_NICEMasterPageBodyContent_SiteContentPlaceholder_divDebug" class="box_auth" style="display: none; border-color: #ffd800; background-color: white;">
    <div class="signinwith fullWidth">Debug</div>
    <div style="font-size: x-small;">
      Server: ADFS11
      <br />
      User Agent: Wget/1.14 (linux-gnu)
    </div>
  </div>
  <span id="ctl00_ctl00_NICEMasterPageBodyContent_SiteContentPlaceholder_lblInfo"></span>



    </div>

    
    <div id="ctl00_ctl00_pnlFooter">
	
        <div id="footer">
            <div class="page">
                <div class="region-footer-first">
                        <h2>Related sites</h2>
                        
    <ul>
        <li class="leaf"><a href="https://account.cern.ch/account/Help/?kbid=021010" target="_blank">Need password help ?</a></li>
        <li class="leaf"><a href="http://cern.ch/account" target="_blank">Create/Check your account</a></li>
        <li class="leaf"><a href="https://www.cern.ch/ssoutils/Disclaimer/UserSettings.aspx" target="_blank">EduGain disclaimer settings</a></li>
        <li class="leaf"><a href="http://www.cern.ch/service-portal" target="_blank">Service Desk</a> <span class='subtle'>+41 22 76 77777</span></li>
        <li class="leaf"><a href="https://cern.service-now.com/service-portal/ssb.do?area=IT" target="_blank">Computing Status Board</a></li>
        <li id="ctl00_ctl00_NICEMasterPageRelatedSites_lblIPv6" class="leaf">Connection using <a href="https://cern.ch/ipv6" target="_blank">IPv6</a></li>
    </ul>
    
    <div style="visibility: hidden">
        <img src="//piwik-login.web.cern.ch/piwik.php?idsite=2536&rec=1" style="border: 0" alt="" />
    </div>

                </div>

                <div class="cern-logo">
                    <a href="http://cern.ch" title="CERN" rel="CERN" ><img class="footer_logo_img" border="0" src="Images/cern-logo-large.png" alt="CERN" border="0" /></a>
                </div>
            </div>
        </div>
    
</div>
    
  </form>

</body>
</html>