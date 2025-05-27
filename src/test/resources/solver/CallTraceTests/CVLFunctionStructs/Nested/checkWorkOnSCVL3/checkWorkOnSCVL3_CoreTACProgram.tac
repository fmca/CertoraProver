TACSymbolTable {
	UserDefined {
		UninterpSort skey
	}
	BuiltinFunctions {
		to_skey:JSON{"#class":"vc.data.TACBuiltInFunction.Hash.ToSkey"}
		skey_basic:JSON{"#class":"vc.data.TACBuiltInFunction.Hash.Basic"}
		hash_3_keccak:JSON{"#class":"vc.data.TACBuiltInFunction.Hash.SimpleHashApplication","arity":3,"hashFamily":{"#class":"vc.data.HashFamily.Keccack"}}
		skey_add:JSON{"#class":"vc.data.TACBuiltInFunction.Hash.Addition"}
	}
	UninterpretedFunctions {
	}
	tacCodesizeCANON0:bv256:0
	tacExtcodesize!!1:wordmap:1
	CANON61!!2:wordmap:2
	CANON77!!3:wordmap:3
	tacExtcodesize:wordmap:1
	B9:bool:4
	R0:bv256:0
	R4:bv256:5
	R5:bv256:6
	R6:bv256:7
	R7:bv256:8
	R8:bv256:4
	B10:bool:4
	B13:bool:9
	B19:bool:10
	B21:bool:11
	B26:bool:12
	B28:bool:13
	B29:bool:14
	B33:bool:4
	B36:bool:9
	B41:bool:9
	B44:bool:9
	B48:bool:4
	B51:bool:9
	B56:bool:9
	B59:bool:9
	B60:bool:14
	B61:bool:9
	I11:int:15
	I12:int:16
	I14:int:15
	I15:int:17
	I16:int:18
	I17:int:19
	I18:int:20
	I20:int:21
	I22:int:22
	I23:int:23
	I24:int:24
	I25:int:25
	I27:int:26
	I30:int:27
	I37:int:27
	I42:int:15
	I43:int:16
	I45:int:27
	I52:int:27
	I57:int:15
	I58:int:28
	R31:(uninterp) skey:4
	R32:(uninterp) skey:4
	R34:bv256:4
	R38:(uninterp) skey:4
	R39:(uninterp) skey:4
	R40:bv256:4
	R46:(uninterp) skey:4
	R47:(uninterp) skey:4
	R49:bv256:4
	R53:(uninterp) skey:4
	R54:(uninterp) skey:4
	R55:bv256:4
	CANON61!!35:wordmap:2
	CANON10:int:29
	CANON11:int:30
	CANON12:int:31
	CANON13:int:32
	CANON14:int:33
	CANON15:int:34
	CANON16:int:35
	CANON17:int:36
	CANON18:int:37
	CANON19:bool:38
	CANON20:bool:39
	CANON21:bool:40
	CANON22:bool:41
	CANON23:bool:42
	CANON24:int:15
	CANON25:int:43
	CANON26:int:17
	CANON27:int:18
	CANON28:int:19
	CANON29:int:20
	CANON30:bool:10
	CANON31:int:21
	CANON32:bool:11
	CANON33:int:22
	CANON34:int:23
	CANON35:int:24
	CANON36:int:25
	CANON37:bool:12
	CANON38:int:26
	CANON39:bool:13
	CANON40:bool:44
	CANON41:int:45
	CANON42:int:46
	CANON43:int:47
	CANON44:int:48
	CANON45:bool:49
	CANON46:int:50
	CANON47:bool:51
	CANON48:int:52
	CANON49:int:53
	CANON50:int:54
	CANON51:int:55
	CANON52:bool:56
	CANON53:int:57
	CANON54:bool:58
	CANON55:bool:59
	CANON56:int:27
	CANON57:bv256:4
	CANON58:bv256:60
	CANON59:bool:4
	CANON60:bv256:4
	CANON61:wordmap:2
	CANON62:bool:9
	CANON63:int:27
	CANON64:bv256:4
	CANON65:bv256:61
	CANON66:bv256:4
	CANON67:bool:9
	CANON68:int:15
	CANON69:int:16
	CANON70:bool:9
	CANON71:bool:62
	CANON72:int:27
	CANON73:bv256:4
	CANON74:bv256:63
	CANON75:bool:4
	CANON76:bv256:4
	CANON77:wordmap:3
	CANON78:bool:9
	CANON79:int:27
	CANON80:bv256:4
	CANON81:bv256:64
	CANON82:bv256:4
	CANON83:bool:9
	CANON84:int:15
	CANON85:int:28
	CANON86:bool:9
	CANON87:bool:62
	CANON88:bool:44
	CANON89:bool:9
	tacContractAtCANON1:bv256:5
	tacContractAtCANON2:bv256:6
	tacContractAtCANON3:bv256:7
	CANON1:int:65
	CANON2:int:66
	CANON3:bv256:4
	CANON4:bool:4
	CANON5:bool:4
	CANON6:int:15
	CANON7:int:16
	CANON8:bool:9
	CANON9:int:67
	tacContractAtCANON:bv256:8
	CANON77!!50:wordmap:3
	CANON:int:68
}
Program {
	Block 0_0_0_0_0_0 Succ [1_0_0_1_0_1] {
		AssignHavocCmd R0:0
		AssumeExpCmd Ge(R0:0 0x1 )
		AssignHavocCmd tacExtcodesize!!1:1
		AssignHavocCmd CANON10:29
		AssumeExpCmd LAnd(Ge(CANON10:29 0x0(int) ) Le(CANON10:29 0xffffffffffffffffffffffffffffffffffffffff(int) ) )
		AssignHavocCmd CANON11:30
		AssumeExpCmd LAnd(Ge(CANON11:30 0x0(int) ) Le(CANON11:30 0xff(int) ) )
		AssignHavocCmd CANON12:31
		AssumeExpCmd LAnd(Ge(CANON12:31 0x0(int) ) Le(CANON12:31 0xff(int) ) )
		AssignHavocCmd CANON13:32
		AssumeExpCmd LAnd(Ge(CANON13:32 0x0(int) ) Le(CANON13:32 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff(int) ) )
		AssignHavocCmd CANON14:33
		AssumeExpCmd LAnd(Ge(CANON14:33 0x0(int) ) Le(CANON14:33 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff(int) ) )
		AssignHavocCmd CANON15:34
		AssumeExpCmd LAnd(Ge(CANON15:34 0x0(int) ) Le(CANON15:34 0xffffffffffffffffffffffffffffffffffffffff(int) ) )
		AssignHavocCmd CANON16:35
		AssumeExpCmd LAnd(Ge(CANON16:35 0x0(int) ) Le(CANON16:35 0xff(int) ) )
		AssignHavocCmd CANON17:36
		AssumeExpCmd LAnd(Ge(CANON17:36 0x0(int) ) Le(CANON17:36 0xff(int) ) )
		AssignHavocCmd CANON18:37
		AssumeExpCmd LAnd(Ge(CANON18:37 0x0(int) ) Le(CANON18:37 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff(int) ) )
		AssignHavocCmd CANON19:38
		AssignHavocCmd CANON20:39
		AssignHavocCmd CANON21:40
		AssignHavocCmd CANON22:41
		AssignHavocCmd CANON23:42
		AssignHavocCmd CANON61!!2:2
		AssignHavocCmd CANON77!!3:3
		AssignHavocCmd R4:5
		AssumeExpCmd Eq(R4:5 0x1 )
		AssignHavocCmd R5:6
		AssumeExpCmd Eq(R5:6 0x2 )
		AssignHavocCmd R6:7
		AssumeExpCmd Eq(R6:7 0x4 )
		AssignHavocCmd CANON9:67
		AssumeExpCmd LAnd(Ge(CANON9:67 0x0(int) ) Le(CANON9:67 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff(int) ) )
		AssignHavocCmd R7:8
		AssumeExpCmd LAnd(Ge(R7:8 0x1 ) Le(R7:8 0xffffffffffffffffffffffffffffffffffffffff ) )
		AnnotationCmd JSON{"key":{"name":"tac.state.extension","type":"analysis.icfg.Inliner$ExtendedStateVars","erasureStrategy":"Canonical"},"value":"rO0ABXNyACdhbmFseXNpcy5pY2ZnLklubGluZXIkRXh0ZW5kZWRTdGF0ZVZhcnOvh/MjxNFkQAIAAUwAFmluc3RhbmNlVG9FeHRlbmRlZFZhcnN0AA9MamF2YS91dGlsL01hcDt4cHNyACFkYXRhc3RydWN0dXJlcy5MaW5rZWRBcnJheUhhc2hNYXAAAAAAAAAAAQMAAkYACmxvYWRGYWN0b3JMAAloYXNoVGFibGV0AC5MZGF0YXN0cnVjdHVyZXMvYXJyYXloYXNodGFibGUvQXJyYXlIYXNoVGFibGU7eHB3CAAAAAFAAAAAc3IAFGphdmEubWF0aC5CaWdJbnRlZ2VyjPyfH6k7+x0DAAZJAAhiaXRDb3VudEkACWJpdExlbmd0aEkAE2ZpcnN0Tm9uemVyb0J5dGVOdW1JAAxsb3dlc3RTZXRCaXRJAAZzaWdudW1bAAltYWduaXR1ZGV0AAJbQnhyABBqYXZhLmxhbmcuTnVtYmVyhqyVHQuU4IsCAAB4cP///////////////v////4AAAABdXIAAltCrPMX+AYIVOACAAB4cAAAABDORgSgAAAAAAAAAAAAAAABeHNxAH4AA3cIAAAAAEAAAAB4eA=="}
		AnnotationCmd:69 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"rule parameters setup"}}
		AssignHavocCmd CANON:68
		AssumeExpCmd LAnd(Ge(CANON:68 0x0(int) ) Le(CANON:68 0x2(int) ) )
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.CVLSnippetCmd.CVLArg.PrimitiveArg","callIndex":0,"index":0,"sym":{"namePrefix":"CANON","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":68,"charByteOffset":22},"end":{"line":68,"charByteOffset":28}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"x"}]},"param":{"Named_type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"id":"x","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":68,"charByteOffset":22},"end":{"line":68,"charByteOffset":28}}}}}
		AnnotationCmd JSON{"key":{"name":"cvl.trace.declaration","type":"spec.CVLCompiler$Companion$TraceMeta$VariableDeclaration","erasureStrategy":"Erased"},"value":{"v":{"#class":"spec.CVLCompiler.Companion.TraceMeta.ValueIdentity.TACVar","t":{"namePrefix":"CANON","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":68,"charByteOffset":22},"end":{"line":68,"charByteOffset":28}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"x"}]}},"t":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"type":{"#class":"spec.CVLCompiler.Companion.TraceMeta.DeclarationType.Parameter","sourceName":"x"},"fields":null}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":0}
		AnnotationCmd:70 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"Setup"}}
		AnnotationCmd:71 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"multi contract setup"}}
		AssignExpCmd CANON1:65 R7:72
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":2}
		AnnotationCmd:73 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"contract address vars initialized"}}
		AssignExpCmd CANON2:66 R7:72
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":3}
		AnnotationCmd:74 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"setup read tracking instrumentation"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":4}
		AnnotationCmd:75 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"last storage initialize"}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule"}},{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.NonTACKeywordEntry","name":"lastStorage"}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":5}
		AnnotationCmd:76 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assuming contracts in scene with non-empty bytecode have EXTCODESIZE larger than zero"}}
		AssignExpCmd R8:4 Select(tacExtcodesize!!1:1 Apply(to_skey:bif R7:72) )
		AssumeExpCmd Ge(R8:4 0x1 )
		AssumeExpCmd Eq(R8:77 R0:78 )
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":6}
		AnnotationCmd:79 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assuming address(0).code has no code deployed"}}
		AssignExpCmd B10:4 Eq(Select(tacExtcodesize!!1:1 Apply(skey_basic:bif 0x0) ) 0x0 )
		AssumeCmd B10:4 "expToAssumeCmd"
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":7}
		AnnotationCmd:80 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about contracts' addresses"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":8}
		AnnotationCmd:81 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about static addresses"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":9}
		AnnotationCmd:82 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"establish addresses of precompiled contracts"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":10}
		AnnotationCmd:83 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about uniqueness of contracts' addresses"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":11}
		AnnotationCmd:84 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"static links"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":12}
		AnnotationCmd:85 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"record starting nonces"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":13}
		AnnotationCmd:86 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"cloned contracts have no balances"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":14}
		AnnotationCmd:87 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"Linked immutable setup"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":15}
		AnnotationCmd:88 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"Constrain immutables"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":16}
		AnnotationCmd:89 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"establish equivalence of extension and base contract immutables"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":17}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1}
		AnnotationCmd:90 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.AssumeCmd.Assume","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":69,"charByteOffset":4},"end":{"line":69,"charByteOffset":18}},"exp":{"#class":"spec.cvlast.CVLExp.RelopExp.ArithRelopExp.LtExp","l":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"x","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":8}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":69,"charByteOffset":12},"end":{"line":69,"charByteOffset":13}}},"twoStateIndex":"NEITHER"},"r":{"#class":"spec.cvlast.CVLExp.Constant.NumberLit","n":"3","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":8}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral","n":"3"},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":69,"charByteOffset":16},"end":{"line":69,"charByteOffset":17}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":8}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":69,"charByteOffset":12},"end":{"line":69,"charByteOffset":17}}}},"description":null,"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":8}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssignExpCmd:91 I11:15 CANON:68
		AssignExpCmd:92 I12:16 0x3
		AssignExpCmd:93 B13:9 true
		AnnotationCmd:94 JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":18}
		AnnotationCmd:95 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Declaration","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":70,"charByteOffset":4},"end":{"line":70,"charByteOffset":27}},"cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Complex","fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"b3","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"id":"s","scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":8}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AnnotationCmd JSON{"key":{"name":"cvl.trace.declaration","type":"spec.CVLCompiler$Companion$TraceMeta$VariableDeclaration","erasureStrategy":"Erased"},"value":{"v":{"#class":"spec.CVLCompiler.Companion.TraceMeta.ValueIdentity.CVLVar","id":"s876"},"t":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Complex","fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"b3","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"type":{"#class":"spec.CVLCompiler.Companion.TraceMeta.DeclarationType.Variable"},"fields":[[{"#class":"tac.DataField.StructField","field":"b3"}],{"namePrefix":"CANON19","tag":{"#class":"tac.Tag.Bool"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"TestContract.Complex","fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"b3","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"fields":[{"fieldName":"b3","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":70,"charByteOffset":4},"end":{"line":70,"charByteOffset":27}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"s.b3"}]},[{"#class":"tac.DataField.StructField","field":"s1"},{"#class":"tac.DataField.StructField","field":"x"}],{"namePrefix":"CANON9","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"TestContract.Complex","fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"b3","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":70,"charByteOffset":4},"end":{"line":70,"charByteOffset":27}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"s.s1.x"}]},[{"#class":"tac.DataField.StructField","field":"s1"},{"#class":"tac.DataField.StructField","field":"y"}],{"namePrefix":"CANON10","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"TestContract.Complex","fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"b3","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":70,"charByteOffset":4},"end":{"line":70,"charByteOffset":27}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"s.s1.y"}]},[{"#class":"tac.DataField.StructField","field":"s2"},{"#class":"tac.DataField.StructField","field":"x"}],{"namePrefix":"CANON14","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"TestContract.Complex","fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"b3","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"fields":[{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":70,"charByteOffset":4},"end":{"line":70,"charByteOffset":27}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"s.s2.x"}]},[{"#class":"tac.DataField.StructField","field":"s2"},{"#class":"tac.DataField.StructField","field":"y"}],{"namePrefix":"CANON15","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"TestContract.Complex","fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"b3","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"fields":[{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":70,"charByteOffset":4},"end":{"line":70,"charByteOffset":27}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"s.s2.y"}]},[{"#class":"tac.DataField.StructField","field":"s1"},{"#class":"tac.DataField.StructField","field":"b1"}],{"namePrefix":"CANON20","tag":{"#class":"tac.Tag.Bool"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"TestContract.Complex","fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"b3","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":70,"charByteOffset":4},"end":{"line":70,"charByteOffset":27}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"s.s1.b1"}]},[{"#class":"tac.DataField.StructField","field":"s1"},{"#class":"tac.DataField.StructField","field":"b2"}],{"namePrefix":"CANON21","tag":{"#class":"tac.Tag.Bool"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"TestContract.Complex","fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"b3","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":70,"charByteOffset":4},"end":{"line":70,"charByteOffset":27}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"s.s1.b2"}]},[{"#class":"tac.DataField.StructField","field":"s2"},{"#class":"tac.DataField.StructField","field":"b1"}],{"namePrefix":"CANON22","tag":{"#class":"tac.Tag.Bool"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"TestContract.Complex","fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"b3","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"fields":[{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":70,"charByteOffset":4},"end":{"line":70,"charByteOffset":27}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"s.s2.b1"}]},[{"#class":"tac.DataField.StructField","field":"s2"},{"#class":"tac.DataField.StructField","field":"b2"}],{"namePrefix":"CANON23","tag":{"#class":"tac.Tag.Bool"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"TestContract.Complex","fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"b3","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"fields":[{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":70,"charByteOffset":4},"end":{"line":70,"charByteOffset":27}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"s.s2.b2"}]},[{"#class":"tac.DataField.StructField","field":"s1"},{"#class":"tac.DataField.StructField","field":"x2"}],{"namePrefix":"CANON13","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"TestContract.Complex","fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"b3","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":70,"charByteOffset":4},"end":{"line":70,"charByteOffset":27}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"s.s1.x2"}]},[{"#class":"tac.DataField.StructField","field":"s2"},{"#class":"tac.DataField.StructField","field":"x2"}],{"namePrefix":"CANON18","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"TestContract.Complex","fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"b3","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"fields":[{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":70,"charByteOffset":4},"end":{"line":70,"charByteOffset":27}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"s.s2.x2"}]},[{"#class":"tac.DataField.StructField","field":"s1"},{"#class":"tac.DataField.StructField","field":"z1"}],{"namePrefix":"CANON11","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"TestContract.Complex","fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"b3","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":70,"charByteOffset":4},"end":{"line":70,"charByteOffset":27}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"s.s1.z1"}]},[{"#class":"tac.DataField.StructField","field":"s1"},{"#class":"tac.DataField.StructField","field":"z2"}],{"namePrefix":"CANON12","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"TestContract.Complex","fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"b3","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":70,"charByteOffset":4},"end":{"line":70,"charByteOffset":27}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"s.s1.z2"}]},[{"#class":"tac.DataField.StructField","field":"s2"},{"#class":"tac.DataField.StructField","field":"z1"}],{"namePrefix":"CANON16","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"TestContract.Complex","fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"b3","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"fields":[{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":70,"charByteOffset":4},"end":{"line":70,"charByteOffset":27}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"s.s2.z1"}]},[{"#class":"tac.DataField.StructField","field":"s2"},{"#class":"tac.DataField.StructField","field":"z2"}],{"namePrefix":"CANON17","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"TestContract.Complex","fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"b3","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"fields":[{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":70,"charByteOffset":4},"end":{"line":70,"charByteOffset":27}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"s.s2.z2"}]}]}}
		AnnotationCmd:96 JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":19}
		AnnotationCmd:97 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Apply","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":71,"charByteOffset":4},"end":{"line":71,"charByteOffset":28}},"exp":{"#class":"spec.cvlast.CVLExp.ApplyExp.CVLFunction","id":"workOnSComplexCVL","args":[{"#class":"spec.cvlast.CVLExp.VariableExp","id":"x","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":8}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":71,"charByteOffset":22},"end":{"line":71,"charByteOffset":23}}},"twoStateIndex":"NEITHER"},{"#class":"spec.cvlast.CVLExp.VariableExp","id":"s","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":8}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Complex","fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"b3","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":71,"charByteOffset":25},"end":{"line":71,"charByteOffset":26}}},"twoStateIndex":"NEITHER"}],"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":8}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Void"},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":71,"charByteOffset":4},"end":{"line":71,"charByteOffset":27}}},"noRevert":true},"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":8}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
	}
	Block 1_0_0_1_0_1 Succ [2_0_0_0_0_0] {
		AnnotationCmd:98 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.CVLSnippetCmd.CVLFunctionStart","callIndex":1,"name":"workOnSComplexCVL","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":71,"charByteOffset":4},"end":{"line":71,"charByteOffset":27}},"isNoRevert":true}}
		AssignExpCmd:99 I14:15 CANON:68
		AssignExpCmd:98 CANON25:43 I14:15
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.CVLSnippetCmd.CVLArg.PrimitiveArg","callIndex":1,"index":0,"sym":{"namePrefix":"CANON25","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Function","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":7,"charByteOffset":27},"end":{"line":7,"charByteOffset":33}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"x"}]},"param":{"Named_type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"id":"x","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":7,"charByteOffset":27},"end":{"line":7,"charByteOffset":33}}}}}
		AnnotationCmd JSON{"key":{"name":"cvl.trace.data.movement","type":"spec.CVLCompiler$Companion$TraceMeta$CVLMovement","erasureStrategy":"Erased"},"value":{"dst":{"id":"s909912"},"src":{"id":"s876"}}}
		AnnotationCmd JSON{"key":{"name":"cvl.trace.data.movement","type":"spec.CVLCompiler$Companion$TraceMeta$CVLMovement","erasureStrategy":"Erased"},"value":{"dst":{"id":"s896"},"src":{"id":"s909912"}}}
		AssignExpCmd CANON41:45 CANON9:67
		AssignExpCmd CANON42:46 CANON10:29
		AssignExpCmd CANON43:47 CANON11:30
		AssignExpCmd CANON44:48 CANON12:31
		AssignExpCmd CANON45:49 CANON20:39
		AssignExpCmd CANON46:50 CANON13:32
		AssignExpCmd CANON47:51 CANON21:40
		AssignExpCmd CANON48:52 CANON14:33
		AssignExpCmd CANON49:53 CANON15:34
		AssignExpCmd CANON50:54 CANON16:35
		AssignExpCmd CANON51:55 CANON17:36
		AssignExpCmd CANON52:56 CANON22:41
		AssignExpCmd CANON53:57 CANON18:37
		AssignExpCmd CANON54:58 CANON23:42
		AssignExpCmd CANON55:59 CANON19:38
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.CVLSnippetCmd.CVLArg.StructArg","callIndex":1,"index":1,"symbols":[{"namePrefix":"CANON41","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"TestContract.Complex","fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"b3","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Function","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":7,"charByteOffset":35},"end":{"line":7,"charByteOffset":57}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"s.s1.x"}]},{"namePrefix":"CANON42","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"TestContract.Complex","fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"b3","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Function","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":7,"charByteOffset":35},"end":{"line":7,"charByteOffset":57}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"s.s1.y"}]},{"namePrefix":"CANON43","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"TestContract.Complex","fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"b3","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Function","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":7,"charByteOffset":35},"end":{"line":7,"charByteOffset":57}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"s.s1.z1"}]},{"namePrefix":"CANON44","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"TestContract.Complex","fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"b3","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Function","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":7,"charByteOffset":35},"end":{"line":7,"charByteOffset":57}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"s.s1.z2"}]},{"namePrefix":"CANON45","tag":{"#class":"tac.Tag.Bool"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"TestContract.Complex","fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"b3","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Function","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":7,"charByteOffset":35},"end":{"line":7,"charByteOffset":57}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"s.s1.b1"}]},{"namePrefix":"CANON46","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"TestContract.Complex","fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"b3","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Function","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":7,"charByteOffset":35},"end":{"line":7,"charByteOffset":57}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"s.s1.x2"}]},{"namePrefix":"CANON47","tag":{"#class":"tac.Tag.Bool"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"TestContract.Complex","fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"b3","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Function","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":7,"charByteOffset":35},"end":{"line":7,"charByteOffset":57}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"s.s1.b2"}]},{"namePrefix":"CANON48","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"TestContract.Complex","fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"b3","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"fields":[{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Function","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":7,"charByteOffset":35},"end":{"line":7,"charByteOffset":57}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"s.s2.x"}]},{"namePrefix":"CANON49","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"TestContract.Complex","fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"b3","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"fields":[{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Function","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":7,"charByteOffset":35},"end":{"line":7,"charByteOffset":57}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"s.s2.y"}]},{"namePrefix":"CANON50","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"TestContract.Complex","fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"b3","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"fields":[{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Function","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":7,"charByteOffset":35},"end":{"line":7,"charByteOffset":57}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"s.s2.z1"}]},{"namePrefix":"CANON51","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"TestContract.Complex","fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"b3","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"fields":[{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Function","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":7,"charByteOffset":35},"end":{"line":7,"charByteOffset":57}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"s.s2.z2"}]},{"namePrefix":"CANON52","tag":{"#class":"tac.Tag.Bool"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"TestContract.Complex","fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"b3","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"fields":[{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Function","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":7,"charByteOffset":35},"end":{"line":7,"charByteOffset":57}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"s.s2.b1"}]},{"namePrefix":"CANON53","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"TestContract.Complex","fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"b3","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"fields":[{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Function","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":7,"charByteOffset":35},"end":{"line":7,"charByteOffset":57}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"s.s2.x2"}]},{"namePrefix":"CANON54","tag":{"#class":"tac.Tag.Bool"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"TestContract.Complex","fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"b3","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"fields":[{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Function","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":7,"charByteOffset":35},"end":{"line":7,"charByteOffset":57}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"s.s2.b2"}]},{"namePrefix":"CANON55","tag":{"#class":"tac.Tag.Bool"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"TestContract.Complex","fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"b3","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"fields":[{"fieldName":"b3","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Function","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":7,"charByteOffset":35},"end":{"line":7,"charByteOffset":57}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"s.b3"}]}],"param":{"Named_type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Complex","fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"b3","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"id":"s","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":7,"charByteOffset":35},"end":{"line":7,"charByteOffset":57}}}}}
		AnnotationCmd:100 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Havoc","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":8,"charByteOffset":4},"end":{"line":8,"charByteOffset":34}},"targets":[{"#class":"spec.cvlast.CVLExp.FieldSelectExp","structExp":{"#class":"spec.cvlast.CVLExp.FieldSelectExp","structExp":{"#class":"spec.cvlast.CVLExp.ArrayDerefExp","array":{"#class":"spec.cvlast.CVLExp.FieldSelectExp","structExp":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"testContract","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":9}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.CodeContract","name":{"name":"TestContract"}},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":8,"charByteOffset":10},"end":{"line":8,"charByteOffset":22}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.CVLExp$VariableExp$ContractInstanceId","instanceId":"ce4604a0000000000000000000000001"}},"twoStateIndex":"NEITHER"},"fieldName":"m","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":9}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.VM","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMMappingDescriptor","keyType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"valueType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.EVMStructDescriptor","canonicalId":"TestContract.sol|TestContract.Complex","location":null,"fields":[{"fieldName":"s1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.EVMStructDescriptor","canonicalId":"TestContract.sol|TestContract.Simple","location":null,"fields":[{"fieldName":"x","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"fieldName":"y","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}},{"fieldName":"z1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8}},{"fieldName":"z2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8}},{"fieldName":"b1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}},{"fieldName":"x2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"fieldName":"b2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}}],"name":"TestContract.Simple"}},{"fieldName":"s2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.EVMStructDescriptor","canonicalId":"TestContract.sol|TestContract.Simple","location":null,"fields":[{"fieldName":"x","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"fieldName":"y","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}},{"fieldName":"z1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8}},{"fieldName":"z2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8}},{"fieldName":"b1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}},{"fieldName":"x2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"fieldName":"b2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}}],"name":"TestContract.Simple"}},{"fieldName":"b3","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}}],"name":"TestContract.Complex"},"location":null},"context":{"#class":"spec.cvlast.typedescriptors.FromVMContext.StateValue"}},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":8,"charByteOffset":10},"end":{"line":8,"charByteOffset":24}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.StorageAccessMarker"}}},"index":{"#class":"spec.cvlast.CVLExp.Constant.NumberLit","n":"0","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":9}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral","n":"0"},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":8,"charByteOffset":25},"end":{"line":8,"charByteOffset":26}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":9}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.VM","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMStructDescriptor","canonicalId":"TestContract.sol|TestContract.Complex","location":null,"fields":[{"fieldName":"s1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.EVMStructDescriptor","canonicalId":"TestContract.sol|TestContract.Simple","location":null,"fields":[{"fieldName":"x","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"fieldName":"y","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}},{"fieldName":"z1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8}},{"fieldName":"z2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8}},{"fieldName":"b1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}},{"fieldName":"x2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"fieldName":"b2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}}],"name":"TestContract.Simple"}},{"fieldName":"s2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.EVMStructDescriptor","canonicalId":"TestContract.sol|TestContract.Simple","location":null,"fields":[{"fieldName":"x","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"fieldName":"y","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}},{"fieldName":"z1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8}},{"fieldName":"z2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8}},{"fieldName":"b1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}},{"fieldName":"x2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"fieldName":"b2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}}],"name":"TestContract.Simple"}},{"fieldName":"b3","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}}],"name":"TestContract.Complex"},"context":{"#class":"spec.cvlast.typedescriptors.FromVMContext.StateValue"}},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":8,"charByteOffset":10},"end":{"line":8,"charByteOffset":27}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.StorageAccessMarker"}}},"fieldName":"s1","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":9}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.VM","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMStructDescriptor","canonicalId":"TestContract.sol|TestContract.Simple","location":null,"fields":[{"fieldName":"x","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"fieldName":"y","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}},{"fieldName":"z1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8}},{"fieldName":"z2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8}},{"fieldName":"b1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}},{"fieldName":"x2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"fieldName":"b2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}}],"name":"TestContract.Simple"},"context":{"#class":"spec.cvlast.typedescriptors.FromVMContext.StateValue"}},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":8,"charByteOffset":10},"end":{"line":8,"charByteOffset":30}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.StorageAccessMarker"}}},"fieldName":"b1","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":9}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.VM","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$bool"},"context":{"#class":"spec.cvlast.typedescriptors.FromVMContext.StateValue"}},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":8,"charByteOffset":10},"end":{"line":8,"charByteOffset":33}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.StorageAccessMarker"}}}],"assumingExp":null,"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":9}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssignExpCmd:101 I30:27 0x0
		AssertCmd:102 true "sanity bounds check on cvl to vm encoding (unsigned int elements of a user array) of %1$s failed"
		AssignExpCmd:103 R31:4 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(skey_basic:bif 0x0) Apply(skey_basic:bif 0x0))
		AssignExpCmd:103 R32:4 Apply(skey_add:bif R31:4 0x1)
		AssignHavocCmd:103 B33:4
		AssignExpCmd:103 R34:4 Ite(B33:4 0x1 0x0 )
		AssignExpCmd:104 CANON61!!35:2 AnnotationExp(Store(CANON61!!2:2 R32:105 R34:4 ) JSON{"key":{"name":"tac.storage.access-paths","type":"analysis.storage.StorageAnalysisResult$AccessPaths","erasureStrategy":"Canonical"},"value":{"paths":[{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.StructAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.MapAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.Root","slot":"0"},"key":{"#class":"vc.data.TACSymbol.Const","value":"0"},"baseSlot":{"#class":"vc.data.TACSymbol.Const","value":"0"},"hashResult":{"#class":"vc.data.TACSymbol.Const","value":"0"}},"offset":{"#class":"analysis.storage.StorageAnalysis.Offset.Bytes","numBytes":"36"}}]}})
		AnnotationCmd:103 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.DirectStorageHavoc","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R34","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"displayPath":{"#class":"analysis.storage.DisplayPath.FieldAccess","field":"b1","base":{"#class":"analysis.storage.DisplayPath.FieldAccess","field":"s1","base":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Const","value":"0"},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"uint256","numBytes":"20","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"m"}}}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"},"contractInstance":"ce4604a0000000000000000000000001","range":{"specFile":"test.spec","start":{"line":8,"charByteOffset":10},"end":{"line":8,"charByteOffset":33}}}}
		AssignExpCmd:106 B36:9 true
		AnnotationCmd:103 JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":21}
		AnnotationCmd:107 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.AssumeCmd.Assume","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":9,"charByteOffset":4},"end":{"line":9,"charByteOffset":47}},"exp":{"#class":"spec.cvlast.CVLExp.RelopExp.EqExp","l":{"#class":"spec.cvlast.CVLExp.FieldSelectExp","structExp":{"#class":"spec.cvlast.CVLExp.FieldSelectExp","structExp":{"#class":"spec.cvlast.CVLExp.ArrayDerefExp","array":{"#class":"spec.cvlast.CVLExp.FieldSelectExp","structExp":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"testContract","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":9}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.CodeContract","name":{"name":"TestContract"}},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":9,"charByteOffset":12},"end":{"line":9,"charByteOffset":24}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.CVLExp$VariableExp$ContractInstanceId","instanceId":"ce4604a0000000000000000000000001"}},"twoStateIndex":"NEITHER"},"fieldName":"m","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":9}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.VM","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMMappingDescriptor","keyType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"valueType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.EVMStructDescriptor","canonicalId":"TestContract.sol|TestContract.Complex","location":null,"fields":[{"fieldName":"s1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.EVMStructDescriptor","canonicalId":"TestContract.sol|TestContract.Simple","location":null,"fields":[{"fieldName":"x","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"fieldName":"y","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}},{"fieldName":"z1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8}},{"fieldName":"z2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8}},{"fieldName":"b1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}},{"fieldName":"x2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"fieldName":"b2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}}],"name":"TestContract.Simple"}},{"fieldName":"s2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.EVMStructDescriptor","canonicalId":"TestContract.sol|TestContract.Simple","location":null,"fields":[{"fieldName":"x","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"fieldName":"y","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}},{"fieldName":"z1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8}},{"fieldName":"z2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8}},{"fieldName":"b1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}},{"fieldName":"x2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"fieldName":"b2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}}],"name":"TestContract.Simple"}},{"fieldName":"b3","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}}],"name":"TestContract.Complex"},"location":null},"context":{"#class":"spec.cvlast.typedescriptors.FromVMContext.StateValue"}},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":9,"charByteOffset":12},"end":{"line":9,"charByteOffset":26}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.StorageAccessMarker"}}},"index":{"#class":"spec.cvlast.CVLExp.Constant.NumberLit","n":"0","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":9}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral","n":"0"},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":9,"charByteOffset":27},"end":{"line":9,"charByteOffset":28}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":9}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.VM","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMStructDescriptor","canonicalId":"TestContract.sol|TestContract.Complex","location":null,"fields":[{"fieldName":"s1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.EVMStructDescriptor","canonicalId":"TestContract.sol|TestContract.Simple","location":null,"fields":[{"fieldName":"x","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"fieldName":"y","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}},{"fieldName":"z1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8}},{"fieldName":"z2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8}},{"fieldName":"b1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}},{"fieldName":"x2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"fieldName":"b2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}}],"name":"TestContract.Simple"}},{"fieldName":"s2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.EVMStructDescriptor","canonicalId":"TestContract.sol|TestContract.Simple","location":null,"fields":[{"fieldName":"x","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"fieldName":"y","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}},{"fieldName":"z1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8}},{"fieldName":"z2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8}},{"fieldName":"b1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}},{"fieldName":"x2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"fieldName":"b2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}}],"name":"TestContract.Simple"}},{"fieldName":"b3","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}}],"name":"TestContract.Complex"},"context":{"#class":"spec.cvlast.typedescriptors.FromVMContext.StateValue"}},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":9,"charByteOffset":12},"end":{"line":9,"charByteOffset":29}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.StorageAccessMarker"}}},"fieldName":"s1","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":9}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.VM","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMStructDescriptor","canonicalId":"TestContract.sol|TestContract.Simple","location":null,"fields":[{"fieldName":"x","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"fieldName":"y","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}},{"fieldName":"z1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8}},{"fieldName":"z2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8}},{"fieldName":"b1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}},{"fieldName":"x2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"fieldName":"b2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}}],"name":"TestContract.Simple"},"context":{"#class":"spec.cvlast.typedescriptors.FromVMContext.StateValue"}},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":9,"charByteOffset":12},"end":{"line":9,"charByteOffset":32}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.StorageAccessMarker"}}},"fieldName":"b1","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":9}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.VM","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$bool"},"context":{"#class":"spec.cvlast.typedescriptors.FromVMContext.StateValue"}},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":9,"charByteOffset":12},"end":{"line":9,"charByteOffset":35}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.StorageAccessMarker"}}},"r":{"#class":"spec.cvlast.CVLExp.RelopExp.ArithRelopExp.GtExp","l":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"x","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":9}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":9,"charByteOffset":40},"end":{"line":9,"charByteOffset":41}}},"twoStateIndex":"NEITHER"},"r":{"#class":"spec.cvlast.CVLExp.Constant.NumberLit","n":"3","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":9}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral","n":"3"},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":9,"charByteOffset":44},"end":{"line":9,"charByteOffset":45}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":9}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":9,"charByteOffset":40},"end":{"line":9,"charByteOffset":45}},"hasParens":true}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":9}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":9,"charByteOffset":12},"end":{"line":9,"charByteOffset":46}}}},"description":null,"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":9}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssignExpCmd:108 I37:27 0x0
		AssertCmd:109 true "sanity bounds check on cvl to vm encoding (unsigned int elements of a user array) of %1$s failed"
		AssignExpCmd:110 R38:4 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(skey_basic:bif 0x0) Apply(skey_basic:bif 0x0))
		AssignExpCmd:110 R39:4 Apply(skey_add:bif R38:4 0x1)
		AssignExpCmd:111 R40:4 AnnotationExp(Select(CANON61!!35:112 R39:113 ) JSON{"key":{"name":"tac.storage.access-paths","type":"analysis.storage.StorageAnalysisResult$AccessPaths","erasureStrategy":"Canonical"},"value":{"paths":[{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.StructAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.MapAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.Root","slot":"0"},"key":{"#class":"vc.data.TACSymbol.Const","value":"0"},"baseSlot":{"#class":"vc.data.TACSymbol.Const","value":"0"},"hashResult":{"#class":"vc.data.TACSymbol.Const","value":"0"}},"offset":{"#class":"analysis.storage.StorageAnalysis.Offset.Bytes","numBytes":"36"}}]}})
		AssumeExpCmd Eq(R40:4 0x0 )
		AssignExpCmd:110 B41:9 false
		AnnotationCmd:110 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.DirectStorageLoad","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"B41","tag":{"#class":"tac.Tag.Bool"},"callIndex":0,"meta":[{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"displayPath":{"#class":"analysis.storage.DisplayPath.FieldAccess","field":"b1","base":{"#class":"analysis.storage.DisplayPath.FieldAccess","field":"s1","base":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Const","value":"0"},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"uint256","numBytes":"20","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"m"}}}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"},"contractInstance":"ce4604a0000000000000000000000001","range":{"specFile":"test.spec","start":{"line":9,"charByteOffset":12},"end":{"line":9,"charByteOffset":35}}}}
		AssignExpCmd:114 I42:15 CANON25:43
		AssignExpCmd:115 I43:16 0x3
		AssignExpCmd:116 B44:9 false
		AssignExpCmd:117 CANON71:62 true
		AnnotationCmd:110 JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":22}
		AnnotationCmd:118 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Havoc","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":10,"charByteOffset":4},"end":{"line":10,"charByteOffset":31}},"targets":[{"#class":"spec.cvlast.CVLExp.FieldSelectExp","structExp":{"#class":"spec.cvlast.CVLExp.ArrayDerefExp","array":{"#class":"spec.cvlast.CVLExp.FieldSelectExp","structExp":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"testContract","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":9}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.CodeContract","name":{"name":"TestContract"}},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":10,"charByteOffset":10},"end":{"line":10,"charByteOffset":22}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.CVLExp$VariableExp$ContractInstanceId","instanceId":"ce4604a0000000000000000000000001"}},"twoStateIndex":"NEITHER"},"fieldName":"m","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":9}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.VM","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMMappingDescriptor","keyType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"valueType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.EVMStructDescriptor","canonicalId":"TestContract.sol|TestContract.Complex","location":null,"fields":[{"fieldName":"s1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.EVMStructDescriptor","canonicalId":"TestContract.sol|TestContract.Simple","location":null,"fields":[{"fieldName":"x","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"fieldName":"y","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}},{"fieldName":"z1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8}},{"fieldName":"z2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8}},{"fieldName":"b1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}},{"fieldName":"x2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"fieldName":"b2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}}],"name":"TestContract.Simple"}},{"fieldName":"s2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.EVMStructDescriptor","canonicalId":"TestContract.sol|TestContract.Simple","location":null,"fields":[{"fieldName":"x","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"fieldName":"y","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}},{"fieldName":"z1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8}},{"fieldName":"z2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8}},{"fieldName":"b1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}},{"fieldName":"x2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"fieldName":"b2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}}],"name":"TestContract.Simple"}},{"fieldName":"b3","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}}],"name":"TestContract.Complex"},"location":null},"context":{"#class":"spec.cvlast.typedescriptors.FromVMContext.StateValue"}},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":10,"charByteOffset":10},"end":{"line":10,"charByteOffset":24}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.StorageAccessMarker"}}},"index":{"#class":"spec.cvlast.CVLExp.Constant.NumberLit","n":"0","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":9}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral","n":"0"},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":10,"charByteOffset":25},"end":{"line":10,"charByteOffset":26}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":9}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.VM","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMStructDescriptor","canonicalId":"TestContract.sol|TestContract.Complex","location":null,"fields":[{"fieldName":"s1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.EVMStructDescriptor","canonicalId":"TestContract.sol|TestContract.Simple","location":null,"fields":[{"fieldName":"x","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"fieldName":"y","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}},{"fieldName":"z1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8}},{"fieldName":"z2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8}},{"fieldName":"b1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}},{"fieldName":"x2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"fieldName":"b2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}}],"name":"TestContract.Simple"}},{"fieldName":"s2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.EVMStructDescriptor","canonicalId":"TestContract.sol|TestContract.Simple","location":null,"fields":[{"fieldName":"x","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"fieldName":"y","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}},{"fieldName":"z1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8}},{"fieldName":"z2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8}},{"fieldName":"b1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}},{"fieldName":"x2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"fieldName":"b2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}}],"name":"TestContract.Simple"}},{"fieldName":"b3","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}}],"name":"TestContract.Complex"},"context":{"#class":"spec.cvlast.typedescriptors.FromVMContext.StateValue"}},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":10,"charByteOffset":10},"end":{"line":10,"charByteOffset":27}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.StorageAccessMarker"}}},"fieldName":"b3","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":9}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.VM","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$bool"},"context":{"#class":"spec.cvlast.typedescriptors.FromVMContext.StateValue"}},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":10,"charByteOffset":10},"end":{"line":10,"charByteOffset":30}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.StorageAccessMarker"}}}],"assumingExp":null,"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":9}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssignExpCmd:119 I45:27 0x0
		AssertCmd:120 true "sanity bounds check on cvl to vm encoding (unsigned int elements of a user array) of %1$s failed"
		AssignExpCmd:121 R46:4 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(skey_basic:bif 0x0) Apply(skey_basic:bif 0x0))
		AssignExpCmd:121 R47:4 Apply(skey_add:bif R46:4 0x8)
		AssignHavocCmd:121 B48:4
		AssignExpCmd:121 R49:4 Ite(B48:4 0x1 0x0 )
		AssignExpCmd:122 CANON77!!50:3 AnnotationExp(Store(CANON77!!3:3 R47:123 R49:4 ) JSON{"key":{"name":"tac.storage.access-paths","type":"analysis.storage.StorageAnalysisResult$AccessPaths","erasureStrategy":"Canonical"},"value":{"paths":[{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.StructAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.MapAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.Root","slot":"0"},"key":{"#class":"vc.data.TACSymbol.Const","value":"0"},"baseSlot":{"#class":"vc.data.TACSymbol.Const","value":"0"},"hashResult":{"#class":"vc.data.TACSymbol.Const","value":"0"}},"offset":{"#class":"analysis.storage.StorageAnalysis.Offset.Bytes","numBytes":"100"}}]}})
		AnnotationCmd:121 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.DirectStorageHavoc","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R49","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"displayPath":{"#class":"analysis.storage.DisplayPath.FieldAccess","field":"b3","base":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Const","value":"0"},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"uint256","numBytes":"20","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"m"}}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"},"contractInstance":"ce4604a0000000000000000000000001","range":{"specFile":"test.spec","start":{"line":10,"charByteOffset":10},"end":{"line":10,"charByteOffset":30}}}}
		AssignExpCmd:124 B51:9 true
		AnnotationCmd:121 JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":23}
		AnnotationCmd:125 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.AssumeCmd.Assume","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":11,"charByteOffset":4},"end":{"line":11,"charByteOffset":44}},"exp":{"#class":"spec.cvlast.CVLExp.RelopExp.EqExp","l":{"#class":"spec.cvlast.CVLExp.FieldSelectExp","structExp":{"#class":"spec.cvlast.CVLExp.ArrayDerefExp","array":{"#class":"spec.cvlast.CVLExp.FieldSelectExp","structExp":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"testContract","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":9}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.CodeContract","name":{"name":"TestContract"}},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":11,"charByteOffset":12},"end":{"line":11,"charByteOffset":24}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.CVLExp$VariableExp$ContractInstanceId","instanceId":"ce4604a0000000000000000000000001"}},"twoStateIndex":"NEITHER"},"fieldName":"m","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":9}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.VM","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMMappingDescriptor","keyType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"valueType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.EVMStructDescriptor","canonicalId":"TestContract.sol|TestContract.Complex","location":null,"fields":[{"fieldName":"s1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.EVMStructDescriptor","canonicalId":"TestContract.sol|TestContract.Simple","location":null,"fields":[{"fieldName":"x","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"fieldName":"y","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}},{"fieldName":"z1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8}},{"fieldName":"z2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8}},{"fieldName":"b1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}},{"fieldName":"x2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"fieldName":"b2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}}],"name":"TestContract.Simple"}},{"fieldName":"s2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.EVMStructDescriptor","canonicalId":"TestContract.sol|TestContract.Simple","location":null,"fields":[{"fieldName":"x","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"fieldName":"y","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}},{"fieldName":"z1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8}},{"fieldName":"z2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8}},{"fieldName":"b1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}},{"fieldName":"x2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"fieldName":"b2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}}],"name":"TestContract.Simple"}},{"fieldName":"b3","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}}],"name":"TestContract.Complex"},"location":null},"context":{"#class":"spec.cvlast.typedescriptors.FromVMContext.StateValue"}},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":11,"charByteOffset":12},"end":{"line":11,"charByteOffset":26}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.StorageAccessMarker"}}},"index":{"#class":"spec.cvlast.CVLExp.Constant.NumberLit","n":"0","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":9}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral","n":"0"},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":11,"charByteOffset":27},"end":{"line":11,"charByteOffset":28}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":9}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.VM","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMStructDescriptor","canonicalId":"TestContract.sol|TestContract.Complex","location":null,"fields":[{"fieldName":"s1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.EVMStructDescriptor","canonicalId":"TestContract.sol|TestContract.Simple","location":null,"fields":[{"fieldName":"x","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"fieldName":"y","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}},{"fieldName":"z1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8}},{"fieldName":"z2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8}},{"fieldName":"b1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}},{"fieldName":"x2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"fieldName":"b2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}}],"name":"TestContract.Simple"}},{"fieldName":"s2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.EVMStructDescriptor","canonicalId":"TestContract.sol|TestContract.Simple","location":null,"fields":[{"fieldName":"x","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"fieldName":"y","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}},{"fieldName":"z1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8}},{"fieldName":"z2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8}},{"fieldName":"b1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}},{"fieldName":"x2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"fieldName":"b2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}}],"name":"TestContract.Simple"}},{"fieldName":"b3","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}}],"name":"TestContract.Complex"},"context":{"#class":"spec.cvlast.typedescriptors.FromVMContext.StateValue"}},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":11,"charByteOffset":12},"end":{"line":11,"charByteOffset":29}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.StorageAccessMarker"}}},"fieldName":"b3","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":9}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.VM","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$bool"},"context":{"#class":"spec.cvlast.typedescriptors.FromVMContext.StateValue"}},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":11,"charByteOffset":12},"end":{"line":11,"charByteOffset":32}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.StorageAccessMarker"}}},"r":{"#class":"spec.cvlast.CVLExp.RelopExp.ArithRelopExp.GtExp","l":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"x","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":9}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":11,"charByteOffset":37},"end":{"line":11,"charByteOffset":38}}},"twoStateIndex":"NEITHER"},"r":{"#class":"spec.cvlast.CVLExp.Constant.NumberLit","n":"5","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":9}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral","n":"5"},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":11,"charByteOffset":41},"end":{"line":11,"charByteOffset":42}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":9}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":11,"charByteOffset":37},"end":{"line":11,"charByteOffset":42}},"hasParens":true}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":9}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":11,"charByteOffset":12},"end":{"line":11,"charByteOffset":43}}}},"description":null,"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":9}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssignExpCmd:126 I52:27 0x0
		AssertCmd:127 true "sanity bounds check on cvl to vm encoding (unsigned int elements of a user array) of %1$s failed"
		AssignExpCmd:128 R53:4 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(skey_basic:bif 0x0) Apply(skey_basic:bif 0x0))
		AssignExpCmd:128 R54:4 Apply(skey_add:bif R53:4 0x8)
		AssignExpCmd:129 R55:4 AnnotationExp(Select(CANON77!!50:130 R54:131 ) JSON{"key":{"name":"tac.storage.access-paths","type":"analysis.storage.StorageAnalysisResult$AccessPaths","erasureStrategy":"Canonical"},"value":{"paths":[{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.StructAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.MapAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.Root","slot":"0"},"key":{"#class":"vc.data.TACSymbol.Const","value":"0"},"baseSlot":{"#class":"vc.data.TACSymbol.Const","value":"0"},"hashResult":{"#class":"vc.data.TACSymbol.Const","value":"0"}},"offset":{"#class":"analysis.storage.StorageAnalysis.Offset.Bytes","numBytes":"100"}}]}})
		AssumeExpCmd Eq(R55:4 0x0 )
		AssignExpCmd:128 B56:9 false
		AnnotationCmd:128 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.DirectStorageLoad","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"B56","tag":{"#class":"tac.Tag.Bool"},"callIndex":0,"meta":[{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"displayPath":{"#class":"analysis.storage.DisplayPath.FieldAccess","field":"b3","base":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Const","value":"0"},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"uint256","numBytes":"20","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"m"}}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"},"contractInstance":"ce4604a0000000000000000000000001","range":{"specFile":"test.spec","start":{"line":11,"charByteOffset":12},"end":{"line":11,"charByteOffset":32}}}}
		AssignExpCmd:132 I57:15 CANON25:43
		AssignExpCmd:133 I58:28 0x5
		AssignExpCmd:134 B59:9 false
		AssignExpCmd:135 CANON87:62 true
		AnnotationCmd:128 JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":24}
		AnnotationCmd:98 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.CVLSnippetCmd.CVLFunctionEnd","callIndex":1,"name":"workOnSComplexCVL"}}
		AnnotationCmd:98 JSON{"key":{"name":"revert.confluence","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:98 "join point of revert handling"
	}
	Block 2_0_0_0_0_0 Succ [] {
		AnnotationCmd:98 JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":20}
		AnnotationCmd:136 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Assert","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":72,"charByteOffset":4},"end":{"line":72,"charByteOffset":16}},"exp":{"#class":"spec.cvlast.CVLExp.FieldSelectExp","structExp":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"s","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":8}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Complex","fields":[{"fieldName":"s1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"s2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"fieldName":"b3","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":72,"charByteOffset":11},"end":{"line":72,"charByteOffset":12}}},"twoStateIndex":"NEITHER"},"fieldName":"b3","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":8}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":72,"charByteOffset":11},"end":{"line":72,"charByteOffset":15}}}},"description":null,"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":8}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AnnotationCmd JSON{"key":{"name":"cvl.trace.data.movement","type":"spec.CVLCompiler$Companion$TraceMeta$CVLMovement","erasureStrategy":"Erased"},"value":{"dst":{"id":"tmp10361037"},"src":{"id":"s876"}}}
		AssignExpCmd:137 B61:9 CANON19:38
		AnnotationCmd JSON{"key":{"name":"cvl.trace.traversal","type":"spec.CVLCompiler$Companion$TraceMeta$ValueTraversal","erasureStrategy":"Erased"},"value":{"lhs":{"#class":"spec.CVLCompiler.Companion.TraceMeta.ValueIdentity.TACVar","t":{"namePrefix":"B61","tag":{"#class":"tac.Tag.Bool"},"callIndex":0,"meta":[{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},"ap":[{"#class":"ReflectivePolymorphicSerializer::spec.CVLCompiler$Companion$TraceMeta$CVLAccessPathStep$Field","f":"b3"}],"base":{"#class":"spec.CVLCompiler.Companion.TraceMeta.ValueIdentity.CVLVar","id":"tmp10361037"}}}
		AssertCmd:138 B61:9 "s.b3"
	}
}
Axioms {
}
Metas {
  "0": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "tacCodesize",
        "maybeTACKeywordOrdinal": 7
      }
    },
    {
      "key": {
        "name": "tac.codesize",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a0000000000000000000000001"
    },
    {
      "key": {
        "name": "tac.no.callindex",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "1": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "tacExtcodesize",
        "maybeTACKeywordOrdinal": 25
      }
    },
    {
      "key": {
        "name": "tac.no.callindex",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "tac.is.extcodesize",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "2": [
    {
      "key": {
        "name": "tac.storage.non-indexed-path.family",
        "type": "analysis.storage.StorageAnalysisResult$StoragePaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "storagePaths": [
          {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.MapAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
                "slot": "0"
              }
            },
            "offset": "1"
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Packed",
        "packedStart": {
          "#class": "vc.data.ScalarizationSort.UnscalarizedBuffer"
        },
        "start": 176
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 8
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
      }
    },
    {
      "key": {
        "name": "tac.storage.non-indexed-path",
        "type": "analysis.storage.StorageAnalysisResult$NonIndexedPath",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
        "base": {
          "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.MapAccess",
          "base": {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
            "slot": "0"
          }
        },
        "offset": "1"
      }
    },
    {
      "key": {
        "name": "tac.storage",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a0000000000000000000000001"
    }
  ],
  "3": [
    {
      "key": {
        "name": "tac.storage.non-indexed-path.family",
        "type": "analysis.storage.StorageAnalysisResult$StoragePaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "storagePaths": [
          {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.MapAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
                "slot": "0"
              }
            },
            "offset": "8"
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Packed",
        "packedStart": {
          "#class": "vc.data.ScalarizationSort.UnscalarizedBuffer"
        },
        "start": 0
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 8
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
      }
    },
    {
      "key": {
        "name": "tac.storage.non-indexed-path",
        "type": "analysis.storage.StorageAnalysisResult$NonIndexedPath",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
        "base": {
          "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.MapAccess",
          "base": {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
            "slot": "0"
          }
        },
        "offset": "8"
      }
    },
    {
      "key": {
        "name": "tac.storage",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a0000000000000000000000001"
    }
  ],
  "4": [
    {
      "key": {
        "name": "tac.is-temp-var",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "5": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.NonTACKeywordEntry",
        "name": "tacContractAt"
      }
    },
    {
      "key": {
        "name": "tac.contract.sym.addr.name",
        "type": "java.lang.String",
        "erasureStrategy": "Erased"
      },
      "value": "ecrecover"
    },
    {
      "key": {
        "name": "tac.contract.sym.addr",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Erased"
      },
      "value": "1"
    }
  ],
  "6": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.NonTACKeywordEntry",
        "name": "tacContractAt"
      }
    },
    {
      "key": {
        "name": "tac.contract.sym.addr.name",
        "type": "java.lang.String",
        "erasureStrategy": "Erased"
      },
      "value": "sha256"
    },
    {
      "key": {
        "name": "tac.contract.sym.addr",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Erased"
      },
      "value": "2"
    }
  ],
  "7": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.NonTACKeywordEntry",
        "name": "tacContractAt"
      }
    },
    {
      "key": {
        "name": "tac.contract.sym.addr.name",
        "type": "java.lang.String",
        "erasureStrategy": "Erased"
      },
      "value": "identity"
    },
    {
      "key": {
        "name": "tac.contract.sym.addr",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Erased"
      },
      "value": "4"
    }
  ],
  "8": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.NonTACKeywordEntry",
        "name": "tacContractAt"
      }
    },
    {
      "key": {
        "name": "tac.contract.sym.addr.name",
        "type": "java.lang.String",
        "erasureStrategy": "Erased"
      },
      "value": "TestContract"
    },
    {
      "key": {
        "name": "tac.contract.sym.addr",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Erased"
      },
      "value": "ce4604a0000000000000000000000001"
    }
  ],
  "9": [
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
      }
    }
  ],
  "10": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "TestContract.Complex",
          "fields": [
            {
              "fieldName": "s1",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "s2",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "b3",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "s1",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "TestContract.Simple",
              "fields": [
                {
                  "fieldName": "x",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "y",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "z1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "z2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "b1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                },
                {
                  "fieldName": "x2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "b2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                }
              ]
            }
          },
          {
            "fieldName": "b1",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
      }
    }
  ],
  "11": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "TestContract.Complex",
          "fields": [
            {
              "fieldName": "s1",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "s2",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "b3",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "s1",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "TestContract.Simple",
              "fields": [
                {
                  "fieldName": "x",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "y",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "z1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "z2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "b1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                },
                {
                  "fieldName": "x2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "b2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                }
              ]
            }
          },
          {
            "fieldName": "b2",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
      }
    }
  ],
  "12": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "TestContract.Complex",
          "fields": [
            {
              "fieldName": "s1",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "s2",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "b3",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "s2",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "TestContract.Simple",
              "fields": [
                {
                  "fieldName": "x",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "y",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "z1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "z2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "b1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                },
                {
                  "fieldName": "x2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "b2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                }
              ]
            }
          },
          {
            "fieldName": "b1",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
      }
    }
  ],
  "13": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "TestContract.Complex",
          "fields": [
            {
              "fieldName": "s1",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "s2",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "b3",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "s2",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "TestContract.Simple",
              "fields": [
                {
                  "fieldName": "x",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "y",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "z1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "z2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "b1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                },
                {
                  "fieldName": "x2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "b2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                }
              ]
            }
          },
          {
            "fieldName": "b2",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
      }
    }
  ],
  "14": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "TestContract.Complex",
          "fields": [
            {
              "fieldName": "s1",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "s2",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "b3",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "b3",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
      }
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "s"
    }
  ],
  "15": [
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
        "k": 256
      }
    }
  ],
  "16": [
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral",
        "n": "3"
      }
    }
  ],
  "17": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "TestContract.Complex",
          "fields": [
            {
              "fieldName": "s1",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "s2",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "b3",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "s1",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "TestContract.Simple",
              "fields": [
                {
                  "fieldName": "x",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "y",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "z1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "z2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "b1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                },
                {
                  "fieldName": "x2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "b2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                }
              ]
            }
          },
          {
            "fieldName": "x",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
              "k": 256
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
        "k": 256
      }
    }
  ],
  "18": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "TestContract.Complex",
          "fields": [
            {
              "fieldName": "s1",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "s2",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "b3",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "s1",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "TestContract.Simple",
              "fields": [
                {
                  "fieldName": "x",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "y",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "z1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "z2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "b1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                },
                {
                  "fieldName": "x2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "b2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                }
              ]
            }
          },
          {
            "fieldName": "y",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
      }
    }
  ],
  "19": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "TestContract.Complex",
          "fields": [
            {
              "fieldName": "s1",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "s2",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "b3",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "s1",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "TestContract.Simple",
              "fields": [
                {
                  "fieldName": "x",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "y",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "z1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "z2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "b1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                },
                {
                  "fieldName": "x2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "b2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                }
              ]
            }
          },
          {
            "fieldName": "z1",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
              "k": 8
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
        "k": 8
      }
    }
  ],
  "20": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "TestContract.Complex",
          "fields": [
            {
              "fieldName": "s1",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "s2",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "b3",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "s1",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "TestContract.Simple",
              "fields": [
                {
                  "fieldName": "x",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "y",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "z1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "z2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "b1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                },
                {
                  "fieldName": "x2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "b2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                }
              ]
            }
          },
          {
            "fieldName": "z2",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
              "k": 8
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
        "k": 8
      }
    }
  ],
  "21": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "TestContract.Complex",
          "fields": [
            {
              "fieldName": "s1",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "s2",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "b3",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "s1",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "TestContract.Simple",
              "fields": [
                {
                  "fieldName": "x",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "y",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "z1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "z2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "b1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                },
                {
                  "fieldName": "x2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "b2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                }
              ]
            }
          },
          {
            "fieldName": "x2",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
              "k": 256
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
        "k": 256
      }
    }
  ],
  "22": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "TestContract.Complex",
          "fields": [
            {
              "fieldName": "s1",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "s2",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "b3",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "s2",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "TestContract.Simple",
              "fields": [
                {
                  "fieldName": "x",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "y",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "z1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "z2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "b1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                },
                {
                  "fieldName": "x2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "b2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                }
              ]
            }
          },
          {
            "fieldName": "x",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
              "k": 256
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
        "k": 256
      }
    }
  ],
  "23": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "TestContract.Complex",
          "fields": [
            {
              "fieldName": "s1",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "s2",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "b3",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "s2",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "TestContract.Simple",
              "fields": [
                {
                  "fieldName": "x",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "y",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "z1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "z2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "b1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                },
                {
                  "fieldName": "x2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "b2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                }
              ]
            }
          },
          {
            "fieldName": "y",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
      }
    }
  ],
  "24": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "TestContract.Complex",
          "fields": [
            {
              "fieldName": "s1",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "s2",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "b3",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "s2",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "TestContract.Simple",
              "fields": [
                {
                  "fieldName": "x",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "y",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "z1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "z2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "b1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                },
                {
                  "fieldName": "x2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "b2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                }
              ]
            }
          },
          {
            "fieldName": "z1",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
              "k": 8
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
        "k": 8
      }
    }
  ],
  "25": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "TestContract.Complex",
          "fields": [
            {
              "fieldName": "s1",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "s2",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "b3",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "s2",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "TestContract.Simple",
              "fields": [
                {
                  "fieldName": "x",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "y",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "z1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "z2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "b1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                },
                {
                  "fieldName": "x2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "b2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                }
              ]
            }
          },
          {
            "fieldName": "z2",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
              "k": 8
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
        "k": 8
      }
    }
  ],
  "26": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "TestContract.Complex",
          "fields": [
            {
              "fieldName": "s1",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "s2",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "b3",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "s2",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "TestContract.Simple",
              "fields": [
                {
                  "fieldName": "x",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "y",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "z1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "z2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "b1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                },
                {
                  "fieldName": "x2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "b2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                }
              ]
            }
          },
          {
            "fieldName": "x2",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
              "k": 256
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
        "k": 256
      }
    }
  ],
  "27": [
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral",
        "n": "0"
      }
    }
  ],
  "28": [
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral",
        "n": "5"
      }
    }
  ],
  "29": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "TestContract.Complex",
          "fields": [
            {
              "fieldName": "s1",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "s2",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "b3",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "s1",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "TestContract.Simple",
              "fields": [
                {
                  "fieldName": "x",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "y",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "z1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "z2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "b1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                },
                {
                  "fieldName": "x2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "b2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                }
              ]
            }
          },
          {
            "fieldName": "y",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Rule",
        "range": {
          "#class": "utils.Range.Range",
          "specFile": "test.spec",
          "start": {
            "line": 70,
            "charByteOffset": 4
          },
          "end": {
            "line": 70,
            "charByteOffset": 27
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "s.s1.y"
    }
  ],
  "30": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "TestContract.Complex",
          "fields": [
            {
              "fieldName": "s1",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "s2",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "b3",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "s1",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "TestContract.Simple",
              "fields": [
                {
                  "fieldName": "x",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "y",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "z1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "z2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "b1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                },
                {
                  "fieldName": "x2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "b2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                }
              ]
            }
          },
          {
            "fieldName": "z1",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
              "k": 8
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Rule",
        "range": {
          "#class": "utils.Range.Range",
          "specFile": "test.spec",
          "start": {
            "line": 70,
            "charByteOffset": 4
          },
          "end": {
            "line": 70,
            "charByteOffset": 27
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
        "k": 8
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "s.s1.z1"
    }
  ],
  "31": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "TestContract.Complex",
          "fields": [
            {
              "fieldName": "s1",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "s2",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "b3",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "s1",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "TestContract.Simple",
              "fields": [
                {
                  "fieldName": "x",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "y",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "z1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "z2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "b1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                },
                {
                  "fieldName": "x2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "b2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                }
              ]
            }
          },
          {
            "fieldName": "z2",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
              "k": 8
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Rule",
        "range": {
          "#class": "utils.Range.Range",
          "specFile": "test.spec",
          "start": {
            "line": 70,
            "charByteOffset": 4
          },
          "end": {
            "line": 70,
            "charByteOffset": 27
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
        "k": 8
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "s.s1.z2"
    }
  ],
  "32": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "TestContract.Complex",
          "fields": [
            {
              "fieldName": "s1",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "s2",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "b3",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "s1",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "TestContract.Simple",
              "fields": [
                {
                  "fieldName": "x",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "y",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "z1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "z2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "b1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                },
                {
                  "fieldName": "x2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "b2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                }
              ]
            }
          },
          {
            "fieldName": "x2",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
              "k": 256
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Rule",
        "range": {
          "#class": "utils.Range.Range",
          "specFile": "test.spec",
          "start": {
            "line": 70,
            "charByteOffset": 4
          },
          "end": {
            "line": 70,
            "charByteOffset": 27
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
        "k": 256
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "s.s1.x2"
    }
  ],
  "33": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "TestContract.Complex",
          "fields": [
            {
              "fieldName": "s1",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "s2",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "b3",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "s2",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "TestContract.Simple",
              "fields": [
                {
                  "fieldName": "x",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "y",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "z1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "z2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "b1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                },
                {
                  "fieldName": "x2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "b2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                }
              ]
            }
          },
          {
            "fieldName": "x",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
              "k": 256
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Rule",
        "range": {
          "#class": "utils.Range.Range",
          "specFile": "test.spec",
          "start": {
            "line": 70,
            "charByteOffset": 4
          },
          "end": {
            "line": 70,
            "charByteOffset": 27
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
        "k": 256
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "s.s2.x"
    }
  ],
  "34": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "TestContract.Complex",
          "fields": [
            {
              "fieldName": "s1",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "s2",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "b3",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "s2",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "TestContract.Simple",
              "fields": [
                {
                  "fieldName": "x",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "y",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "z1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "z2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "b1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                },
                {
                  "fieldName": "x2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "b2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                }
              ]
            }
          },
          {
            "fieldName": "y",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Rule",
        "range": {
          "#class": "utils.Range.Range",
          "specFile": "test.spec",
          "start": {
            "line": 70,
            "charByteOffset": 4
          },
          "end": {
            "line": 70,
            "charByteOffset": 27
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "s.s2.y"
    }
  ],
  "35": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "TestContract.Complex",
          "fields": [
            {
              "fieldName": "s1",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "s2",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "b3",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "s2",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "TestContract.Simple",
              "fields": [
                {
                  "fieldName": "x",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "y",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "z1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "z2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "b1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                },
                {
                  "fieldName": "x2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "b2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                }
              ]
            }
          },
          {
            "fieldName": "z1",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
              "k": 8
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Rule",
        "range": {
          "#class": "utils.Range.Range",
          "specFile": "test.spec",
          "start": {
            "line": 70,
            "charByteOffset": 4
          },
          "end": {
            "line": 70,
            "charByteOffset": 27
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
        "k": 8
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "s.s2.z1"
    }
  ],
  "36": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "TestContract.Complex",
          "fields": [
            {
              "fieldName": "s1",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "s2",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "b3",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "s2",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "TestContract.Simple",
              "fields": [
                {
                  "fieldName": "x",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "y",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "z1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "z2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "b1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                },
                {
                  "fieldName": "x2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "b2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                }
              ]
            }
          },
          {
            "fieldName": "z2",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
              "k": 8
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Rule",
        "range": {
          "#class": "utils.Range.Range",
          "specFile": "test.spec",
          "start": {
            "line": 70,
            "charByteOffset": 4
          },
          "end": {
            "line": 70,
            "charByteOffset": 27
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
        "k": 8
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "s.s2.z2"
    }
  ],
  "37": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "TestContract.Complex",
          "fields": [
            {
              "fieldName": "s1",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "s2",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "b3",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "s2",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "TestContract.Simple",
              "fields": [
                {
                  "fieldName": "x",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "y",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "z1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "z2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "b1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                },
                {
                  "fieldName": "x2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "b2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                }
              ]
            }
          },
          {
            "fieldName": "x2",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
              "k": 256
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Rule",
        "range": {
          "#class": "utils.Range.Range",
          "specFile": "test.spec",
          "start": {
            "line": 70,
            "charByteOffset": 4
          },
          "end": {
            "line": 70,
            "charByteOffset": 27
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
        "k": 256
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "s.s2.x2"
    }
  ],
  "38": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "TestContract.Complex",
          "fields": [
            {
              "fieldName": "s1",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "s2",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "b3",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "b3",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Rule",
        "range": {
          "#class": "utils.Range.Range",
          "specFile": "test.spec",
          "start": {
            "line": 70,
            "charByteOffset": 4
          },
          "end": {
            "line": 70,
            "charByteOffset": 27
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "s.b3"
    }
  ],
  "39": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "TestContract.Complex",
          "fields": [
            {
              "fieldName": "s1",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "s2",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "b3",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "s1",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "TestContract.Simple",
              "fields": [
                {
                  "fieldName": "x",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "y",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "z1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "z2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "b1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                },
                {
                  "fieldName": "x2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "b2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                }
              ]
            }
          },
          {
            "fieldName": "b1",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Rule",
        "range": {
          "#class": "utils.Range.Range",
          "specFile": "test.spec",
          "start": {
            "line": 70,
            "charByteOffset": 4
          },
          "end": {
            "line": 70,
            "charByteOffset": 27
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "s.s1.b1"
    }
  ],
  "40": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "TestContract.Complex",
          "fields": [
            {
              "fieldName": "s1",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "s2",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "b3",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "s1",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "TestContract.Simple",
              "fields": [
                {
                  "fieldName": "x",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "y",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "z1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "z2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "b1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                },
                {
                  "fieldName": "x2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "b2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                }
              ]
            }
          },
          {
            "fieldName": "b2",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Rule",
        "range": {
          "#class": "utils.Range.Range",
          "specFile": "test.spec",
          "start": {
            "line": 70,
            "charByteOffset": 4
          },
          "end": {
            "line": 70,
            "charByteOffset": 27
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "s.s1.b2"
    }
  ],
  "41": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "TestContract.Complex",
          "fields": [
            {
              "fieldName": "s1",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "s2",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "b3",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "s2",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "TestContract.Simple",
              "fields": [
                {
                  "fieldName": "x",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "y",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "z1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "z2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "b1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                },
                {
                  "fieldName": "x2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "b2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                }
              ]
            }
          },
          {
            "fieldName": "b1",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Rule",
        "range": {
          "#class": "utils.Range.Range",
          "specFile": "test.spec",
          "start": {
            "line": 70,
            "charByteOffset": 4
          },
          "end": {
            "line": 70,
            "charByteOffset": 27
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "s.s2.b1"
    }
  ],
  "42": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "TestContract.Complex",
          "fields": [
            {
              "fieldName": "s1",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "s2",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "b3",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "s2",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "TestContract.Simple",
              "fields": [
                {
                  "fieldName": "x",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "y",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "z1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "z2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "b1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                },
                {
                  "fieldName": "x2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "b2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                }
              ]
            }
          },
          {
            "fieldName": "b2",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Rule",
        "range": {
          "#class": "utils.Range.Range",
          "specFile": "test.spec",
          "start": {
            "line": 70,
            "charByteOffset": 4
          },
          "end": {
            "line": 70,
            "charByteOffset": 27
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "s.s2.b2"
    }
  ],
  "43": [
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Function",
        "range": {
          "#class": "utils.Range.Range",
          "specFile": "test.spec",
          "start": {
            "line": 7,
            "charByteOffset": 27
          },
          "end": {
            "line": 7,
            "charByteOffset": 33
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
        "k": 256
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "x"
    }
  ],
  "44": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "TestContract.Complex",
          "fields": [
            {
              "fieldName": "s1",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "s2",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "b3",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "b3",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
      }
    }
  ],
  "45": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "TestContract.Complex",
          "fields": [
            {
              "fieldName": "s1",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "s2",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "b3",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "s1",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "TestContract.Simple",
              "fields": [
                {
                  "fieldName": "x",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "y",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "z1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "z2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "b1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                },
                {
                  "fieldName": "x2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "b2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                }
              ]
            }
          },
          {
            "fieldName": "x",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
              "k": 256
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Function",
        "range": {
          "#class": "utils.Range.Range",
          "specFile": "test.spec",
          "start": {
            "line": 7,
            "charByteOffset": 35
          },
          "end": {
            "line": 7,
            "charByteOffset": 57
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
        "k": 256
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "s.s1.x"
    }
  ],
  "46": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "TestContract.Complex",
          "fields": [
            {
              "fieldName": "s1",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "s2",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "b3",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "s1",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "TestContract.Simple",
              "fields": [
                {
                  "fieldName": "x",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "y",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "z1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "z2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "b1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                },
                {
                  "fieldName": "x2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "b2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                }
              ]
            }
          },
          {
            "fieldName": "y",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Function",
        "range": {
          "#class": "utils.Range.Range",
          "specFile": "test.spec",
          "start": {
            "line": 7,
            "charByteOffset": 35
          },
          "end": {
            "line": 7,
            "charByteOffset": 57
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "s.s1.y"
    }
  ],
  "47": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "TestContract.Complex",
          "fields": [
            {
              "fieldName": "s1",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "s2",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "b3",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "s1",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "TestContract.Simple",
              "fields": [
                {
                  "fieldName": "x",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "y",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "z1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "z2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "b1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                },
                {
                  "fieldName": "x2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "b2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                }
              ]
            }
          },
          {
            "fieldName": "z1",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
              "k": 8
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Function",
        "range": {
          "#class": "utils.Range.Range",
          "specFile": "test.spec",
          "start": {
            "line": 7,
            "charByteOffset": 35
          },
          "end": {
            "line": 7,
            "charByteOffset": 57
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
        "k": 8
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "s.s1.z1"
    }
  ],
  "48": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "TestContract.Complex",
          "fields": [
            {
              "fieldName": "s1",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "s2",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "b3",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "s1",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "TestContract.Simple",
              "fields": [
                {
                  "fieldName": "x",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "y",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "z1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "z2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "b1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                },
                {
                  "fieldName": "x2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "b2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                }
              ]
            }
          },
          {
            "fieldName": "z2",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
              "k": 8
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Function",
        "range": {
          "#class": "utils.Range.Range",
          "specFile": "test.spec",
          "start": {
            "line": 7,
            "charByteOffset": 35
          },
          "end": {
            "line": 7,
            "charByteOffset": 57
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
        "k": 8
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "s.s1.z2"
    }
  ],
  "49": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "TestContract.Complex",
          "fields": [
            {
              "fieldName": "s1",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "s2",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "b3",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "s1",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "TestContract.Simple",
              "fields": [
                {
                  "fieldName": "x",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "y",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "z1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "z2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "b1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                },
                {
                  "fieldName": "x2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "b2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                }
              ]
            }
          },
          {
            "fieldName": "b1",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Function",
        "range": {
          "#class": "utils.Range.Range",
          "specFile": "test.spec",
          "start": {
            "line": 7,
            "charByteOffset": 35
          },
          "end": {
            "line": 7,
            "charByteOffset": 57
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "s.s1.b1"
    }
  ],
  "50": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "TestContract.Complex",
          "fields": [
            {
              "fieldName": "s1",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "s2",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "b3",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "s1",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "TestContract.Simple",
              "fields": [
                {
                  "fieldName": "x",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "y",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "z1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "z2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "b1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                },
                {
                  "fieldName": "x2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "b2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                }
              ]
            }
          },
          {
            "fieldName": "x2",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
              "k": 256
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Function",
        "range": {
          "#class": "utils.Range.Range",
          "specFile": "test.spec",
          "start": {
            "line": 7,
            "charByteOffset": 35
          },
          "end": {
            "line": 7,
            "charByteOffset": 57
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
        "k": 256
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "s.s1.x2"
    }
  ],
  "51": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "TestContract.Complex",
          "fields": [
            {
              "fieldName": "s1",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "s2",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "b3",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "s1",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "TestContract.Simple",
              "fields": [
                {
                  "fieldName": "x",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "y",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "z1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "z2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "b1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                },
                {
                  "fieldName": "x2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "b2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                }
              ]
            }
          },
          {
            "fieldName": "b2",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Function",
        "range": {
          "#class": "utils.Range.Range",
          "specFile": "test.spec",
          "start": {
            "line": 7,
            "charByteOffset": 35
          },
          "end": {
            "line": 7,
            "charByteOffset": 57
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "s.s1.b2"
    }
  ],
  "52": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "TestContract.Complex",
          "fields": [
            {
              "fieldName": "s1",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "s2",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "b3",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "s2",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "TestContract.Simple",
              "fields": [
                {
                  "fieldName": "x",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "y",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "z1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "z2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "b1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                },
                {
                  "fieldName": "x2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "b2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                }
              ]
            }
          },
          {
            "fieldName": "x",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
              "k": 256
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Function",
        "range": {
          "#class": "utils.Range.Range",
          "specFile": "test.spec",
          "start": {
            "line": 7,
            "charByteOffset": 35
          },
          "end": {
            "line": 7,
            "charByteOffset": 57
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
        "k": 256
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "s.s2.x"
    }
  ],
  "53": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "TestContract.Complex",
          "fields": [
            {
              "fieldName": "s1",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "s2",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "b3",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "s2",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "TestContract.Simple",
              "fields": [
                {
                  "fieldName": "x",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "y",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "z1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "z2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "b1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                },
                {
                  "fieldName": "x2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "b2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                }
              ]
            }
          },
          {
            "fieldName": "y",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Function",
        "range": {
          "#class": "utils.Range.Range",
          "specFile": "test.spec",
          "start": {
            "line": 7,
            "charByteOffset": 35
          },
          "end": {
            "line": 7,
            "charByteOffset": 57
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "s.s2.y"
    }
  ],
  "54": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "TestContract.Complex",
          "fields": [
            {
              "fieldName": "s1",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "s2",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "b3",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "s2",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "TestContract.Simple",
              "fields": [
                {
                  "fieldName": "x",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "y",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "z1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "z2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "b1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                },
                {
                  "fieldName": "x2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "b2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                }
              ]
            }
          },
          {
            "fieldName": "z1",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
              "k": 8
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Function",
        "range": {
          "#class": "utils.Range.Range",
          "specFile": "test.spec",
          "start": {
            "line": 7,
            "charByteOffset": 35
          },
          "end": {
            "line": 7,
            "charByteOffset": 57
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
        "k": 8
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "s.s2.z1"
    }
  ],
  "55": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "TestContract.Complex",
          "fields": [
            {
              "fieldName": "s1",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "s2",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "b3",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "s2",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "TestContract.Simple",
              "fields": [
                {
                  "fieldName": "x",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "y",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "z1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "z2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "b1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                },
                {
                  "fieldName": "x2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "b2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                }
              ]
            }
          },
          {
            "fieldName": "z2",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
              "k": 8
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Function",
        "range": {
          "#class": "utils.Range.Range",
          "specFile": "test.spec",
          "start": {
            "line": 7,
            "charByteOffset": 35
          },
          "end": {
            "line": 7,
            "charByteOffset": 57
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
        "k": 8
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "s.s2.z2"
    }
  ],
  "56": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "TestContract.Complex",
          "fields": [
            {
              "fieldName": "s1",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "s2",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "b3",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "s2",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "TestContract.Simple",
              "fields": [
                {
                  "fieldName": "x",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "y",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "z1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "z2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "b1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                },
                {
                  "fieldName": "x2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "b2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                }
              ]
            }
          },
          {
            "fieldName": "b1",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Function",
        "range": {
          "#class": "utils.Range.Range",
          "specFile": "test.spec",
          "start": {
            "line": 7,
            "charByteOffset": 35
          },
          "end": {
            "line": 7,
            "charByteOffset": 57
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "s.s2.b1"
    }
  ],
  "57": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "TestContract.Complex",
          "fields": [
            {
              "fieldName": "s1",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "s2",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "b3",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "s2",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "TestContract.Simple",
              "fields": [
                {
                  "fieldName": "x",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "y",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "z1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "z2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "b1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                },
                {
                  "fieldName": "x2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "b2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                }
              ]
            }
          },
          {
            "fieldName": "x2",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
              "k": 256
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Function",
        "range": {
          "#class": "utils.Range.Range",
          "specFile": "test.spec",
          "start": {
            "line": 7,
            "charByteOffset": 35
          },
          "end": {
            "line": 7,
            "charByteOffset": 57
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
        "k": 256
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "s.s2.x2"
    }
  ],
  "58": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "TestContract.Complex",
          "fields": [
            {
              "fieldName": "s1",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "s2",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "b3",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "s2",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "TestContract.Simple",
              "fields": [
                {
                  "fieldName": "x",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "y",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "z1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "z2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "b1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                },
                {
                  "fieldName": "x2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "b2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                }
              ]
            }
          },
          {
            "fieldName": "b2",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Function",
        "range": {
          "#class": "utils.Range.Range",
          "specFile": "test.spec",
          "start": {
            "line": 7,
            "charByteOffset": 35
          },
          "end": {
            "line": 7,
            "charByteOffset": 57
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "s.s2.b2"
    }
  ],
  "59": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "TestContract.Complex",
          "fields": [
            {
              "fieldName": "s1",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "s2",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "b3",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "b3",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Function",
        "range": {
          "#class": "utils.Range.Range",
          "specFile": "test.spec",
          "start": {
            "line": 7,
            "charByteOffset": 35
          },
          "end": {
            "line": 7,
            "charByteOffset": 57
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "s.b3"
    }
  ],
  "60": [
    {
      "key": {
        "name": "tac.is-temp-var",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "tac.storage.access-paths",
        "type": "analysis.storage.StorageAnalysisResult$AccessPaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.StorageAnalysis.AnalysisPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysis.AnalysisPath.MapAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysis.AnalysisPath.Root",
                "slot": "0"
              },
              "key": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "CANON56",
                "tag": {
                  "#class": "tac.Tag.Int"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "cvl.type",
                      "type": "spec.cvlast.CVLType$PureCVLType",
                      "erasureStrategy": "CallTrace"
                    },
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral",
                      "n": "0"
                    }
                  }
                ]
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Const",
                "value": "0"
              },
              "hashResult": {
                "#class": "vc.data.TACSymbol.Const",
                "value": "0"
              }
            },
            "offset": {
              "#class": "analysis.storage.StorageAnalysis.Offset.Bytes",
              "numBytes": "36"
            }
          }
        ]
      }
    }
  ],
  "61": [
    {
      "key": {
        "name": "tac.is-temp-var",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "tac.storage.access-paths",
        "type": "analysis.storage.StorageAnalysisResult$AccessPaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.StorageAnalysis.AnalysisPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysis.AnalysisPath.MapAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysis.AnalysisPath.Root",
                "slot": "0"
              },
              "key": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "CANON63",
                "tag": {
                  "#class": "tac.Tag.Int"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "cvl.type",
                      "type": "spec.cvlast.CVLType$PureCVLType",
                      "erasureStrategy": "CallTrace"
                    },
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral",
                      "n": "0"
                    }
                  }
                ]
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Const",
                "value": "0"
              },
              "hashResult": {
                "#class": "vc.data.TACSymbol.Const",
                "value": "0"
              }
            },
            "offset": {
              "#class": "analysis.storage.StorageAnalysis.Offset.Bytes",
              "numBytes": "36"
            }
          }
        ]
      }
    }
  ],
  "62": [
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    }
  ],
  "63": [
    {
      "key": {
        "name": "tac.is-temp-var",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "tac.storage.access-paths",
        "type": "analysis.storage.StorageAnalysisResult$AccessPaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.StorageAnalysis.AnalysisPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysis.AnalysisPath.MapAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysis.AnalysisPath.Root",
                "slot": "0"
              },
              "key": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "CANON72",
                "tag": {
                  "#class": "tac.Tag.Int"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "cvl.type",
                      "type": "spec.cvlast.CVLType$PureCVLType",
                      "erasureStrategy": "CallTrace"
                    },
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral",
                      "n": "0"
                    }
                  }
                ]
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Const",
                "value": "0"
              },
              "hashResult": {
                "#class": "vc.data.TACSymbol.Const",
                "value": "0"
              }
            },
            "offset": {
              "#class": "analysis.storage.StorageAnalysis.Offset.Bytes",
              "numBytes": "100"
            }
          }
        ]
      }
    }
  ],
  "64": [
    {
      "key": {
        "name": "tac.is-temp-var",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "tac.storage.access-paths",
        "type": "analysis.storage.StorageAnalysisResult$AccessPaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.StorageAnalysis.AnalysisPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysis.AnalysisPath.MapAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysis.AnalysisPath.Root",
                "slot": "0"
              },
              "key": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "CANON79",
                "tag": {
                  "#class": "tac.Tag.Int"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "cvl.type",
                      "type": "spec.cvlast.CVLType$PureCVLType",
                      "erasureStrategy": "CallTrace"
                    },
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral",
                      "n": "0"
                    }
                  }
                ]
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Const",
                "value": "0"
              },
              "hashResult": {
                "#class": "vc.data.TACSymbol.Const",
                "value": "0"
              }
            },
            "offset": {
              "#class": "analysis.storage.StorageAnalysis.Offset.Bytes",
              "numBytes": "100"
            }
          }
        ]
      }
    }
  ],
  "65": [
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.CodeContract",
        "name": {
          "name": "TestContract"
        }
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "tac.no.callindex",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "testContract"
    }
  ],
  "66": [
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.CodeContract",
        "name": {
          "name": "TestContract"
        }
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "tac.no.callindex",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "currentContract"
    }
  ],
  "67": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "TestContract.Complex",
          "fields": [
            {
              "fieldName": "s1",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "s2",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Simple",
                "fields": [
                  {
                    "fieldName": "x",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "y",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "z1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "z2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 8
                    }
                  },
                  {
                    "fieldName": "b1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  },
                  {
                    "fieldName": "x2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "b2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "b3",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "s1",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "TestContract.Simple",
              "fields": [
                {
                  "fieldName": "x",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "y",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "z1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "z2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 8
                  }
                },
                {
                  "fieldName": "b1",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                },
                {
                  "fieldName": "x2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "b2",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                  }
                }
              ]
            }
          },
          {
            "fieldName": "x",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
              "k": 256
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Rule",
        "range": {
          "#class": "utils.Range.Range",
          "specFile": "test.spec",
          "start": {
            "line": 70,
            "charByteOffset": 4
          },
          "end": {
            "line": 70,
            "charByteOffset": 27
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
        "k": 256
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "s.s1.x"
    }
  ],
  "68": [
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Rule",
        "range": {
          "#class": "utils.Range.Range",
          "specFile": "test.spec",
          "start": {
            "line": 68,
            "charByteOffset": 22
          },
          "end": {
            "line": 68,
            "charByteOffset": 28
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
        "k": 256
      }
    },
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    },
    {
      "key": {
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "x"
    }
  ],
  "69": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 0
    }
  ],
  "70": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1
    }
  ],
  "71": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 2
    }
  ],
  "72": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.NonTACKeywordEntry",
        "name": "tacContractAt"
      }
    },
    {
      "key": {
        "name": "tac.contract.sym.addr.name",
        "type": "java.lang.String",
        "erasureStrategy": "Erased"
      },
      "value": "TestContract"
    },
    {
      "key": {
        "name": "tac.contract.sym.addr",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Erased"
      },
      "value": "ce4604a0000000000000000000000001"
    },
    {
      "key": {
        "name": "tac.non.zero.var",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "73": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 3
    }
  ],
  "74": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 4
    }
  ],
  "75": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 5
    }
  ],
  "76": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 6
    }
  ],
  "77": [
    {
      "key": {
        "name": "tac.is-temp-var",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "tac.non.zero.var",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "78": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "tacCodesize",
        "maybeTACKeywordOrdinal": 7
      }
    },
    {
      "key": {
        "name": "tac.codesize",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a0000000000000000000000001"
    },
    {
      "key": {
        "name": "tac.no.callindex",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "tac.non.zero.var",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "79": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 7
    }
  ],
  "80": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 8
    }
  ],
  "81": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 9
    }
  ],
  "82": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 10
    }
  ],
  "83": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 11
    }
  ],
  "84": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 12
    }
  ],
  "85": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 13
    }
  ],
  "86": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 14
    }
  ],
  "87": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 15
    }
  ],
  "88": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 16
    }
  ],
  "89": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 17
    }
  ],
  "90": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 18
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "test.spec",
        "start": {
          "line": 69,
          "charByteOffset": 4
        },
        "end": {
          "line": 69,
          "charByteOffset": 18
        }
      }
    }
  ],
  "91": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.NullaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.VariableExp",
          "id": "x",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 8
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                  ],
                  "innerScope": null
                }
              }
            },
            "type": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
              "k": 256
            },
            "range": {
              "#class": "utils.Range.Range",
              "specFile": "test.spec",
              "start": {
                "line": 69,
                "charByteOffset": 12
              },
              "end": {
                "line": 69,
                "charByteOffset": 13
              }
            }
          },
          "twoStateIndex": "NEITHER"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "test.spec",
        "start": {
          "line": 69,
          "charByteOffset": 4
        },
        "end": {
          "line": 69,
          "charByteOffset": 18
        }
      }
    }
  ],
  "92": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.NullaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
          "n": "3",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 8
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                  ],
                  "innerScope": null
                }
              }
            },
            "type": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral",
              "n": "3"
            },
            "range": {
              "#class": "utils.Range.Range",
              "specFile": "test.spec",
              "start": {
                "line": 69,
                "charByteOffset": 16
              },
              "end": {
                "line": 69,
                "charByteOffset": 17
              }
            }
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "test.spec",
        "start": {
          "line": 69,
          "charByteOffset": 4
        },
        "end": {
          "line": 69,
          "charByteOffset": 18
        }
      }
    }
  ],
  "93": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.BinaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.RelopExp.ArithRelopExp.LtExp",
          "l": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "x",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 8
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                "k": 256
              },
              "range": {
                "#class": "utils.Range.Range",
                "specFile": "test.spec",
                "start": {
                  "line": 69,
                  "charByteOffset": 12
                },
                "end": {
                  "line": 69,
                  "charByteOffset": 13
                }
              }
            },
            "twoStateIndex": "NEITHER"
          },
          "r": {
            "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
            "n": "3",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 8
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral",
                "n": "3"
              },
              "range": {
                "#class": "utils.Range.Range",
                "specFile": "test.spec",
                "start": {
                  "line": 69,
                  "charByteOffset": 16
                },
                "end": {
                  "line": 69,
                  "charByteOffset": 17
                }
              }
            }
          },
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 8
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                  ],
                  "innerScope": null
                }
              }
            },
            "type": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
            },
            "range": {
              "#class": "utils.Range.Range",
              "specFile": "test.spec",
              "start": {
                "line": 69,
                "charByteOffset": 12
              },
              "end": {
                "line": 69,
                "charByteOffset": 17
              }
            }
          }
        },
        "o1": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "I11",
            "tag": {
              "#class": "tac.Tag.Int"
            },
            "callIndex": 0,
            "meta": [
              {
                "key": {
                  "name": "cvl.type",
                  "type": "spec.cvlast.CVLType$PureCVLType",
                  "erasureStrategy": "CallTrace"
                },
                "value": {
                  "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                  "k": 256
                }
              }
            ]
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "x",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 8
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                "k": 256
              },
              "range": {
                "#class": "utils.Range.Range",
                "specFile": "test.spec",
                "start": {
                  "line": 69,
                  "charByteOffset": 12
                },
                "end": {
                  "line": 69,
                  "charByteOffset": 13
                }
              }
            },
            "twoStateIndex": "NEITHER"
          }
        },
        "o2": {
          "out": {
            "#class": "vc.data.TACSymbol.Const",
            "value": "3"
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
            "n": "3",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 8
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral",
                "n": "3"
              },
              "range": {
                "#class": "utils.Range.Range",
                "specFile": "test.spec",
                "start": {
                  "line": 69,
                  "charByteOffset": 16
                },
                "end": {
                  "line": 69,
                  "charByteOffset": 17
                }
              }
            }
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "test.spec",
        "start": {
          "line": 69,
          "charByteOffset": 4
        },
        "end": {
          "line": 69,
          "charByteOffset": 18
        }
      }
    }
  ],
  "94": [
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "test.spec",
        "start": {
          "line": 69,
          "charByteOffset": 4
        },
        "end": {
          "line": 69,
          "charByteOffset": 18
        }
      }
    }
  ],
  "95": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 19
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "test.spec",
        "start": {
          "line": 70,
          "charByteOffset": 4
        },
        "end": {
          "line": 70,
          "charByteOffset": 27
        }
      }
    }
  ],
  "96": [
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "test.spec",
        "start": {
          "line": 70,
          "charByteOffset": 4
        },
        "end": {
          "line": 70,
          "charByteOffset": 27
        }
      }
    }
  ],
  "97": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 20
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "test.spec",
        "start": {
          "line": 71,
          "charByteOffset": 4
        },
        "end": {
          "line": 71,
          "charByteOffset": 28
        }
      }
    }
  ],
  "98": [
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "test.spec",
        "start": {
          "line": 71,
          "charByteOffset": 4
        },
        "end": {
          "line": 71,
          "charByteOffset": 28
        }
      }
    }
  ],
  "99": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.NullaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.VariableExp",
          "id": "x",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 8
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                  ],
                  "innerScope": null
                }
              }
            },
            "type": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
              "k": 256
            },
            "range": {
              "#class": "utils.Range.Range",
              "specFile": "test.spec",
              "start": {
                "line": 71,
                "charByteOffset": 22
              },
              "end": {
                "line": 71,
                "charByteOffset": 23
              }
            }
          },
          "twoStateIndex": "NEITHER"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "test.spec",
        "start": {
          "line": 71,
          "charByteOffset": 4
        },
        "end": {
          "line": 71,
          "charByteOffset": 28
        }
      }
    }
  ],
  "100": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 21
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "test.spec",
        "start": {
          "line": 8,
          "charByteOffset": 4
        },
        "end": {
          "line": 8,
          "charByteOffset": 34
        }
      }
    }
  ],
  "101": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.NullaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
          "n": "0",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                  "scopeId": 9
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                  ],
                  "innerScope": null
                }
              }
            },
            "type": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral",
              "n": "0"
            },
            "range": {
              "#class": "utils.Range.Range",
              "specFile": "test.spec",
              "start": {
                "line": 8,
                "charByteOffset": 25
              },
              "end": {
                "line": 8,
                "charByteOffset": 26
              }
            }
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "test.spec",
        "start": {
          "line": 8,
          "charByteOffset": 4
        },
        "end": {
          "line": 8,
          "charByteOffset": 34
        }
      }
    }
  ],
  "102": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Const",
        "value": "0"
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "test.spec",
        "start": {
          "line": 8,
          "charByteOffset": 4
        },
        "end": {
          "line": 8,
          "charByteOffset": 34
        }
      }
    }
  ],
  "103": [
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "test.spec",
        "start": {
          "line": 8,
          "charByteOffset": 4
        },
        "end": {
          "line": 8,
          "charByteOffset": 34
        }
      }
    }
  ],
  "104": [
    {
      "key": {
        "name": "tac.direct.storage.access",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "test.spec",
        "start": {
          "line": 8,
          "charByteOffset": 4
        },
        "end": {
          "line": 8,
          "charByteOffset": 34
        }
      }
    }
  ],
  "105": [
    {
      "key": {
        "name": "tac.is-temp-var",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "tac.storage.access-paths",
        "type": "analysis.storage.StorageAnalysisResult$AccessPaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.StorageAnalysis.AnalysisPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysis.AnalysisPath.MapAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysis.AnalysisPath.Root",
                "slot": "0"
              },
              "key": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "I30",
                "tag": {
                  "#class": "tac.Tag.Int"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "cvl.type",
                      "type": "spec.cvlast.CVLType$PureCVLType",
                      "erasureStrategy": "CallTrace"
                    },
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral",
                      "n": "0"
                    }
                  }
                ]
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Const",
                "value": "0"
              },
              "hashResult": {
                "#class": "vc.data.TACSymbol.Const",
                "value": "0"
              }
            },
            "offset": {
              "#class": "analysis.storage.StorageAnalysis.Offset.Bytes",
              "numBytes": "36"
            }
          }
        ]
      }
    }
  ],
  "106": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.NullaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
          "b": "1",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                  "scopeId": 9
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                  ],
                  "innerScope": null
                }
              }
            },
            "type": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
            },
            "range": {
              "#class": "utils.Range.Empty",
              "comment": "autogenerated bool expression at test.spec:9:5"
            }
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "test.spec",
        "start": {
          "line": 8,
          "charByteOffset": 4
        },
        "end": {
          "line": 8,
          "charByteOffset": 34
        }
      }
    }
  ],
  "107": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 22
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "test.spec",
        "start": {
          "line": 9,
          "charByteOffset": 4
        },
        "end": {
          "line": 9,
          "charByteOffset": 47
        }
      }
    }
  ],
  "108": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.NullaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
          "n": "0",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                  "scopeId": 9
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                  ],
                  "innerScope": null
                }
              }
            },
            "type": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral",
              "n": "0"
            },
            "range": {
              "#class": "utils.Range.Range",
              "specFile": "test.spec",
              "start": {
                "line": 9,
                "charByteOffset": 27
              },
              "end": {
                "line": 9,
                "charByteOffset": 28
              }
            }
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "test.spec",
        "start": {
          "line": 9,
          "charByteOffset": 4
        },
        "end": {
          "line": 9,
          "charByteOffset": 47
        }
      }
    }
  ],
  "109": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Const",
        "value": "0"
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "test.spec",
        "start": {
          "line": 9,
          "charByteOffset": 4
        },
        "end": {
          "line": 9,
          "charByteOffset": 47
        }
      }
    }
  ],
  "110": [
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "test.spec",
        "start": {
          "line": 9,
          "charByteOffset": 4
        },
        "end": {
          "line": 9,
          "charByteOffset": 47
        }
      }
    }
  ],
  "111": [
    {
      "key": {
        "name": "tac.direct.storage.access",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "test.spec",
        "start": {
          "line": 9,
          "charByteOffset": 4
        },
        "end": {
          "line": 9,
          "charByteOffset": 47
        }
      }
    }
  ],
  "112": [
    {
      "key": {
        "name": "tac.storage.non-indexed-path.family",
        "type": "analysis.storage.StorageAnalysisResult$StoragePaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "storagePaths": [
          {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.MapAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
                "slot": "0"
              }
            },
            "offset": "1"
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Packed",
        "packedStart": {
          "#class": "vc.data.ScalarizationSort.UnscalarizedBuffer"
        },
        "start": 176
      }
    },
    {
      "key": {
        "name": "tac.direct.storage.access.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 8
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
      }
    },
    {
      "key": {
        "name": "tac.storage.non-indexed-path",
        "type": "analysis.storage.StorageAnalysisResult$NonIndexedPath",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
        "base": {
          "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.MapAccess",
          "base": {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
            "slot": "0"
          }
        },
        "offset": "1"
      }
    },
    {
      "key": {
        "name": "tac.storage",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a0000000000000000000000001"
    }
  ],
  "113": [
    {
      "key": {
        "name": "tac.is-temp-var",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "tac.storage.access-paths",
        "type": "analysis.storage.StorageAnalysisResult$AccessPaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.StorageAnalysis.AnalysisPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysis.AnalysisPath.MapAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysis.AnalysisPath.Root",
                "slot": "0"
              },
              "key": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "I37",
                "tag": {
                  "#class": "tac.Tag.Int"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "cvl.type",
                      "type": "spec.cvlast.CVLType$PureCVLType",
                      "erasureStrategy": "CallTrace"
                    },
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral",
                      "n": "0"
                    }
                  }
                ]
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Const",
                "value": "0"
              },
              "hashResult": {
                "#class": "vc.data.TACSymbol.Const",
                "value": "0"
              }
            },
            "offset": {
              "#class": "analysis.storage.StorageAnalysis.Offset.Bytes",
              "numBytes": "36"
            }
          }
        ]
      }
    }
  ],
  "114": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.NullaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.VariableExp",
          "id": "x",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                  "scopeId": 9
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                  ],
                  "innerScope": null
                }
              }
            },
            "type": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
              "k": 256
            },
            "range": {
              "#class": "utils.Range.Range",
              "specFile": "test.spec",
              "start": {
                "line": 9,
                "charByteOffset": 40
              },
              "end": {
                "line": 9,
                "charByteOffset": 41
              }
            }
          },
          "twoStateIndex": "NEITHER"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "test.spec",
        "start": {
          "line": 9,
          "charByteOffset": 4
        },
        "end": {
          "line": 9,
          "charByteOffset": 47
        }
      }
    }
  ],
  "115": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.NullaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
          "n": "3",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                  "scopeId": 9
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                  ],
                  "innerScope": null
                }
              }
            },
            "type": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral",
              "n": "3"
            },
            "range": {
              "#class": "utils.Range.Range",
              "specFile": "test.spec",
              "start": {
                "line": 9,
                "charByteOffset": 44
              },
              "end": {
                "line": 9,
                "charByteOffset": 45
              }
            }
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "test.spec",
        "start": {
          "line": 9,
          "charByteOffset": 4
        },
        "end": {
          "line": 9,
          "charByteOffset": 47
        }
      }
    }
  ],
  "116": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.BinaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.RelopExp.ArithRelopExp.GtExp",
          "l": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "x",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                    "scopeId": 9
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                "k": 256
              },
              "range": {
                "#class": "utils.Range.Range",
                "specFile": "test.spec",
                "start": {
                  "line": 9,
                  "charByteOffset": 40
                },
                "end": {
                  "line": 9,
                  "charByteOffset": 41
                }
              }
            },
            "twoStateIndex": "NEITHER"
          },
          "r": {
            "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
            "n": "3",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                    "scopeId": 9
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral",
                "n": "3"
              },
              "range": {
                "#class": "utils.Range.Range",
                "specFile": "test.spec",
                "start": {
                  "line": 9,
                  "charByteOffset": 44
                },
                "end": {
                  "line": 9,
                  "charByteOffset": 45
                }
              }
            }
          },
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                  "scopeId": 9
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                  ],
                  "innerScope": null
                }
              }
            },
            "type": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
            },
            "range": {
              "#class": "utils.Range.Range",
              "specFile": "test.spec",
              "start": {
                "line": 9,
                "charByteOffset": 40
              },
              "end": {
                "line": 9,
                "charByteOffset": 45
              }
            },
            "hasParens": true
          }
        },
        "o1": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "I42",
            "tag": {
              "#class": "tac.Tag.Int"
            },
            "callIndex": 0,
            "meta": [
              {
                "key": {
                  "name": "cvl.type",
                  "type": "spec.cvlast.CVLType$PureCVLType",
                  "erasureStrategy": "CallTrace"
                },
                "value": {
                  "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                  "k": 256
                }
              }
            ]
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "x",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                    "scopeId": 9
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                "k": 256
              },
              "range": {
                "#class": "utils.Range.Range",
                "specFile": "test.spec",
                "start": {
                  "line": 9,
                  "charByteOffset": 40
                },
                "end": {
                  "line": 9,
                  "charByteOffset": 41
                }
              }
            },
            "twoStateIndex": "NEITHER"
          }
        },
        "o2": {
          "out": {
            "#class": "vc.data.TACSymbol.Const",
            "value": "3"
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
            "n": "3",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                    "scopeId": 9
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral",
                "n": "3"
              },
              "range": {
                "#class": "utils.Range.Range",
                "specFile": "test.spec",
                "start": {
                  "line": 9,
                  "charByteOffset": 44
                },
                "end": {
                  "line": 9,
                  "charByteOffset": 45
                }
              }
            }
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "test.spec",
        "start": {
          "line": 9,
          "charByteOffset": 4
        },
        "end": {
          "line": 9,
          "charByteOffset": 47
        }
      }
    }
  ],
  "117": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.BinaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.RelopExp.EqExp",
          "l": {
            "#class": "spec.cvlast.CVLExp.FieldSelectExp",
            "structExp": {
              "#class": "spec.cvlast.CVLExp.FieldSelectExp",
              "structExp": {
                "#class": "spec.cvlast.CVLExp.ArrayDerefExp",
                "array": {
                  "#class": "spec.cvlast.CVLExp.FieldSelectExp",
                  "structExp": {
                    "#class": "spec.cvlast.CVLExp.VariableExp",
                    "id": "testContract",
                    "tag": {
                      "scope": {
                        "scopeStack": [
                          {
                            "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                          },
                          {
                            "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                            "scopeId": 9
                          }
                        ],
                        "innerScope": {
                          "scopeStack": [
                            {
                              "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                            }
                          ],
                          "innerScope": {
                            "scopeStack": [
                            ],
                            "innerScope": null
                          }
                        }
                      },
                      "type": {
                        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.CodeContract",
                        "name": {
                          "name": "TestContract"
                        }
                      },
                      "range": {
                        "#class": "utils.Range.Range",
                        "specFile": "test.spec",
                        "start": {
                          "line": 9,
                          "charByteOffset": 12
                        },
                        "end": {
                          "line": 9,
                          "charByteOffset": 24
                        }
                      },
                      "annotation": {
                        "#class": "ReflectivePolymorphicSerializer::spec.cvlast.CVLExp$VariableExp$ContractInstanceId",
                        "instanceId": "ce4604a0000000000000000000000001"
                      }
                    },
                    "twoStateIndex": "NEITHER"
                  },
                  "fieldName": "m",
                  "tag": {
                    "scope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        },
                        {
                          "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                          "scopeId": 9
                        }
                      ],
                      "innerScope": {
                        "scopeStack": [
                          {
                            "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                          }
                        ],
                        "innerScope": {
                          "scopeStack": [
                          ],
                          "innerScope": null
                        }
                      }
                    },
                    "type": {
                      "#class": "spec.cvlast.CVLType.VM",
                      "descriptor": {
                        "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMMappingDescriptor",
                        "keyType": {
                          "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                          "bitwidth": 256
                        },
                        "valueType": {
                          "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.EVMStructDescriptor",
                          "canonicalId": "TestContract.sol|TestContract.Complex",
                          "location": null,
                          "fields": [
                            {
                              "fieldName": "s1",
                              "fieldType": {
                                "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.EVMStructDescriptor",
                                "canonicalId": "TestContract.sol|TestContract.Simple",
                                "location": null,
                                "fields": [
                                  {
                                    "fieldName": "x",
                                    "fieldType": {
                                      "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                      "bitwidth": 256
                                    }
                                  },
                                  {
                                    "fieldName": "y",
                                    "fieldType": {
                                      "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.address"
                                    }
                                  },
                                  {
                                    "fieldName": "z1",
                                    "fieldType": {
                                      "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                      "bitwidth": 8
                                    }
                                  },
                                  {
                                    "fieldName": "z2",
                                    "fieldType": {
                                      "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                      "bitwidth": 8
                                    }
                                  },
                                  {
                                    "fieldName": "b1",
                                    "fieldType": {
                                      "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
                                    }
                                  },
                                  {
                                    "fieldName": "x2",
                                    "fieldType": {
                                      "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                      "bitwidth": 256
                                    }
                                  },
                                  {
                                    "fieldName": "b2",
                                    "fieldType": {
                                      "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
                                    }
                                  }
                                ],
                                "name": "TestContract.Simple"
                              }
                            },
                            {
                              "fieldName": "s2",
                              "fieldType": {
                                "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.EVMStructDescriptor",
                                "canonicalId": "TestContract.sol|TestContract.Simple",
                                "location": null,
                                "fields": [
                                  {
                                    "fieldName": "x",
                                    "fieldType": {
                                      "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                      "bitwidth": 256
                                    }
                                  },
                                  {
                                    "fieldName": "y",
                                    "fieldType": {
                                      "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.address"
                                    }
                                  },
                                  {
                                    "fieldName": "z1",
                                    "fieldType": {
                                      "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                      "bitwidth": 8
                                    }
                                  },
                                  {
                                    "fieldName": "z2",
                                    "fieldType": {
                                      "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                      "bitwidth": 8
                                    }
                                  },
                                  {
                                    "fieldName": "b1",
                                    "fieldType": {
                                      "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
                                    }
                                  },
                                  {
                                    "fieldName": "x2",
                                    "fieldType": {
                                      "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                      "bitwidth": 256
                                    }
                                  },
                                  {
                                    "fieldName": "b2",
                                    "fieldType": {
                                      "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
                                    }
                                  }
                                ],
                                "name": "TestContract.Simple"
                              }
                            },
                            {
                              "fieldName": "b3",
                              "fieldType": {
                                "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
                              }
                            }
                          ],
                          "name": "TestContract.Complex"
                        },
                        "location": null
                      },
                      "context": {
                        "#class": "spec.cvlast.typedescriptors.FromVMContext.StateValue"
                      }
                    },
                    "range": {
                      "#class": "utils.Range.Range",
                      "specFile": "test.spec",
                      "start": {
                        "line": 9,
                        "charByteOffset": 12
                      },
                      "end": {
                        "line": 9,
                        "charByteOffset": 26
                      }
                    },
                    "annotation": {
                      "#class": "ReflectivePolymorphicSerializer::spec.cvlast.StorageAccessMarker"
                    }
                  }
                },
                "index": {
                  "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
                  "n": "0",
                  "tag": {
                    "scope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        },
                        {
                          "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                          "scopeId": 9
                        }
                      ],
                      "innerScope": {
                        "scopeStack": [
                          {
                            "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                          }
                        ],
                        "innerScope": {
                          "scopeStack": [
                          ],
                          "innerScope": null
                        }
                      }
                    },
                    "type": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral",
                      "n": "0"
                    },
                    "range": {
                      "#class": "utils.Range.Range",
                      "specFile": "test.spec",
                      "start": {
                        "line": 9,
                        "charByteOffset": 27
                      },
                      "end": {
                        "line": 9,
                        "charByteOffset": 28
                      }
                    }
                  }
                },
                "tag": {
                  "scope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      },
                      {
                        "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                        "scopeId": 9
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        }
                      ],
                      "innerScope": {
                        "scopeStack": [
                        ],
                        "innerScope": null
                      }
                    }
                  },
                  "type": {
                    "#class": "spec.cvlast.CVLType.VM",
                    "descriptor": {
                      "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMStructDescriptor",
                      "canonicalId": "TestContract.sol|TestContract.Complex",
                      "location": null,
                      "fields": [
                        {
                          "fieldName": "s1",
                          "fieldType": {
                            "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.EVMStructDescriptor",
                            "canonicalId": "TestContract.sol|TestContract.Simple",
                            "location": null,
                            "fields": [
                              {
                                "fieldName": "x",
                                "fieldType": {
                                  "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                  "bitwidth": 256
                                }
                              },
                              {
                                "fieldName": "y",
                                "fieldType": {
                                  "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.address"
                                }
                              },
                              {
                                "fieldName": "z1",
                                "fieldType": {
                                  "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                  "bitwidth": 8
                                }
                              },
                              {
                                "fieldName": "z2",
                                "fieldType": {
                                  "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                  "bitwidth": 8
                                }
                              },
                              {
                                "fieldName": "b1",
                                "fieldType": {
                                  "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
                                }
                              },
                              {
                                "fieldName": "x2",
                                "fieldType": {
                                  "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                  "bitwidth": 256
                                }
                              },
                              {
                                "fieldName": "b2",
                                "fieldType": {
                                  "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
                                }
                              }
                            ],
                            "name": "TestContract.Simple"
                          }
                        },
                        {
                          "fieldName": "s2",
                          "fieldType": {
                            "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.EVMStructDescriptor",
                            "canonicalId": "TestContract.sol|TestContract.Simple",
                            "location": null,
                            "fields": [
                              {
                                "fieldName": "x",
                                "fieldType": {
                                  "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                  "bitwidth": 256
                                }
                              },
                              {
                                "fieldName": "y",
                                "fieldType": {
                                  "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.address"
                                }
                              },
                              {
                                "fieldName": "z1",
                                "fieldType": {
                                  "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                  "bitwidth": 8
                                }
                              },
                              {
                                "fieldName": "z2",
                                "fieldType": {
                                  "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                  "bitwidth": 8
                                }
                              },
                              {
                                "fieldName": "b1",
                                "fieldType": {
                                  "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
                                }
                              },
                              {
                                "fieldName": "x2",
                                "fieldType": {
                                  "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                  "bitwidth": 256
                                }
                              },
                              {
                                "fieldName": "b2",
                                "fieldType": {
                                  "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
                                }
                              }
                            ],
                            "name": "TestContract.Simple"
                          }
                        },
                        {
                          "fieldName": "b3",
                          "fieldType": {
                            "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
                          }
                        }
                      ],
                      "name": "TestContract.Complex"
                    },
                    "context": {
                      "#class": "spec.cvlast.typedescriptors.FromVMContext.StateValue"
                    }
                  },
                  "range": {
                    "#class": "utils.Range.Range",
                    "specFile": "test.spec",
                    "start": {
                      "line": 9,
                      "charByteOffset": 12
                    },
                    "end": {
                      "line": 9,
                      "charByteOffset": 29
                    }
                  },
                  "annotation": {
                    "#class": "ReflectivePolymorphicSerializer::spec.cvlast.StorageAccessMarker"
                  }
                }
              },
              "fieldName": "s1",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                      "scopeId": 9
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                      ],
                      "innerScope": null
                    }
                  }
                },
                "type": {
                  "#class": "spec.cvlast.CVLType.VM",
                  "descriptor": {
                    "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMStructDescriptor",
                    "canonicalId": "TestContract.sol|TestContract.Simple",
                    "location": null,
                    "fields": [
                      {
                        "fieldName": "x",
                        "fieldType": {
                          "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                          "bitwidth": 256
                        }
                      },
                      {
                        "fieldName": "y",
                        "fieldType": {
                          "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.address"
                        }
                      },
                      {
                        "fieldName": "z1",
                        "fieldType": {
                          "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                          "bitwidth": 8
                        }
                      },
                      {
                        "fieldName": "z2",
                        "fieldType": {
                          "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                          "bitwidth": 8
                        }
                      },
                      {
                        "fieldName": "b1",
                        "fieldType": {
                          "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
                        }
                      },
                      {
                        "fieldName": "x2",
                        "fieldType": {
                          "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                          "bitwidth": 256
                        }
                      },
                      {
                        "fieldName": "b2",
                        "fieldType": {
                          "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
                        }
                      }
                    ],
                    "name": "TestContract.Simple"
                  },
                  "context": {
                    "#class": "spec.cvlast.typedescriptors.FromVMContext.StateValue"
                  }
                },
                "range": {
                  "#class": "utils.Range.Range",
                  "specFile": "test.spec",
                  "start": {
                    "line": 9,
                    "charByteOffset": 12
                  },
                  "end": {
                    "line": 9,
                    "charByteOffset": 32
                  }
                },
                "annotation": {
                  "#class": "ReflectivePolymorphicSerializer::spec.cvlast.StorageAccessMarker"
                }
              }
            },
            "fieldName": "b1",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                    "scopeId": 9
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.VM",
                "descriptor": {
                  "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$bool"
                },
                "context": {
                  "#class": "spec.cvlast.typedescriptors.FromVMContext.StateValue"
                }
              },
              "range": {
                "#class": "utils.Range.Range",
                "specFile": "test.spec",
                "start": {
                  "line": 9,
                  "charByteOffset": 12
                },
                "end": {
                  "line": 9,
                  "charByteOffset": 35
                }
              },
              "annotation": {
                "#class": "ReflectivePolymorphicSerializer::spec.cvlast.StorageAccessMarker"
              }
            }
          },
          "r": {
            "#class": "spec.cvlast.CVLExp.RelopExp.ArithRelopExp.GtExp",
            "l": {
              "#class": "spec.cvlast.CVLExp.VariableExp",
              "id": "x",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                      "scopeId": 9
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                      ],
                      "innerScope": null
                    }
                  }
                },
                "type": {
                  "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                  "k": 256
                },
                "range": {
                  "#class": "utils.Range.Range",
                  "specFile": "test.spec",
                  "start": {
                    "line": 9,
                    "charByteOffset": 40
                  },
                  "end": {
                    "line": 9,
                    "charByteOffset": 41
                  }
                }
              },
              "twoStateIndex": "NEITHER"
            },
            "r": {
              "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
              "n": "3",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                      "scopeId": 9
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                      ],
                      "innerScope": null
                    }
                  }
                },
                "type": {
                  "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral",
                  "n": "3"
                },
                "range": {
                  "#class": "utils.Range.Range",
                  "specFile": "test.spec",
                  "start": {
                    "line": 9,
                    "charByteOffset": 44
                  },
                  "end": {
                    "line": 9,
                    "charByteOffset": 45
                  }
                }
              }
            },
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                    "scopeId": 9
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              },
              "range": {
                "#class": "utils.Range.Range",
                "specFile": "test.spec",
                "start": {
                  "line": 9,
                  "charByteOffset": 40
                },
                "end": {
                  "line": 9,
                  "charByteOffset": 45
                }
              },
              "hasParens": true
            }
          },
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                  "scopeId": 9
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                  ],
                  "innerScope": null
                }
              }
            },
            "type": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
            },
            "range": {
              "#class": "utils.Range.Range",
              "specFile": "test.spec",
              "start": {
                "line": 9,
                "charByteOffset": 12
              },
              "end": {
                "line": 9,
                "charByteOffset": 46
              }
            }
          }
        },
        "o1": {
          "out": {
            "#class": "vc.data.TACSymbol.Const",
            "value": "0",
            "tag": {
              "#class": "tac.Tag.Bool"
            }
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.FieldSelectExp",
            "structExp": {
              "#class": "spec.cvlast.CVLExp.FieldSelectExp",
              "structExp": {
                "#class": "spec.cvlast.CVLExp.ArrayDerefExp",
                "array": {
                  "#class": "spec.cvlast.CVLExp.FieldSelectExp",
                  "structExp": {
                    "#class": "spec.cvlast.CVLExp.VariableExp",
                    "id": "testContract",
                    "tag": {
                      "scope": {
                        "scopeStack": [
                          {
                            "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                          },
                          {
                            "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                            "scopeId": 9
                          }
                        ],
                        "innerScope": {
                          "scopeStack": [
                            {
                              "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                            }
                          ],
                          "innerScope": {
                            "scopeStack": [
                            ],
                            "innerScope": null
                          }
                        }
                      },
                      "type": {
                        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.CodeContract",
                        "name": {
                          "name": "TestContract"
                        }
                      },
                      "range": {
                        "#class": "utils.Range.Range",
                        "specFile": "test.spec",
                        "start": {
                          "line": 9,
                          "charByteOffset": 12
                        },
                        "end": {
                          "line": 9,
                          "charByteOffset": 24
                        }
                      },
                      "annotation": {
                        "#class": "ReflectivePolymorphicSerializer::spec.cvlast.CVLExp$VariableExp$ContractInstanceId",
                        "instanceId": "ce4604a0000000000000000000000001"
                      }
                    },
                    "twoStateIndex": "NEITHER"
                  },
                  "fieldName": "m",
                  "tag": {
                    "scope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        },
                        {
                          "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                          "scopeId": 9
                        }
                      ],
                      "innerScope": {
                        "scopeStack": [
                          {
                            "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                          }
                        ],
                        "innerScope": {
                          "scopeStack": [
                          ],
                          "innerScope": null
                        }
                      }
                    },
                    "type": {
                      "#class": "spec.cvlast.CVLType.VM",
                      "descriptor": {
                        "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMMappingDescriptor",
                        "keyType": {
                          "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                          "bitwidth": 256
                        },
                        "valueType": {
                          "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.EVMStructDescriptor",
                          "canonicalId": "TestContract.sol|TestContract.Complex",
                          "location": null,
                          "fields": [
                            {
                              "fieldName": "s1",
                              "fieldType": {
                                "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.EVMStructDescriptor",
                                "canonicalId": "TestContract.sol|TestContract.Simple",
                                "location": null,
                                "fields": [
                                  {
                                    "fieldName": "x",
                                    "fieldType": {
                                      "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                      "bitwidth": 256
                                    }
                                  },
                                  {
                                    "fieldName": "y",
                                    "fieldType": {
                                      "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.address"
                                    }
                                  },
                                  {
                                    "fieldName": "z1",
                                    "fieldType": {
                                      "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                      "bitwidth": 8
                                    }
                                  },
                                  {
                                    "fieldName": "z2",
                                    "fieldType": {
                                      "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                      "bitwidth": 8
                                    }
                                  },
                                  {
                                    "fieldName": "b1",
                                    "fieldType": {
                                      "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
                                    }
                                  },
                                  {
                                    "fieldName": "x2",
                                    "fieldType": {
                                      "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                      "bitwidth": 256
                                    }
                                  },
                                  {
                                    "fieldName": "b2",
                                    "fieldType": {
                                      "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
                                    }
                                  }
                                ],
                                "name": "TestContract.Simple"
                              }
                            },
                            {
                              "fieldName": "s2",
                              "fieldType": {
                                "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.EVMStructDescriptor",
                                "canonicalId": "TestContract.sol|TestContract.Simple",
                                "location": null,
                                "fields": [
                                  {
                                    "fieldName": "x",
                                    "fieldType": {
                                      "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                      "bitwidth": 256
                                    }
                                  },
                                  {
                                    "fieldName": "y",
                                    "fieldType": {
                                      "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.address"
                                    }
                                  },
                                  {
                                    "fieldName": "z1",
                                    "fieldType": {
                                      "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                      "bitwidth": 8
                                    }
                                  },
                                  {
                                    "fieldName": "z2",
                                    "fieldType": {
                                      "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                      "bitwidth": 8
                                    }
                                  },
                                  {
                                    "fieldName": "b1",
                                    "fieldType": {
                                      "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
                                    }
                                  },
                                  {
                                    "fieldName": "x2",
                                    "fieldType": {
                                      "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                      "bitwidth": 256
                                    }
                                  },
                                  {
                                    "fieldName": "b2",
                                    "fieldType": {
                                      "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
                                    }
                                  }
                                ],
                                "name": "TestContract.Simple"
                              }
                            },
                            {
                              "fieldName": "b3",
                              "fieldType": {
                                "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
                              }
                            }
                          ],
                          "name": "TestContract.Complex"
                        },
                        "location": null
                      },
                      "context": {
                        "#class": "spec.cvlast.typedescriptors.FromVMContext.StateValue"
                      }
                    },
                    "range": {
                      "#class": "utils.Range.Range",
                      "specFile": "test.spec",
                      "start": {
                        "line": 9,
                        "charByteOffset": 12
                      },
                      "end": {
                        "line": 9,
                        "charByteOffset": 26
                      }
                    },
                    "annotation": {
                      "#class": "ReflectivePolymorphicSerializer::spec.cvlast.StorageAccessMarker"
                    }
                  }
                },
                "index": {
                  "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
                  "n": "0",
                  "tag": {
                    "scope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        },
                        {
                          "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                          "scopeId": 9
                        }
                      ],
                      "innerScope": {
                        "scopeStack": [
                          {
                            "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                          }
                        ],
                        "innerScope": {
                          "scopeStack": [
                          ],
                          "innerScope": null
                        }
                      }
                    },
                    "type": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral",
                      "n": "0"
                    },
                    "range": {
                      "#class": "utils.Range.Range",
                      "specFile": "test.spec",
                      "start": {
                        "line": 9,
                        "charByteOffset": 27
                      },
                      "end": {
                        "line": 9,
                        "charByteOffset": 28
                      }
                    }
                  }
                },
                "tag": {
                  "scope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      },
                      {
                        "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                        "scopeId": 9
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        }
                      ],
                      "innerScope": {
                        "scopeStack": [
                        ],
                        "innerScope": null
                      }
                    }
                  },
                  "type": {
                    "#class": "spec.cvlast.CVLType.VM",
                    "descriptor": {
                      "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMStructDescriptor",
                      "canonicalId": "TestContract.sol|TestContract.Complex",
                      "location": null,
                      "fields": [
                        {
                          "fieldName": "s1",
                          "fieldType": {
                            "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.EVMStructDescriptor",
                            "canonicalId": "TestContract.sol|TestContract.Simple",
                            "location": null,
                            "fields": [
                              {
                                "fieldName": "x",
                                "fieldType": {
                                  "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                  "bitwidth": 256
                                }
                              },
                              {
                                "fieldName": "y",
                                "fieldType": {
                                  "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.address"
                                }
                              },
                              {
                                "fieldName": "z1",
                                "fieldType": {
                                  "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                  "bitwidth": 8
                                }
                              },
                              {
                                "fieldName": "z2",
                                "fieldType": {
                                  "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                  "bitwidth": 8
                                }
                              },
                              {
                                "fieldName": "b1",
                                "fieldType": {
                                  "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
                                }
                              },
                              {
                                "fieldName": "x2",
                                "fieldType": {
                                  "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                  "bitwidth": 256
                                }
                              },
                              {
                                "fieldName": "b2",
                                "fieldType": {
                                  "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
                                }
                              }
                            ],
                            "name": "TestContract.Simple"
                          }
                        },
                        {
                          "fieldName": "s2",
                          "fieldType": {
                            "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.EVMStructDescriptor",
                            "canonicalId": "TestContract.sol|TestContract.Simple",
                            "location": null,
                            "fields": [
                              {
                                "fieldName": "x",
                                "fieldType": {
                                  "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                  "bitwidth": 256
                                }
                              },
                              {
                                "fieldName": "y",
                                "fieldType": {
                                  "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.address"
                                }
                              },
                              {
                                "fieldName": "z1",
                                "fieldType": {
                                  "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                  "bitwidth": 8
                                }
                              },
                              {
                                "fieldName": "z2",
                                "fieldType": {
                                  "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                  "bitwidth": 8
                                }
                              },
                              {
                                "fieldName": "b1",
                                "fieldType": {
                                  "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
                                }
                              },
                              {
                                "fieldName": "x2",
                                "fieldType": {
                                  "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                  "bitwidth": 256
                                }
                              },
                              {
                                "fieldName": "b2",
                                "fieldType": {
                                  "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
                                }
                              }
                            ],
                            "name": "TestContract.Simple"
                          }
                        },
                        {
                          "fieldName": "b3",
                          "fieldType": {
                            "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
                          }
                        }
                      ],
                      "name": "TestContract.Complex"
                    },
                    "context": {
                      "#class": "spec.cvlast.typedescriptors.FromVMContext.StateValue"
                    }
                  },
                  "range": {
                    "#class": "utils.Range.Range",
                    "specFile": "test.spec",
                    "start": {
                      "line": 9,
                      "charByteOffset": 12
                    },
                    "end": {
                      "line": 9,
                      "charByteOffset": 29
                    }
                  },
                  "annotation": {
                    "#class": "ReflectivePolymorphicSerializer::spec.cvlast.StorageAccessMarker"
                  }
                }
              },
              "fieldName": "s1",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                      "scopeId": 9
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                      ],
                      "innerScope": null
                    }
                  }
                },
                "type": {
                  "#class": "spec.cvlast.CVLType.VM",
                  "descriptor": {
                    "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMStructDescriptor",
                    "canonicalId": "TestContract.sol|TestContract.Simple",
                    "location": null,
                    "fields": [
                      {
                        "fieldName": "x",
                        "fieldType": {
                          "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                          "bitwidth": 256
                        }
                      },
                      {
                        "fieldName": "y",
                        "fieldType": {
                          "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.address"
                        }
                      },
                      {
                        "fieldName": "z1",
                        "fieldType": {
                          "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                          "bitwidth": 8
                        }
                      },
                      {
                        "fieldName": "z2",
                        "fieldType": {
                          "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                          "bitwidth": 8
                        }
                      },
                      {
                        "fieldName": "b1",
                        "fieldType": {
                          "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
                        }
                      },
                      {
                        "fieldName": "x2",
                        "fieldType": {
                          "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                          "bitwidth": 256
                        }
                      },
                      {
                        "fieldName": "b2",
                        "fieldType": {
                          "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
                        }
                      }
                    ],
                    "name": "TestContract.Simple"
                  },
                  "context": {
                    "#class": "spec.cvlast.typedescriptors.FromVMContext.StateValue"
                  }
                },
                "range": {
                  "#class": "utils.Range.Range",
                  "specFile": "test.spec",
                  "start": {
                    "line": 9,
                    "charByteOffset": 12
                  },
                  "end": {
                    "line": 9,
                    "charByteOffset": 32
                  }
                },
                "annotation": {
                  "#class": "ReflectivePolymorphicSerializer::spec.cvlast.StorageAccessMarker"
                }
              }
            },
            "fieldName": "b1",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                    "scopeId": 9
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.VM",
                "descriptor": {
                  "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$bool"
                },
                "context": {
                  "#class": "spec.cvlast.typedescriptors.FromVMContext.StateValue"
                }
              },
              "range": {
                "#class": "utils.Range.Range",
                "specFile": "test.spec",
                "start": {
                  "line": 9,
                  "charByteOffset": 12
                },
                "end": {
                  "line": 9,
                  "charByteOffset": 35
                }
              },
              "annotation": {
                "#class": "ReflectivePolymorphicSerializer::spec.cvlast.StorageAccessMarker"
              }
            }
          }
        },
        "o2": {
          "out": {
            "#class": "vc.data.TACSymbol.Const",
            "value": "0",
            "tag": {
              "#class": "tac.Tag.Bool"
            }
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.RelopExp.ArithRelopExp.GtExp",
            "l": {
              "#class": "spec.cvlast.CVLExp.VariableExp",
              "id": "x",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                      "scopeId": 9
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                      ],
                      "innerScope": null
                    }
                  }
                },
                "type": {
                  "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                  "k": 256
                },
                "range": {
                  "#class": "utils.Range.Range",
                  "specFile": "test.spec",
                  "start": {
                    "line": 9,
                    "charByteOffset": 40
                  },
                  "end": {
                    "line": 9,
                    "charByteOffset": 41
                  }
                }
              },
              "twoStateIndex": "NEITHER"
            },
            "r": {
              "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
              "n": "3",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                      "scopeId": 9
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                      ],
                      "innerScope": null
                    }
                  }
                },
                "type": {
                  "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral",
                  "n": "3"
                },
                "range": {
                  "#class": "utils.Range.Range",
                  "specFile": "test.spec",
                  "start": {
                    "line": 9,
                    "charByteOffset": 44
                  },
                  "end": {
                    "line": 9,
                    "charByteOffset": 45
                  }
                }
              }
            },
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                    "scopeId": 9
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              },
              "range": {
                "#class": "utils.Range.Range",
                "specFile": "test.spec",
                "start": {
                  "line": 9,
                  "charByteOffset": 40
                },
                "end": {
                  "line": 9,
                  "charByteOffset": 45
                }
              },
              "hasParens": true
            }
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "test.spec",
        "start": {
          "line": 9,
          "charByteOffset": 4
        },
        "end": {
          "line": 9,
          "charByteOffset": 47
        }
      }
    }
  ],
  "118": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 23
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "test.spec",
        "start": {
          "line": 10,
          "charByteOffset": 4
        },
        "end": {
          "line": 10,
          "charByteOffset": 31
        }
      }
    }
  ],
  "119": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.NullaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
          "n": "0",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                  "scopeId": 9
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                  ],
                  "innerScope": null
                }
              }
            },
            "type": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral",
              "n": "0"
            },
            "range": {
              "#class": "utils.Range.Range",
              "specFile": "test.spec",
              "start": {
                "line": 10,
                "charByteOffset": 25
              },
              "end": {
                "line": 10,
                "charByteOffset": 26
              }
            }
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "test.spec",
        "start": {
          "line": 10,
          "charByteOffset": 4
        },
        "end": {
          "line": 10,
          "charByteOffset": 31
        }
      }
    }
  ],
  "120": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Const",
        "value": "0"
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "test.spec",
        "start": {
          "line": 10,
          "charByteOffset": 4
        },
        "end": {
          "line": 10,
          "charByteOffset": 31
        }
      }
    }
  ],
  "121": [
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "test.spec",
        "start": {
          "line": 10,
          "charByteOffset": 4
        },
        "end": {
          "line": 10,
          "charByteOffset": 31
        }
      }
    }
  ],
  "122": [
    {
      "key": {
        "name": "tac.direct.storage.access",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "test.spec",
        "start": {
          "line": 10,
          "charByteOffset": 4
        },
        "end": {
          "line": 10,
          "charByteOffset": 31
        }
      }
    }
  ],
  "123": [
    {
      "key": {
        "name": "tac.is-temp-var",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "tac.storage.access-paths",
        "type": "analysis.storage.StorageAnalysisResult$AccessPaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.StorageAnalysis.AnalysisPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysis.AnalysisPath.MapAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysis.AnalysisPath.Root",
                "slot": "0"
              },
              "key": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "I45",
                "tag": {
                  "#class": "tac.Tag.Int"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "cvl.type",
                      "type": "spec.cvlast.CVLType$PureCVLType",
                      "erasureStrategy": "CallTrace"
                    },
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral",
                      "n": "0"
                    }
                  }
                ]
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Const",
                "value": "0"
              },
              "hashResult": {
                "#class": "vc.data.TACSymbol.Const",
                "value": "0"
              }
            },
            "offset": {
              "#class": "analysis.storage.StorageAnalysis.Offset.Bytes",
              "numBytes": "100"
            }
          }
        ]
      }
    }
  ],
  "124": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.NullaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.Constant.BoolLit",
          "b": "1",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                  "scopeId": 9
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                  ],
                  "innerScope": null
                }
              }
            },
            "type": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
            },
            "range": {
              "#class": "utils.Range.Empty",
              "comment": "autogenerated bool expression at test.spec:11:5"
            }
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "test.spec",
        "start": {
          "line": 10,
          "charByteOffset": 4
        },
        "end": {
          "line": 10,
          "charByteOffset": 31
        }
      }
    }
  ],
  "125": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 24
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "test.spec",
        "start": {
          "line": 11,
          "charByteOffset": 4
        },
        "end": {
          "line": 11,
          "charByteOffset": 44
        }
      }
    }
  ],
  "126": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.NullaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
          "n": "0",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                  "scopeId": 9
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                  ],
                  "innerScope": null
                }
              }
            },
            "type": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral",
              "n": "0"
            },
            "range": {
              "#class": "utils.Range.Range",
              "specFile": "test.spec",
              "start": {
                "line": 11,
                "charByteOffset": 27
              },
              "end": {
                "line": 11,
                "charByteOffset": 28
              }
            }
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "test.spec",
        "start": {
          "line": 11,
          "charByteOffset": 4
        },
        "end": {
          "line": 11,
          "charByteOffset": 44
        }
      }
    }
  ],
  "127": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Const",
        "value": "0"
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "test.spec",
        "start": {
          "line": 11,
          "charByteOffset": 4
        },
        "end": {
          "line": 11,
          "charByteOffset": 44
        }
      }
    }
  ],
  "128": [
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "test.spec",
        "start": {
          "line": 11,
          "charByteOffset": 4
        },
        "end": {
          "line": 11,
          "charByteOffset": 44
        }
      }
    }
  ],
  "129": [
    {
      "key": {
        "name": "tac.direct.storage.access",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "test.spec",
        "start": {
          "line": 11,
          "charByteOffset": 4
        },
        "end": {
          "line": 11,
          "charByteOffset": 44
        }
      }
    }
  ],
  "130": [
    {
      "key": {
        "name": "tac.storage.non-indexed-path.family",
        "type": "analysis.storage.StorageAnalysisResult$StoragePaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "storagePaths": [
          {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.MapAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
                "slot": "0"
              }
            },
            "offset": "8"
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Packed",
        "packedStart": {
          "#class": "vc.data.ScalarizationSort.UnscalarizedBuffer"
        },
        "start": 0
      }
    },
    {
      "key": {
        "name": "tac.direct.storage.access.type",
        "type": "spec.cvlast.CVLType$PureCVLType",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 8
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
      }
    },
    {
      "key": {
        "name": "tac.storage.non-indexed-path",
        "type": "analysis.storage.StorageAnalysisResult$NonIndexedPath",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.StructAccess",
        "base": {
          "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.MapAccess",
          "base": {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
            "slot": "0"
          }
        },
        "offset": "8"
      }
    },
    {
      "key": {
        "name": "tac.storage",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "ce4604a0000000000000000000000001"
    }
  ],
  "131": [
    {
      "key": {
        "name": "tac.is-temp-var",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "tac.storage.access-paths",
        "type": "analysis.storage.StorageAnalysisResult$AccessPaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.StorageAnalysis.AnalysisPath.StructAccess",
            "base": {
              "#class": "analysis.storage.StorageAnalysis.AnalysisPath.MapAccess",
              "base": {
                "#class": "analysis.storage.StorageAnalysis.AnalysisPath.Root",
                "slot": "0"
              },
              "key": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "I52",
                "tag": {
                  "#class": "tac.Tag.Int"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "cvl.type",
                      "type": "spec.cvlast.CVLType$PureCVLType",
                      "erasureStrategy": "CallTrace"
                    },
                    "value": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral",
                      "n": "0"
                    }
                  }
                ]
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Const",
                "value": "0"
              },
              "hashResult": {
                "#class": "vc.data.TACSymbol.Const",
                "value": "0"
              }
            },
            "offset": {
              "#class": "analysis.storage.StorageAnalysis.Offset.Bytes",
              "numBytes": "100"
            }
          }
        ]
      }
    }
  ],
  "132": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.NullaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.VariableExp",
          "id": "x",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                  "scopeId": 9
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                  ],
                  "innerScope": null
                }
              }
            },
            "type": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
              "k": 256
            },
            "range": {
              "#class": "utils.Range.Range",
              "specFile": "test.spec",
              "start": {
                "line": 11,
                "charByteOffset": 37
              },
              "end": {
                "line": 11,
                "charByteOffset": 38
              }
            }
          },
          "twoStateIndex": "NEITHER"
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "test.spec",
        "start": {
          "line": 11,
          "charByteOffset": 4
        },
        "end": {
          "line": 11,
          "charByteOffset": 44
        }
      }
    }
  ],
  "133": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.NullaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
          "n": "5",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                  "scopeId": 9
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                  ],
                  "innerScope": null
                }
              }
            },
            "type": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral",
              "n": "5"
            },
            "range": {
              "#class": "utils.Range.Range",
              "specFile": "test.spec",
              "start": {
                "line": 11,
                "charByteOffset": 41
              },
              "end": {
                "line": 11,
                "charByteOffset": 42
              }
            }
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "test.spec",
        "start": {
          "line": 11,
          "charByteOffset": 4
        },
        "end": {
          "line": 11,
          "charByteOffset": 44
        }
      }
    }
  ],
  "134": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.BinaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.RelopExp.ArithRelopExp.GtExp",
          "l": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "x",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                    "scopeId": 9
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                "k": 256
              },
              "range": {
                "#class": "utils.Range.Range",
                "specFile": "test.spec",
                "start": {
                  "line": 11,
                  "charByteOffset": 37
                },
                "end": {
                  "line": 11,
                  "charByteOffset": 38
                }
              }
            },
            "twoStateIndex": "NEITHER"
          },
          "r": {
            "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
            "n": "5",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                    "scopeId": 9
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral",
                "n": "5"
              },
              "range": {
                "#class": "utils.Range.Range",
                "specFile": "test.spec",
                "start": {
                  "line": 11,
                  "charByteOffset": 41
                },
                "end": {
                  "line": 11,
                  "charByteOffset": 42
                }
              }
            }
          },
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                  "scopeId": 9
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                  ],
                  "innerScope": null
                }
              }
            },
            "type": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
            },
            "range": {
              "#class": "utils.Range.Range",
              "specFile": "test.spec",
              "start": {
                "line": 11,
                "charByteOffset": 37
              },
              "end": {
                "line": 11,
                "charByteOffset": 42
              }
            },
            "hasParens": true
          }
        },
        "o1": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "I57",
            "tag": {
              "#class": "tac.Tag.Int"
            },
            "callIndex": 0,
            "meta": [
              {
                "key": {
                  "name": "cvl.type",
                  "type": "spec.cvlast.CVLType$PureCVLType",
                  "erasureStrategy": "CallTrace"
                },
                "value": {
                  "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                  "k": 256
                }
              }
            ]
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "x",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                    "scopeId": 9
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                "k": 256
              },
              "range": {
                "#class": "utils.Range.Range",
                "specFile": "test.spec",
                "start": {
                  "line": 11,
                  "charByteOffset": 37
                },
                "end": {
                  "line": 11,
                  "charByteOffset": 38
                }
              }
            },
            "twoStateIndex": "NEITHER"
          }
        },
        "o2": {
          "out": {
            "#class": "vc.data.TACSymbol.Const",
            "value": "5"
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
            "n": "5",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                    "scopeId": 9
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral",
                "n": "5"
              },
              "range": {
                "#class": "utils.Range.Range",
                "specFile": "test.spec",
                "start": {
                  "line": 11,
                  "charByteOffset": 41
                },
                "end": {
                  "line": 11,
                  "charByteOffset": 42
                }
              }
            }
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "test.spec",
        "start": {
          "line": 11,
          "charByteOffset": 4
        },
        "end": {
          "line": 11,
          "charByteOffset": 44
        }
      }
    }
  ],
  "135": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.BinaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.RelopExp.EqExp",
          "l": {
            "#class": "spec.cvlast.CVLExp.FieldSelectExp",
            "structExp": {
              "#class": "spec.cvlast.CVLExp.ArrayDerefExp",
              "array": {
                "#class": "spec.cvlast.CVLExp.FieldSelectExp",
                "structExp": {
                  "#class": "spec.cvlast.CVLExp.VariableExp",
                  "id": "testContract",
                  "tag": {
                    "scope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        },
                        {
                          "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                          "scopeId": 9
                        }
                      ],
                      "innerScope": {
                        "scopeStack": [
                          {
                            "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                          }
                        ],
                        "innerScope": {
                          "scopeStack": [
                          ],
                          "innerScope": null
                        }
                      }
                    },
                    "type": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.CodeContract",
                      "name": {
                        "name": "TestContract"
                      }
                    },
                    "range": {
                      "#class": "utils.Range.Range",
                      "specFile": "test.spec",
                      "start": {
                        "line": 11,
                        "charByteOffset": 12
                      },
                      "end": {
                        "line": 11,
                        "charByteOffset": 24
                      }
                    },
                    "annotation": {
                      "#class": "ReflectivePolymorphicSerializer::spec.cvlast.CVLExp$VariableExp$ContractInstanceId",
                      "instanceId": "ce4604a0000000000000000000000001"
                    }
                  },
                  "twoStateIndex": "NEITHER"
                },
                "fieldName": "m",
                "tag": {
                  "scope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      },
                      {
                        "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                        "scopeId": 9
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        }
                      ],
                      "innerScope": {
                        "scopeStack": [
                        ],
                        "innerScope": null
                      }
                    }
                  },
                  "type": {
                    "#class": "spec.cvlast.CVLType.VM",
                    "descriptor": {
                      "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMMappingDescriptor",
                      "keyType": {
                        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                        "bitwidth": 256
                      },
                      "valueType": {
                        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.EVMStructDescriptor",
                        "canonicalId": "TestContract.sol|TestContract.Complex",
                        "location": null,
                        "fields": [
                          {
                            "fieldName": "s1",
                            "fieldType": {
                              "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.EVMStructDescriptor",
                              "canonicalId": "TestContract.sol|TestContract.Simple",
                              "location": null,
                              "fields": [
                                {
                                  "fieldName": "x",
                                  "fieldType": {
                                    "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                    "bitwidth": 256
                                  }
                                },
                                {
                                  "fieldName": "y",
                                  "fieldType": {
                                    "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.address"
                                  }
                                },
                                {
                                  "fieldName": "z1",
                                  "fieldType": {
                                    "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                    "bitwidth": 8
                                  }
                                },
                                {
                                  "fieldName": "z2",
                                  "fieldType": {
                                    "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                    "bitwidth": 8
                                  }
                                },
                                {
                                  "fieldName": "b1",
                                  "fieldType": {
                                    "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
                                  }
                                },
                                {
                                  "fieldName": "x2",
                                  "fieldType": {
                                    "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                    "bitwidth": 256
                                  }
                                },
                                {
                                  "fieldName": "b2",
                                  "fieldType": {
                                    "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
                                  }
                                }
                              ],
                              "name": "TestContract.Simple"
                            }
                          },
                          {
                            "fieldName": "s2",
                            "fieldType": {
                              "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.EVMStructDescriptor",
                              "canonicalId": "TestContract.sol|TestContract.Simple",
                              "location": null,
                              "fields": [
                                {
                                  "fieldName": "x",
                                  "fieldType": {
                                    "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                    "bitwidth": 256
                                  }
                                },
                                {
                                  "fieldName": "y",
                                  "fieldType": {
                                    "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.address"
                                  }
                                },
                                {
                                  "fieldName": "z1",
                                  "fieldType": {
                                    "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                    "bitwidth": 8
                                  }
                                },
                                {
                                  "fieldName": "z2",
                                  "fieldType": {
                                    "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                    "bitwidth": 8
                                  }
                                },
                                {
                                  "fieldName": "b1",
                                  "fieldType": {
                                    "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
                                  }
                                },
                                {
                                  "fieldName": "x2",
                                  "fieldType": {
                                    "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                    "bitwidth": 256
                                  }
                                },
                                {
                                  "fieldName": "b2",
                                  "fieldType": {
                                    "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
                                  }
                                }
                              ],
                              "name": "TestContract.Simple"
                            }
                          },
                          {
                            "fieldName": "b3",
                            "fieldType": {
                              "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
                            }
                          }
                        ],
                        "name": "TestContract.Complex"
                      },
                      "location": null
                    },
                    "context": {
                      "#class": "spec.cvlast.typedescriptors.FromVMContext.StateValue"
                    }
                  },
                  "range": {
                    "#class": "utils.Range.Range",
                    "specFile": "test.spec",
                    "start": {
                      "line": 11,
                      "charByteOffset": 12
                    },
                    "end": {
                      "line": 11,
                      "charByteOffset": 26
                    }
                  },
                  "annotation": {
                    "#class": "ReflectivePolymorphicSerializer::spec.cvlast.StorageAccessMarker"
                  }
                }
              },
              "index": {
                "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
                "n": "0",
                "tag": {
                  "scope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      },
                      {
                        "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                        "scopeId": 9
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        }
                      ],
                      "innerScope": {
                        "scopeStack": [
                        ],
                        "innerScope": null
                      }
                    }
                  },
                  "type": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral",
                    "n": "0"
                  },
                  "range": {
                    "#class": "utils.Range.Range",
                    "specFile": "test.spec",
                    "start": {
                      "line": 11,
                      "charByteOffset": 27
                    },
                    "end": {
                      "line": 11,
                      "charByteOffset": 28
                    }
                  }
                }
              },
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                      "scopeId": 9
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                      ],
                      "innerScope": null
                    }
                  }
                },
                "type": {
                  "#class": "spec.cvlast.CVLType.VM",
                  "descriptor": {
                    "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMStructDescriptor",
                    "canonicalId": "TestContract.sol|TestContract.Complex",
                    "location": null,
                    "fields": [
                      {
                        "fieldName": "s1",
                        "fieldType": {
                          "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.EVMStructDescriptor",
                          "canonicalId": "TestContract.sol|TestContract.Simple",
                          "location": null,
                          "fields": [
                            {
                              "fieldName": "x",
                              "fieldType": {
                                "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                "bitwidth": 256
                              }
                            },
                            {
                              "fieldName": "y",
                              "fieldType": {
                                "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.address"
                              }
                            },
                            {
                              "fieldName": "z1",
                              "fieldType": {
                                "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                "bitwidth": 8
                              }
                            },
                            {
                              "fieldName": "z2",
                              "fieldType": {
                                "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                "bitwidth": 8
                              }
                            },
                            {
                              "fieldName": "b1",
                              "fieldType": {
                                "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
                              }
                            },
                            {
                              "fieldName": "x2",
                              "fieldType": {
                                "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                "bitwidth": 256
                              }
                            },
                            {
                              "fieldName": "b2",
                              "fieldType": {
                                "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
                              }
                            }
                          ],
                          "name": "TestContract.Simple"
                        }
                      },
                      {
                        "fieldName": "s2",
                        "fieldType": {
                          "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.EVMStructDescriptor",
                          "canonicalId": "TestContract.sol|TestContract.Simple",
                          "location": null,
                          "fields": [
                            {
                              "fieldName": "x",
                              "fieldType": {
                                "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                "bitwidth": 256
                              }
                            },
                            {
                              "fieldName": "y",
                              "fieldType": {
                                "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.address"
                              }
                            },
                            {
                              "fieldName": "z1",
                              "fieldType": {
                                "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                "bitwidth": 8
                              }
                            },
                            {
                              "fieldName": "z2",
                              "fieldType": {
                                "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                "bitwidth": 8
                              }
                            },
                            {
                              "fieldName": "b1",
                              "fieldType": {
                                "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
                              }
                            },
                            {
                              "fieldName": "x2",
                              "fieldType": {
                                "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                "bitwidth": 256
                              }
                            },
                            {
                              "fieldName": "b2",
                              "fieldType": {
                                "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
                              }
                            }
                          ],
                          "name": "TestContract.Simple"
                        }
                      },
                      {
                        "fieldName": "b3",
                        "fieldType": {
                          "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
                        }
                      }
                    ],
                    "name": "TestContract.Complex"
                  },
                  "context": {
                    "#class": "spec.cvlast.typedescriptors.FromVMContext.StateValue"
                  }
                },
                "range": {
                  "#class": "utils.Range.Range",
                  "specFile": "test.spec",
                  "start": {
                    "line": 11,
                    "charByteOffset": 12
                  },
                  "end": {
                    "line": 11,
                    "charByteOffset": 29
                  }
                },
                "annotation": {
                  "#class": "ReflectivePolymorphicSerializer::spec.cvlast.StorageAccessMarker"
                }
              }
            },
            "fieldName": "b3",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                    "scopeId": 9
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.VM",
                "descriptor": {
                  "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$bool"
                },
                "context": {
                  "#class": "spec.cvlast.typedescriptors.FromVMContext.StateValue"
                }
              },
              "range": {
                "#class": "utils.Range.Range",
                "specFile": "test.spec",
                "start": {
                  "line": 11,
                  "charByteOffset": 12
                },
                "end": {
                  "line": 11,
                  "charByteOffset": 32
                }
              },
              "annotation": {
                "#class": "ReflectivePolymorphicSerializer::spec.cvlast.StorageAccessMarker"
              }
            }
          },
          "r": {
            "#class": "spec.cvlast.CVLExp.RelopExp.ArithRelopExp.GtExp",
            "l": {
              "#class": "spec.cvlast.CVLExp.VariableExp",
              "id": "x",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                      "scopeId": 9
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                      ],
                      "innerScope": null
                    }
                  }
                },
                "type": {
                  "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                  "k": 256
                },
                "range": {
                  "#class": "utils.Range.Range",
                  "specFile": "test.spec",
                  "start": {
                    "line": 11,
                    "charByteOffset": 37
                  },
                  "end": {
                    "line": 11,
                    "charByteOffset": 38
                  }
                }
              },
              "twoStateIndex": "NEITHER"
            },
            "r": {
              "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
              "n": "5",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                      "scopeId": 9
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                      ],
                      "innerScope": null
                    }
                  }
                },
                "type": {
                  "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral",
                  "n": "5"
                },
                "range": {
                  "#class": "utils.Range.Range",
                  "specFile": "test.spec",
                  "start": {
                    "line": 11,
                    "charByteOffset": 41
                  },
                  "end": {
                    "line": 11,
                    "charByteOffset": 42
                  }
                }
              }
            },
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                    "scopeId": 9
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              },
              "range": {
                "#class": "utils.Range.Range",
                "specFile": "test.spec",
                "start": {
                  "line": 11,
                  "charByteOffset": 37
                },
                "end": {
                  "line": 11,
                  "charByteOffset": 42
                }
              },
              "hasParens": true
            }
          },
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                  "scopeId": 9
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                  ],
                  "innerScope": null
                }
              }
            },
            "type": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
            },
            "range": {
              "#class": "utils.Range.Range",
              "specFile": "test.spec",
              "start": {
                "line": 11,
                "charByteOffset": 12
              },
              "end": {
                "line": 11,
                "charByteOffset": 43
              }
            }
          }
        },
        "o1": {
          "out": {
            "#class": "vc.data.TACSymbol.Const",
            "value": "0",
            "tag": {
              "#class": "tac.Tag.Bool"
            }
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.FieldSelectExp",
            "structExp": {
              "#class": "spec.cvlast.CVLExp.ArrayDerefExp",
              "array": {
                "#class": "spec.cvlast.CVLExp.FieldSelectExp",
                "structExp": {
                  "#class": "spec.cvlast.CVLExp.VariableExp",
                  "id": "testContract",
                  "tag": {
                    "scope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        },
                        {
                          "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                          "scopeId": 9
                        }
                      ],
                      "innerScope": {
                        "scopeStack": [
                          {
                            "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                          }
                        ],
                        "innerScope": {
                          "scopeStack": [
                          ],
                          "innerScope": null
                        }
                      }
                    },
                    "type": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.CodeContract",
                      "name": {
                        "name": "TestContract"
                      }
                    },
                    "range": {
                      "#class": "utils.Range.Range",
                      "specFile": "test.spec",
                      "start": {
                        "line": 11,
                        "charByteOffset": 12
                      },
                      "end": {
                        "line": 11,
                        "charByteOffset": 24
                      }
                    },
                    "annotation": {
                      "#class": "ReflectivePolymorphicSerializer::spec.cvlast.CVLExp$VariableExp$ContractInstanceId",
                      "instanceId": "ce4604a0000000000000000000000001"
                    }
                  },
                  "twoStateIndex": "NEITHER"
                },
                "fieldName": "m",
                "tag": {
                  "scope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      },
                      {
                        "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                        "scopeId": 9
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        }
                      ],
                      "innerScope": {
                        "scopeStack": [
                        ],
                        "innerScope": null
                      }
                    }
                  },
                  "type": {
                    "#class": "spec.cvlast.CVLType.VM",
                    "descriptor": {
                      "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMMappingDescriptor",
                      "keyType": {
                        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                        "bitwidth": 256
                      },
                      "valueType": {
                        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.EVMStructDescriptor",
                        "canonicalId": "TestContract.sol|TestContract.Complex",
                        "location": null,
                        "fields": [
                          {
                            "fieldName": "s1",
                            "fieldType": {
                              "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.EVMStructDescriptor",
                              "canonicalId": "TestContract.sol|TestContract.Simple",
                              "location": null,
                              "fields": [
                                {
                                  "fieldName": "x",
                                  "fieldType": {
                                    "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                    "bitwidth": 256
                                  }
                                },
                                {
                                  "fieldName": "y",
                                  "fieldType": {
                                    "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.address"
                                  }
                                },
                                {
                                  "fieldName": "z1",
                                  "fieldType": {
                                    "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                    "bitwidth": 8
                                  }
                                },
                                {
                                  "fieldName": "z2",
                                  "fieldType": {
                                    "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                    "bitwidth": 8
                                  }
                                },
                                {
                                  "fieldName": "b1",
                                  "fieldType": {
                                    "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
                                  }
                                },
                                {
                                  "fieldName": "x2",
                                  "fieldType": {
                                    "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                    "bitwidth": 256
                                  }
                                },
                                {
                                  "fieldName": "b2",
                                  "fieldType": {
                                    "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
                                  }
                                }
                              ],
                              "name": "TestContract.Simple"
                            }
                          },
                          {
                            "fieldName": "s2",
                            "fieldType": {
                              "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.EVMStructDescriptor",
                              "canonicalId": "TestContract.sol|TestContract.Simple",
                              "location": null,
                              "fields": [
                                {
                                  "fieldName": "x",
                                  "fieldType": {
                                    "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                    "bitwidth": 256
                                  }
                                },
                                {
                                  "fieldName": "y",
                                  "fieldType": {
                                    "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.address"
                                  }
                                },
                                {
                                  "fieldName": "z1",
                                  "fieldType": {
                                    "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                    "bitwidth": 8
                                  }
                                },
                                {
                                  "fieldName": "z2",
                                  "fieldType": {
                                    "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                    "bitwidth": 8
                                  }
                                },
                                {
                                  "fieldName": "b1",
                                  "fieldType": {
                                    "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
                                  }
                                },
                                {
                                  "fieldName": "x2",
                                  "fieldType": {
                                    "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                    "bitwidth": 256
                                  }
                                },
                                {
                                  "fieldName": "b2",
                                  "fieldType": {
                                    "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
                                  }
                                }
                              ],
                              "name": "TestContract.Simple"
                            }
                          },
                          {
                            "fieldName": "b3",
                            "fieldType": {
                              "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
                            }
                          }
                        ],
                        "name": "TestContract.Complex"
                      },
                      "location": null
                    },
                    "context": {
                      "#class": "spec.cvlast.typedescriptors.FromVMContext.StateValue"
                    }
                  },
                  "range": {
                    "#class": "utils.Range.Range",
                    "specFile": "test.spec",
                    "start": {
                      "line": 11,
                      "charByteOffset": 12
                    },
                    "end": {
                      "line": 11,
                      "charByteOffset": 26
                    }
                  },
                  "annotation": {
                    "#class": "ReflectivePolymorphicSerializer::spec.cvlast.StorageAccessMarker"
                  }
                }
              },
              "index": {
                "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
                "n": "0",
                "tag": {
                  "scope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      },
                      {
                        "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                        "scopeId": 9
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                        {
                          "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                        }
                      ],
                      "innerScope": {
                        "scopeStack": [
                        ],
                        "innerScope": null
                      }
                    }
                  },
                  "type": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral",
                    "n": "0"
                  },
                  "range": {
                    "#class": "utils.Range.Range",
                    "specFile": "test.spec",
                    "start": {
                      "line": 11,
                      "charByteOffset": 27
                    },
                    "end": {
                      "line": 11,
                      "charByteOffset": 28
                    }
                  }
                }
              },
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                      "scopeId": 9
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                      ],
                      "innerScope": null
                    }
                  }
                },
                "type": {
                  "#class": "spec.cvlast.CVLType.VM",
                  "descriptor": {
                    "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMStructDescriptor",
                    "canonicalId": "TestContract.sol|TestContract.Complex",
                    "location": null,
                    "fields": [
                      {
                        "fieldName": "s1",
                        "fieldType": {
                          "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.EVMStructDescriptor",
                          "canonicalId": "TestContract.sol|TestContract.Simple",
                          "location": null,
                          "fields": [
                            {
                              "fieldName": "x",
                              "fieldType": {
                                "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                "bitwidth": 256
                              }
                            },
                            {
                              "fieldName": "y",
                              "fieldType": {
                                "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.address"
                              }
                            },
                            {
                              "fieldName": "z1",
                              "fieldType": {
                                "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                "bitwidth": 8
                              }
                            },
                            {
                              "fieldName": "z2",
                              "fieldType": {
                                "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                "bitwidth": 8
                              }
                            },
                            {
                              "fieldName": "b1",
                              "fieldType": {
                                "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
                              }
                            },
                            {
                              "fieldName": "x2",
                              "fieldType": {
                                "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                "bitwidth": 256
                              }
                            },
                            {
                              "fieldName": "b2",
                              "fieldType": {
                                "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
                              }
                            }
                          ],
                          "name": "TestContract.Simple"
                        }
                      },
                      {
                        "fieldName": "s2",
                        "fieldType": {
                          "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.EVMStructDescriptor",
                          "canonicalId": "TestContract.sol|TestContract.Simple",
                          "location": null,
                          "fields": [
                            {
                              "fieldName": "x",
                              "fieldType": {
                                "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                "bitwidth": 256
                              }
                            },
                            {
                              "fieldName": "y",
                              "fieldType": {
                                "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.address"
                              }
                            },
                            {
                              "fieldName": "z1",
                              "fieldType": {
                                "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                "bitwidth": 8
                              }
                            },
                            {
                              "fieldName": "z2",
                              "fieldType": {
                                "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                "bitwidth": 8
                              }
                            },
                            {
                              "fieldName": "b1",
                              "fieldType": {
                                "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
                              }
                            },
                            {
                              "fieldName": "x2",
                              "fieldType": {
                                "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
                                "bitwidth": 256
                              }
                            },
                            {
                              "fieldName": "b2",
                              "fieldType": {
                                "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
                              }
                            }
                          ],
                          "name": "TestContract.Simple"
                        }
                      },
                      {
                        "fieldName": "b3",
                        "fieldType": {
                          "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"
                        }
                      }
                    ],
                    "name": "TestContract.Complex"
                  },
                  "context": {
                    "#class": "spec.cvlast.typedescriptors.FromVMContext.StateValue"
                  }
                },
                "range": {
                  "#class": "utils.Range.Range",
                  "specFile": "test.spec",
                  "start": {
                    "line": 11,
                    "charByteOffset": 12
                  },
                  "end": {
                    "line": 11,
                    "charByteOffset": 29
                  }
                },
                "annotation": {
                  "#class": "ReflectivePolymorphicSerializer::spec.cvlast.StorageAccessMarker"
                }
              }
            },
            "fieldName": "b3",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                    "scopeId": 9
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.VM",
                "descriptor": {
                  "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$bool"
                },
                "context": {
                  "#class": "spec.cvlast.typedescriptors.FromVMContext.StateValue"
                }
              },
              "range": {
                "#class": "utils.Range.Range",
                "specFile": "test.spec",
                "start": {
                  "line": 11,
                  "charByteOffset": 12
                },
                "end": {
                  "line": 11,
                  "charByteOffset": 32
                }
              },
              "annotation": {
                "#class": "ReflectivePolymorphicSerializer::spec.cvlast.StorageAccessMarker"
              }
            }
          }
        },
        "o2": {
          "out": {
            "#class": "vc.data.TACSymbol.Const",
            "value": "0",
            "tag": {
              "#class": "tac.Tag.Bool"
            }
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.RelopExp.ArithRelopExp.GtExp",
            "l": {
              "#class": "spec.cvlast.CVLExp.VariableExp",
              "id": "x",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                      "scopeId": 9
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                      ],
                      "innerScope": null
                    }
                  }
                },
                "type": {
                  "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                  "k": 256
                },
                "range": {
                  "#class": "utils.Range.Range",
                  "specFile": "test.spec",
                  "start": {
                    "line": 11,
                    "charByteOffset": 37
                  },
                  "end": {
                    "line": 11,
                    "charByteOffset": 38
                  }
                }
              },
              "twoStateIndex": "NEITHER"
            },
            "r": {
              "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
              "n": "5",
              "tag": {
                "scope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    },
                    {
                      "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                      "scopeId": 9
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                      {
                        "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                      }
                    ],
                    "innerScope": {
                      "scopeStack": [
                      ],
                      "innerScope": null
                    }
                  }
                },
                "type": {
                  "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral",
                  "n": "5"
                },
                "range": {
                  "#class": "utils.Range.Range",
                  "specFile": "test.spec",
                  "start": {
                    "line": 11,
                    "charByteOffset": 41
                  },
                  "end": {
                    "line": 11,
                    "charByteOffset": 42
                  }
                }
              }
            },
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                    "scopeId": 9
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
              },
              "range": {
                "#class": "utils.Range.Range",
                "specFile": "test.spec",
                "start": {
                  "line": 11,
                  "charByteOffset": 37
                },
                "end": {
                  "line": 11,
                  "charByteOffset": 42
                }
              },
              "hasParens": true
            }
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "test.spec",
        "start": {
          "line": 11,
          "charByteOffset": 4
        },
        "end": {
          "line": 11,
          "charByteOffset": 44
        }
      }
    }
  ],
  "136": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 25
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "test.spec",
        "start": {
          "line": 72,
          "charByteOffset": 4
        },
        "end": {
          "line": 72,
          "charByteOffset": 16
        }
      }
    }
  ],
  "137": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.NullaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.FieldSelectExp",
          "structExp": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "s",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 8
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                    {
                      "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                    }
                  ],
                  "innerScope": {
                    "scopeStack": [
                    ],
                    "innerScope": null
                  }
                }
              },
              "type": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "TestContract.Complex",
                "fields": [
                  {
                    "fieldName": "s1",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                      "name": "TestContract.Simple",
                      "fields": [
                        {
                          "fieldName": "x",
                          "cvlType": {
                            "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                            "k": 256
                          }
                        },
                        {
                          "fieldName": "y",
                          "cvlType": {
                            "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                          }
                        },
                        {
                          "fieldName": "z1",
                          "cvlType": {
                            "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                            "k": 8
                          }
                        },
                        {
                          "fieldName": "z2",
                          "cvlType": {
                            "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                            "k": 8
                          }
                        },
                        {
                          "fieldName": "b1",
                          "cvlType": {
                            "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                          }
                        },
                        {
                          "fieldName": "x2",
                          "cvlType": {
                            "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                            "k": 256
                          }
                        },
                        {
                          "fieldName": "b2",
                          "cvlType": {
                            "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                          }
                        }
                      ]
                    }
                  },
                  {
                    "fieldName": "s2",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                      "name": "TestContract.Simple",
                      "fields": [
                        {
                          "fieldName": "x",
                          "cvlType": {
                            "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                            "k": 256
                          }
                        },
                        {
                          "fieldName": "y",
                          "cvlType": {
                            "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                          }
                        },
                        {
                          "fieldName": "z1",
                          "cvlType": {
                            "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                            "k": 8
                          }
                        },
                        {
                          "fieldName": "z2",
                          "cvlType": {
                            "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                            "k": 8
                          }
                        },
                        {
                          "fieldName": "b1",
                          "cvlType": {
                            "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                          }
                        },
                        {
                          "fieldName": "x2",
                          "cvlType": {
                            "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                            "k": 256
                          }
                        },
                        {
                          "fieldName": "b2",
                          "cvlType": {
                            "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                          }
                        }
                      ]
                    }
                  },
                  {
                    "fieldName": "b3",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
                    }
                  }
                ]
              },
              "range": {
                "#class": "utils.Range.Range",
                "specFile": "test.spec",
                "start": {
                  "line": 72,
                  "charByteOffset": 11
                },
                "end": {
                  "line": 72,
                  "charByteOffset": 12
                }
              }
            },
            "twoStateIndex": "NEITHER"
          },
          "fieldName": "b3",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 8
                }
              ],
              "innerScope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  }
                ],
                "innerScope": {
                  "scopeStack": [
                  ],
                  "innerScope": null
                }
              }
            },
            "type": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Bool"
            },
            "range": {
              "#class": "utils.Range.Range",
              "specFile": "test.spec",
              "start": {
                "line": 72,
                "charByteOffset": 11
              },
              "end": {
                "line": 72,
                "charByteOffset": 15
              }
            }
          }
        }
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "test.spec",
        "start": {
          "line": 72,
          "charByteOffset": 4
        },
        "end": {
          "line": 72,
          "charByteOffset": 16
        }
      }
    }
  ],
  "138": [
    {
      "key": {
        "name": "cvl.user.defined.assert",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "test.spec",
        "start": {
          "line": 72,
          "charByteOffset": 4
        },
        "end": {
          "line": 72,
          "charByteOffset": 16
        }
      }
    }
  ]
}