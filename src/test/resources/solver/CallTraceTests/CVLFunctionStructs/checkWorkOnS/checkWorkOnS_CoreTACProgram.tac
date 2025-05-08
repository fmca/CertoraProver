TACSymbolTable {
	UserDefined {
		UninterpSort skey
	}
	BuiltinFunctions {
		to_skey:JSON{"#class":"vc.data.TACBuiltInFunction.Hash.ToSkey"}
		skey_basic:JSON{"#class":"vc.data.TACBuiltInFunction.Hash.Basic"}
		safe_math_narrow_bv256:JSON{"#class":"vc.data.TACBuiltInFunction.SafeMathNarrow","returnSort":{"bits":256}}
		hash_3_keccak:JSON{"#class":"vc.data.TACBuiltInFunction.Hash.SimpleHashApplication","arity":3,"hashFamily":{"#class":"vc.data.HashFamily.Keccack"}}
		skey_add:JSON{"#class":"vc.data.TACBuiltInFunction.Hash.Addition"}
	}
	UninterpretedFunctions {
	}
	tacMCANON0!!46:bytemap:0
	tacMCANON0!!48:bytemap:0
	tacMCANON0!!52:bytemap:0
	tacMCANON0!!59:bytemap:0
	tacMCANON0!!61:bytemap:0
	tacMCANON0!!63:bytemap:0
	tacMCANON0!!67:bytemap:0
	tacMCANON0!!71:bytemap:0
	tacMCANON0!!77:bytemap:0
	tacReturndata!!82:bytemap:1
	tacM0x40@1:bv256:2
	tacCodesizeCANON0:bv256:3
	tacCalldatabufCANON0@1:bv256:4
	tacMCANON1!!4:bytemap:5
	tacM0x40!!0:bv256:2
	tacAddress!!33:bv256:6
	lastReverted:bool:7
	CANON2!!21:int:8
	CANON2!!83:int:8
	tacExtcodesize!!3:wordmap:9
	CANON47!!7:wordmap:10
	CANON50!!9:wordmap:11
	tacCalldatasize:bv256:12
	tacCalldatasize@1:bv256:12
	tacReturndata@1:bytemap:1
	calledContract:int:13
	tacExtcodesize:wordmap:9
	tacCalldatasize!!30:bv256:12
	tacMCANON0@1:bytemap:0
	tacMCANON1@1:bytemap:5
	tacMCANON2@1:bytemap:14
	tacBalance:wordmap:15
	CANON51!!10:wordmap:16
	tacBalance!!38:wordmap:15
	CANON52!!11:wordmap:17
	CANON53!!12:wordmap:18
	CANON53!!93:wordmap:18
	tacBalance!!5:wordmap:15
	CANON58!!13:wordmap:19
	tacCalldatabuf@1:bytemap:20
	R1:bv256:3
	R8:bv256:21
	B23:bool:21
	B24:bool:21
	B27:bool
	B64:bool:22
	B74:bool:22
	B84:bool:21
	B85:bool:21
	B86:bool:21
	B87:bool:21
	B91:bool:21
	B94:bool
	B99:bool
	I25:int
	I26:int
	I28:int
	I29:int
	I37:int:21
	I40:int:21
	I88:int
	I95:int
	R15:bv256:23
	R16:bv256:24
	R17:bv256:25
	R18:bv256:26
	R22:bv256:21
	R31:bv256:21
	R34:bv256:21
	R35:bv256:21
	R36:bv256:21
	R39:bv256:21
	R41:bv256:21
	R42:bv256:21
	R43:bv256:27
	R44:(uninterp) skey:28
	R45:bv256:21
	R47:bv256:29
	R49:bv256:30
	R50:bv256:30
	R51:bv256:31
	R53:(uninterp) skey:30
	R54:bv256:30
	R55:bv256:30
	R56:bv256:30
	R57:bv256:30
	R58:bv256:32
	R60:bv256:33
	R62:bv256:34
	R65:bv256:22
	R66:bv256:35
	R68:(uninterp) skey:30
	R69:bv256:30
	R70:bv256:36
	R72:(uninterp) skey:30
	R73:bv256:30
	R75:bv256:22
	R76:bv256:37
	R78:bv256:38
	R79:bv256:39
	R80:bv256:40
	R81:bv256:40
	R89:(uninterp) skey:21
	R90:(uninterp) skey:21
	R92:bv256:21
	R96:(uninterp) skey:21
	R97:(uninterp) skey:21
	R98:bv256:21
	B102:bool
	B108:bool:21
	B109:bool
	I100:int
	I101:int
	I104:int
	R105:(uninterp) skey:21
	R106:(uninterp) skey:21
	R107:bv256:21
	lastHasThrown!!103:bool:41
	CANON22!6:ghostmap(bv256*bv256*bv256->bv256):42
	tacAddress@1:bv256:6
	LCANON0@1:bv256:27
	LCANON1@1:bv256:28
	LCANON2@1:bv256:43
	LCANON3@1:bv256:30
	LCANON4@1:bv256:44
	LCANON5@1:bv256:30
	LCANON6@1:bv256:30
	LCANON7@1:bv256:30
	LCANON8@1:bv256:30
	LCANON9@1:bool:22
	CANON60!!14:wordmap:45
	CANON10:int:46
	CANON11:int:47
	CANON12:int:48
	CANON13:int:49
	CANON14:int:50
	CANON15:int:51
	CANON16:int:52
	CANON17:int:53
	CANON18:int:54
	CANON19:int
	CANON20:int
	CANON22:ghostmap(bv256*bv256*bv256->bv256):42
	CANON23:bv256:21
	CANON36:bv256:21
	CANON37:bv256:21
	CANON38:bv256:21
	CANON39:bv256:21
	CANON40:int:21
	CANON41:bv256:21
	CANON42:int:21
	CANON43:bv256:21
	CANON44@1:bv256:21
	CANON45@1:bv256:21
	CANON46@1:bv256:29
	CANON47:wordmap:10
	CANON48@1:bv256:21
	CANON49@1:bv256:31
	CANON50:wordmap:11
	CANON51:wordmap:16
	CANON52:wordmap:17
	CANON53:wordmap:18
	CANON54@1:bv256:32
	CANON55@1:bv256:33
	CANON56@1:bv256:34
	CANON57@1:bv256:35
	CANON58:wordmap:19
	CANON59@1:bv256:36
	CANON60:wordmap:45
	CANON61@1:bv256:37
	CANON62:int:55
	CANON63:bool:21
	CANON64:bool:21
	CANON65:bool:21
	CANON66:bool:21
	CANON67:int:56
	CANON68:int:57
	CANON69:int:58
	CANON70:int:59
	CANON71:bool:60
	CANON72:int:61
	CANON73:bool:62
	CANON74:int
	CANON75@2:bv256:21
	CANON76@2:bv256:63
	CANON77@2:bool:21
	CANON78@2:bv256:21
	CANON79:bool
	CANON80:int
	CANON81@2:bv256:21
	CANON82@2:bv256:64
	CANON83@2:bv256:21
	CANON84:bool
	CANON85:int
	CANON86:int
	CANON87:bool
	CANON88:bool:65
	CANON89:int
	CANON90:bv256:21
	CANON91:bv256:66
	CANON92:bv256:21
	CANON93:bool:21
	CANON94:bool
	LCANON10@1:bv256:22
	LCANON11@1:bv256:67
	LCANON12@1:bv256:30
	LCANON13@1:bv256:68
	LCANON14@1:bv256:30
	LCANON15@1:bool:22
	LCANON16@1:bv256:22
	LCANON17@1:bv256:38
	LCANON18@1:bv256:39
	LCANON19@1:bv256:40
	LCANON20@1:bv256:40
	tacContractAtCANON1:bv256:23
	tacContractAtCANON2:bv256:24
	tacContractAtCANON3:bv256:25
	executingContract:int:69
	lastHasThrown:bool:41
	CANON1:int:70
	CANON2:int:8
	CANON3:bv256:21
	CANON4:bool:21
	CANON5:bool:21
	CANON6:int
	CANON7:int
	CANON8:bool
	CANON9:int:71
	tacContractAtCANON:bv256:26
	tacCalldatasize!!2:bv256:12
	tacMCANON0havocme606@1:bytemap:72
	lastHasThrown!!32:bool:41
	tacSighash!!20:bv256:73
	tacSighash@1:bv256:73
	CANON:int:74
	tacMCANON0havocme606!!19:bytemap:72
}
Program {
	Block 0_0_0_0_0_0 Succ [1_0_0_1_0_0] {
		AssignHavocCmd tacM0x40!!0:2
		AssumeExpCmd Le(tacM0x40!!0:2 0x80 )
		AssignHavocCmd R1:3
		AssumeExpCmd Ge(R1:3 0x1 )
		AssignHavocCmd tacCalldatasize!!2:12
		AssignHavocCmd tacExtcodesize!!3:9
		AssignExpCmd tacMCANON1!!4:5 MapDefinition(i.609:bv256 -> 0x0 bytemap)
		AssignHavocCmd tacBalance!!5:15
		AssignHavocCmd CANON10:46
		AssumeExpCmd Eq(CANON10:46 0x0(int) )
		AssignHavocCmd CANON11:47
		AssumeExpCmd LAnd(Ge(CANON11:47 0x0(int) ) Le(CANON11:47 0xffffffffffffffffffffffffffffffffffffffff(int) ) )
		AssignHavocCmd CANON12:48
		AssumeExpCmd LAnd(Ge(CANON12:48 0x0(int) ) Le(CANON12:48 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff(int) ) )
		AssignHavocCmd CANON13:49
		AssumeExpCmd LAnd(Ge(CANON13:49 0x0(int) ) Le(CANON13:49 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff(int) ) )
		AssignHavocCmd CANON14:50
		AssumeExpCmd LAnd(Ge(CANON14:50 0x0(int) ) Le(CANON14:50 0xffffffffffffffffffffffffffffffffffffffff(int) ) )
		AssignHavocCmd CANON15:51
		AssumeExpCmd LAnd(Ge(CANON15:51 0x0(int) ) Le(CANON15:51 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff(int) ) )
		AssignHavocCmd CANON16:52
		AssumeExpCmd LAnd(Ge(CANON16:52 0x0(int) ) Le(CANON16:52 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff(int) ) )
		AssignHavocCmd CANON17:53
		AssumeExpCmd LAnd(Ge(CANON17:53 0x0(int) ) Le(CANON17:53 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff(int) ) )
		AssignHavocCmd CANON18:54
		AssumeExpCmd LAnd(Ge(CANON18:54 0x0(int) ) Le(CANON18:54 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff(int) ) )
		AssignHavocCmd CANON22!6:42
		AssignHavocCmd CANON47!!7:10
		AssignHavocCmd R8:21
		AssignHavocCmd CANON50!!9:11
		AssignHavocCmd CANON51!!10:16
		AssignHavocCmd CANON52!!11:17
		AssignHavocCmd CANON53!!12:18
		AssignHavocCmd CANON58!!13:19
		AssignHavocCmd CANON60!!14:45
		AssignHavocCmd R15:23
		AssumeExpCmd Eq(R15:23 0x1 )
		AssignHavocCmd R16:24
		AssumeExpCmd Eq(R16:24 0x2 )
		AssignHavocCmd R17:25
		AssumeExpCmd Eq(R17:25 0x4 )
		AssignHavocCmd CANON9:71
		AssumeExpCmd LAnd(Ge(CANON9:71 0x0(int) ) Le(CANON9:71 0xffffffffffffffffffffffffffffffffffffffff(int) ) )
		AssignHavocCmd R18:26
		AssumeExpCmd LAnd(Ge(R18:26 0x1 ) Le(R18:26 0xffffffffffffffffffffffffffffffffffffffff ) )
		AssignExpCmd tacMCANON0havocme606!!19:72 MapDefinition(i.610:bv256 -> 0x0 bytemap)
		AssignHavocCmd tacSighash!!20:73
		AssumeExpCmd Eq(tacSighash!!20:73 0x2f0949c5 )
		AnnotationCmd JSON{"key":{"name":"tac.state.extension","type":"analysis.icfg.Inliner$ExtendedStateVars","erasureStrategy":"Canonical"},"value":"rO0ABXNyACdhbmFseXNpcy5pY2ZnLklubGluZXIkRXh0ZW5kZWRTdGF0ZVZhcnOvh/MjxNFkQAIAAUwAFmluc3RhbmNlVG9FeHRlbmRlZFZhcnN0AA9MamF2YS91dGlsL01hcDt4cHNyACFkYXRhc3RydWN0dXJlcy5MaW5rZWRBcnJheUhhc2hNYXAAAAAAAAAAAQMAAkYACmxvYWRGYWN0b3JMAAloYXNoVGFibGV0AC5MZGF0YXN0cnVjdHVyZXMvYXJyYXloYXNodGFibGUvQXJyYXlIYXNoVGFibGU7eHB3CAAAAAFAAAAAc3IAFGphdmEubWF0aC5CaWdJbnRlZ2VyjPyfH6k7+x0DAAZJAAhiaXRDb3VudEkACWJpdExlbmd0aEkAE2ZpcnN0Tm9uemVyb0J5dGVOdW1JAAxsb3dlc3RTZXRCaXRJAAZzaWdudW1bAAltYWduaXR1ZGV0AAJbQnhyABBqYXZhLmxhbmcuTnVtYmVyhqyVHQuU4IsCAAB4cP///////////////v////4AAAABdXIAAltCrPMX+AYIVOACAAB4cAAAABDORgSgAAAAAAAAAAAAAAABeHNxAH4AA3cIAAAAAEAAAAB4eA=="}
		AnnotationCmd:75 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"rule parameters setup"}}
		AssignHavocCmd CANON:74
		AssumeExpCmd LAnd(Ge(CANON:74 0x0(int) ) Le(CANON:74 0x2(int) ) )
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.CVLSnippetCmd.CVLArg.PrimitiveArg","callIndex":0,"index":0,"sym":{"namePrefix":"CANON","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":11,"charByteOffset":18},"end":{"line":11,"charByteOffset":24}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"x"}]},"param":{"Named_type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"id":"x","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":11,"charByteOffset":18},"end":{"line":11,"charByteOffset":24}}}}}
		AnnotationCmd JSON{"key":{"name":"cvl.trace.declaration","type":"spec.CVLCompiler$Companion$TraceMeta$VariableDeclaration","erasureStrategy":"Erased"},"value":{"v":{"#class":"spec.CVLCompiler.Companion.TraceMeta.ValueIdentity.TACVar","t":{"namePrefix":"CANON","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":11,"charByteOffset":18},"end":{"line":11,"charByteOffset":24}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"x"}]}},"t":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"type":{"#class":"spec.CVLCompiler.Companion.TraceMeta.DeclarationType.Parameter","sourceName":"x"},"fields":null}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":0}
		AnnotationCmd:76 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"Setup"}}
		AnnotationCmd:77 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"multi contract setup"}}
		AssignExpCmd CANON1:70 R18:78
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":2}
		AnnotationCmd:79 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"contract address vars initialized"}}
		AssignExpCmd CANON2!!21:8 R18:78
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":3}
		AnnotationCmd:80 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"setup read tracking instrumentation"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":4}
		AnnotationCmd:81 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"last storage initialize"}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule"}},{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.NonTACKeywordEntry","name":"lastStorage"}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":5}
		AnnotationCmd:82 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assuming contracts in scene with non-empty bytecode have EXTCODESIZE larger than zero"}}
		AssignExpCmd R22:21 Select(tacExtcodesize!!3:9 Apply(to_skey:bif R18:78) )
		AssumeExpCmd Ge(R22:21 0x1 )
		AssumeExpCmd Eq(R22:83 R1:84 )
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":6}
		AnnotationCmd:85 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assuming address(0).code has no code deployed"}}
		AssignExpCmd B24:21 Eq(Select(tacExtcodesize!!3:9 Apply(skey_basic:bif 0x0) ) 0x0 )
		AssumeCmd B24:21 "expToAssumeCmd"
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":7}
		AnnotationCmd:86 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about contracts' addresses"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":8}
		AnnotationCmd:87 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about static addresses"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":9}
		AnnotationCmd:88 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"establish addresses of precompiled contracts"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":10}
		AnnotationCmd:89 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about uniqueness of contracts' addresses"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":11}
		AnnotationCmd:90 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"static links"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":12}
		AnnotationCmd:91 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"record starting nonces"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":13}
		AnnotationCmd:92 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"cloned contracts have no balances"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":14}
		AnnotationCmd:93 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"Linked immutable setup"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":15}
		AnnotationCmd:94 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"Constrain immutables"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":16}
		AnnotationCmd:95 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"establish equivalence of extension and base contract immutables"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":17}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1}
		AnnotationCmd:96 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.AssumeCmd.Assume","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":12,"charByteOffset":4},"end":{"line":12,"charByteOffset":18}},"exp":{"#class":"spec.cvlast.CVLExp.RelopExp.ArithRelopExp.LtExp","l":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"x","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":1}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":12,"charByteOffset":12},"end":{"line":12,"charByteOffset":13}}},"twoStateIndex":"NEITHER"},"r":{"#class":"spec.cvlast.CVLExp.Constant.NumberLit","n":"3","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":1}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral","n":"3"},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":12,"charByteOffset":16},"end":{"line":12,"charByteOffset":17}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":1}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":12,"charByteOffset":12},"end":{"line":12,"charByteOffset":17}}}},"description":null,"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":1}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssignExpCmd:97 I25 CANON:74
		AssignExpCmd:98 I26 0x3
		AssignExpCmd:99 B27 true
		AnnotationCmd:100 JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":18}
		AnnotationCmd:101 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Declaration","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":14,"charByteOffset":4},"end":{"line":14,"charByteOffset":10}},"cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"id":"e","scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":1}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AnnotationCmd JSON{"key":{"name":"cvl.trace.declaration","type":"spec.CVLCompiler$Companion$TraceMeta$VariableDeclaration","erasureStrategy":"Erased"},"value":{"v":{"#class":"spec.CVLCompiler.Companion.TraceMeta.ValueIdentity.CVLVar","id":"e290"},"t":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"type":{"#class":"spec.CVLCompiler.Companion.TraceMeta.DeclarationType.Variable"},"fields":[[{"#class":"tac.DataField.StructField","field":"block"},{"#class":"tac.DataField.StructField","field":"coinbase"}],{"namePrefix":"CANON14","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"fields":[{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":14,"charByteOffset":4},"end":{"line":14,"charByteOffset":10}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"e.block.coinbase"}]},[{"#class":"tac.DataField.StructField","field":"block"},{"#class":"tac.DataField.StructField","field":"basefee"}],{"namePrefix":"CANON12","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"fields":[{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":14,"charByteOffset":4},"end":{"line":14,"charByteOffset":10}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"e.block.basefee"}]},[{"#class":"tac.DataField.StructField","field":"block"},{"#class":"tac.DataField.StructField","field":"timestamp"}],{"namePrefix":"CANON18","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"fields":[{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":14,"charByteOffset":4},"end":{"line":14,"charByteOffset":10}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"e.block.timestamp"}]},[{"#class":"tac.DataField.StructField","field":"block"},{"#class":"tac.DataField.StructField","field":"blobbasefee"}],{"namePrefix":"CANON13","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"fields":[{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":14,"charByteOffset":4},"end":{"line":14,"charByteOffset":10}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"e.block.blobbasefee"}]},[{"#class":"tac.DataField.StructField","field":"tx"},{"#class":"tac.DataField.StructField","field":"origin"}],{"namePrefix":"CANON11","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"fields":[{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":14,"charByteOffset":4},"end":{"line":14,"charByteOffset":10}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"e.tx.origin"}]},[{"#class":"tac.DataField.StructField","field":"msg"},{"#class":"tac.DataField.StructField","field":"sender"}],{"namePrefix":"CANON9","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":14,"charByteOffset":4},"end":{"line":14,"charByteOffset":10}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"e.msg.sender"}]},[{"#class":"tac.DataField.StructField","field":"msg"},{"#class":"tac.DataField.StructField","field":"value"}],{"namePrefix":"CANON10","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":14,"charByteOffset":4},"end":{"line":14,"charByteOffset":10}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"e.msg.value"}]},[{"#class":"tac.DataField.StructField","field":"block"},{"#class":"tac.DataField.StructField","field":"difficulty"}],{"namePrefix":"CANON15","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"fields":[{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":14,"charByteOffset":4},"end":{"line":14,"charByteOffset":10}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"e.block.difficulty"}]},[{"#class":"tac.DataField.StructField","field":"block"},{"#class":"tac.DataField.StructField","field":"gaslimit"}],{"namePrefix":"CANON16","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"fields":[{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":14,"charByteOffset":4},"end":{"line":14,"charByteOffset":10}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"e.block.gaslimit"}]},[{"#class":"tac.DataField.StructField","field":"block"},{"#class":"tac.DataField.StructField","field":"number"}],{"namePrefix":"CANON17","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"fields":[{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":14,"charByteOffset":4},"end":{"line":14,"charByteOffset":10}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"e.block.number"}]}]}}
		AnnotationCmd:102 JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":19}
		AnnotationCmd:103 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Apply","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":15,"charByteOffset":4},"end":{"line":15,"charByteOffset":21}},"exp":{"#class":"spec.cvlast.CVLExp.ApplyExp.ContractFunction.Concrete","methodIdWithCallContext":{"#class":"spec.cvlast.ConcreteMethod","signature":{"#class":"spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig","wrapped":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"TestContract"},"methodId":"workOnSExt"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"x","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}],"res":[]},"sighashInt":{"n":"2f0949c5"}}},"args":[{"#class":"spec.cvlast.CVLExp.VariableExp","id":"e","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":1}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":15,"charByteOffset":15},"end":{"line":15,"charByteOffset":16}}},"twoStateIndex":"NEITHER"},{"#class":"spec.cvlast.CVLExp.VariableExp","id":"x","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":1}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":15,"charByteOffset":18},"end":{"line":15,"charByteOffset":19}}},"twoStateIndex":"NEITHER"}],"noRevert":true,"storage":{"id":"lastStorage","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":1}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"},"range":{"#class":"utils.Range.Empty","comment":"empty storage type"}},"twoStateIndex":"NEITHER"},"isWhole":false,"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":1}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Void"},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":15,"charByteOffset":4},"end":{"line":15,"charByteOffset":20}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.CallResolution$DirectPassing","target":{"methodSignature":{"#class":"spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig","wrapped":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"TestContract"},"methodId":"workOnSExt"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"x","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}],"res":[]},"sighashInt":{"n":"2f0949c5"}},"definitelyNonPayable":true,"annotation":{"visibility":"EXTERNAL","envFree":false,"library":false,"virtual":false},"stateMutability":"nonpayable","evmExternalMethodInfo":{"sigHash":"2f0949c5","name":"workOnSExt","argTypes":[{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}],"resultTypes":[],"stateMutability":"nonpayable","isConstant":false,"paramNames":["x"],"isLibrary":false,"contractName":"TestContract","contractInstanceId":"ce4604a0000000000000000000000001","sourceSegment":{"range":{"specFile":"TestContract.sol","start":{"line":15,"charByteOffset":4},"end":{"line":17,"charByteOffset":5}},"content":"function workOnSExt(uint x) external {\n        this.workOnS(x, m[0]);\n    }"}}},"hasEnv":true}}},"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":1}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AnnotationCmd JSON{"key":{"name":"cvl.trace.data.movement","type":"spec.CVLCompiler$Companion$TraceMeta$CVLMovement","erasureStrategy":"Erased"},"value":{"dst":{"id":"certoraArg296297"},"src":{"id":"e290"}}}
		AssignExpCmd:104 I29 CANON:74
	}
	Block 1_0_0_1_0_0 Succ [2_0_0_2_0_1] {
		AnnotationCmd:105 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":{"callee":{"contractId":"ce4604a0000000000000000000000001","sigHash":{"n":"2f0949c5"},"attr":{"#class":"scene.MethodAttribute.Common"}},"summary":null,"convention":{"#class":"analysis.icfg.Inliner.CallConventionType.FromCVL"},"calleeId":1}}
		AssignHavocCmd:105 tacCalldatasize!!30:12
		AssumeExpCmd Eq(tacCalldatasize!!30:12 0x24 )
		AssignExpCmd:105 tacCalldatabuf@1:20 MapDefinition(CANON21.608:bv256 -> Ite(Lt(CANON21.608 tacCalldatasize!!30:12 ) Select(Select(Select(CANON22!6:42 CANON21.608 ) tacCalldatasize!!30:12 ) 0x2f0949c5 ) 0x0 ) bytemap)
		AssignExpCmd:105 R31:21 Select(Select(Select(CANON22!6:42 0x0 ) 0x24 ) 0x2f0949c5 )
		AssumeExpCmd LAnd(Ge(R31:21 0x2f0949c500000000000000000000000000000000000000000000000000000000 ) Le(R31:21 0x2f0949c5ffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) )
		AnnotationCmd:105 JSON{"key":{"name":"cvl.arg-serialization.start","type":"spec.CVLInvocationCompiler$StartSerializationMarker","erasureStrategy":"Canonical"},"value":{"id":0,"callId":1}}
		LabelCmd:105 "0: Read primitive from certoraArg298299:int..."
		AssertCmd:106 true "sanity bounds check on cvl to vm encoding (unsigned int elements of a user array) of %1$s failed"
		AssertCmd:106 true "sanity bounds check on cvl to vm encoding (unsigned int elements of a user array) of %1$s failed"
		AssignExpCmd:105 tacCalldatabufCANON0@1:107 Apply(safe_math_narrow_bv256:bif I29)
		LabelCmd:105 "...done 0"
		AnnotationCmd JSON{"key":{"name":"cvl.trace.external","type":"spec.CVLCompiler$Companion$TraceMeta$ExternalArg","erasureStrategy":"Erased"},"value":{"s":{"#class":"spec.CVLCompiler.Companion.TraceMeta.ValueIdentity.TACVar","t":{"namePrefix":"I29","tag":{"#class":"tac.Tag.Int"},"callIndex":0}},"rootOffset":"0","callId":1,"targetType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"sourceType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"fields":null}}
		AnnotationCmd:105 JSON{"key":{"name":"cvl.arg-serialization.end","type":"spec.CVLInvocationCompiler$EndSerializationMarker","erasureStrategy":"Canonical"},"value":{"id":0,"callId":1}}
		AssignExpCmd:105 lastHasThrown!!32:41 false
		AssertCmd:108 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:109 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:110 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:111 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:112 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:113 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:114 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:115 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:116 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:117 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:118 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:119 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssignExpCmd:105 R34:21 Apply(safe_math_narrow_bv256:bif CANON9:71)
		AssignExpCmd:105 R36:21 Select(tacBalance!!5:15 Apply(to_skey:bif R34:21) )
		AssignExpCmd:120 tacBalance!!38:15 Store(tacBalance!!5:15 Apply(to_skey:bif R34:21) R36:21 )
		AssignExpCmd:105 R39:21 Select(tacBalance!!38:15 Apply(to_skey:bif R18:78) )
		AssignExpCmd:120 R41:21 Apply(safe_math_narrow_bv256:bif R39:21)
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.TransferSnippet","srcAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R36","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R36","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R34","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}},"trgAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R39","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R41","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R18","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.NonTACKeywordEntry","name":"tacContractAt"}},{"key":{"name":"tac.contract.sym.addr.name","type":"java.lang.String","erasureStrategy":"Erased"},"value":"TestContract"},{"key":{"name":"tac.contract.sym.addr","type":"java.math.BigInteger","erasureStrategy":"Erased"},"value":"ce4604a0000000000000000000000001"}]}},"transferredAmount":{"#class":"vc.data.TACSymbol.Const","value":"0"}}}
		LabelCmd:105 "Start procedure TestContract-workOnSExt(uint256)"
		AnnotationCmd:105 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:105 R42:21 Select(tacExtcodesize!!3:9 Apply(to_skey:bif R18:121) )
		AssumeExpCmd Ge(R42:21 0x1 )
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.RawStorageAccess.WithLocSym","isLoad":true,"loc":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R18","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"tacAddress","maybeTACKeywordOrdinal":22}},{"key":{"name":"tac.env.known-bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.contract.sym.addr.name","type":"java.lang.String","erasureStrategy":"Erased"},"value":"TestContract"},{"key":{"name":"tac.contract.sym.addr","type":"java.math.BigInteger","erasureStrategy":"Erased"},"value":"ce4604a0000000000000000000000001"}]},"contractInstance":"ce4604a0000000000000000000000001","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R42","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"storageType":null,"range":null}}
		AnnotationCmd:105 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":{"unresolvedFunctions":[]}}
		AnnotationCmd:105 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AnnotationCmd:105 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":0,"bytecodeCount":8,"sources":[{"source":0,"begin":25,"end":866}]}}
		LabelCmd "→ Assuming FP is strictly monotonic increasing"
		LabelCmd "←"
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.StartBranchSnippet","branchIndex":0,"branchSource":{"range":{"specFile":"TestContract.sol","start":{"line":2,"charByteOffset":0},"end":{"line":26,"charByteOffset":1}},"content":"contract TestContract {...}"}}}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.EndBranchSnippet","branchIndex":0}}
		AnnotationCmd:122 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":16,"bytecodeCount":7,"sources":[{"source":0,"begin":25,"end":866}]}}
		AnnotationCmd:122 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":26,"bytecodeCount":9,"sources":[{"source":0,"begin":25,"end":866}]}}
		AnnotationCmd:122 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":59,"bytecodeCount":14,"sources":[{"source":0,"begin":235,"end":310}]}}
		AnnotationCmd:123 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":498,"bytecodeCount":10,"sources":[{"source":1,"begin":690,"end":1019},{"source":1,"begin":749,"end":755},{"source":1,"begin":798,"end":800},{"source":1,"begin":786,"end":795},{"source":1,"begin":777,"end":784},{"source":1,"begin":773,"end":796},{"source":1,"begin":769,"end":801},{"source":1,"begin":766,"end":885}]}}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.StartBranchSnippet","branchIndex":1,"branchSource":{"range":{"specFile":"TestContract.sol","start":{"line":15,"charByteOffset":4},"end":{"line":17,"charByteOffset":5}},"content":"compiler-generate condition in function workOnSExt(uint x) external "}}}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.EndBranchSnippet","branchIndex":1}}
		AnnotationCmd:105 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":520,"bytecodeCount":9,"sources":[{"source":1,"begin":766,"end":885},{"source":1,"begin":924,"end":925},{"source":1,"begin":949,"end":1002},{"source":1,"begin":994,"end":1001},{"source":1,"begin":985,"end":991},{"source":1,"begin":974,"end":983},{"source":1,"begin":970,"end":992}]}}
		AnnotationCmd:105 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":477,"bytecodeCount":10,"sources":[{"source":1,"begin":545,"end":684},{"source":1,"begin":591,"end":596},{"source":1,"begin":629,"end":635},{"source":1,"begin":616,"end":636},{"source":1,"begin":607,"end":636},{"source":1,"begin":645,"end":678},{"source":1,"begin":672,"end":677}]}}
		AnnotationCmd:105 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":454,"bytecodeCount":5,"sources":[{"source":1,"begin":417,"end":539},{"source":1,"begin":490,"end":514},{"source":1,"begin":508,"end":513}]}}
		AnnotationCmd:105 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":444,"bytecodeCount":9,"sources":[{"source":1,"begin":334,"end":411},{"source":1,"begin":371,"end":378},{"source":1,"begin":400,"end":405},{"source":1,"begin":389,"end":405}]}}
		AnnotationCmd:105 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":463,"bytecodeCount":5,"sources":[{"source":1,"begin":490,"end":514},{"source":1,"begin":483,"end":488},{"source":1,"begin":480,"end":515},{"source":1,"begin":470,"end":533}]}}
		AnnotationCmd:105 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":474,"bytecodeCount":3,"sources":[{"source":1,"begin":470,"end":533},{"source":1,"begin":417,"end":539}]}}
		AnnotationCmd:105 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":492,"bytecodeCount":6,"sources":[{"source":1,"begin":645,"end":678},{"source":1,"begin":545,"end":684}]}}
		AnnotationCmd:105 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":534,"bytecodeCount":9,"sources":[{"source":1,"begin":949,"end":1002},{"source":1,"begin":939,"end":1002},{"source":1,"begin":895,"end":1012},{"source":1,"begin":690,"end":1019}]}}
		AnnotationCmd:105 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":80,"bytecodeCount":3,"sources":[{"source":0,"begin":235,"end":310}]}}
		AnnotationCmd:123 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":115,"bytecodeCount":37,"sources":[{"source":0,"begin":235,"end":310},{"source":0,"begin":282,"end":286},{"source":0,"begin":282,"end":294},{"source":0,"begin":295,"end":296},{"source":0,"begin":298,"end":299},{"source":0,"begin":298,"end":302},{"source":0,"begin":300,"end":301},{"source":0,"begin":282,"end":303}]}}
		AssignExpCmd:124 R44:28 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(skey_basic:bif 0x0) Apply(skey_basic:bif 0x0))
		AnnotationCmd:105 JSON{"key":{"name":"init.reorder.fence","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AssignExpCmd:125 tacMCANON0!!46:0 Store(tacMCANON0havocme606!!19:72 0x80 0x8c43a44100000000000000000000000000000000000000000000000000000000 )
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1691,"bytecodeCount":14,"sources":[{"source":1,"begin":9444,"end":9859},{"source":1,"begin":9606,"end":9610},{"source":1,"begin":9644,"end":9647},{"source":1,"begin":9633,"end":9642},{"source":1,"begin":9629,"end":9648},{"source":1,"begin":9621,"end":9648},{"source":1,"begin":9658,"end":9729},{"source":1,"begin":9726,"end":9727},{"source":1,"begin":9715,"end":9724},{"source":1,"begin":9711,"end":9728},{"source":1,"begin":9702,"end":9708}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1140,"bytecodeCount":5,"sources":[{"source":1,"begin":5126,"end":5244},{"source":1,"begin":5213,"end":5237},{"source":1,"begin":5231,"end":5236}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":444,"bytecodeCount":9,"sources":[{"source":1,"begin":334,"end":411},{"source":1,"begin":371,"end":378},{"source":1,"begin":400,"end":405},{"source":1,"begin":389,"end":405}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1149,"bytecodeCount":6,"sources":[{"source":1,"begin":5213,"end":5237},{"source":1,"begin":5208,"end":5211},{"source":1,"begin":5201,"end":5238},{"source":1,"begin":5126,"end":5244}]}}
		AssignExpCmd:105 R47:29 tacCalldatabufCANON0@1:127
		AssignExpCmd:125 tacMCANON0!!48:0 Store(tacMCANON0!!46:0 0x84 tacCalldatabufCANON0@1:127 )
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1713,"bytecodeCount":8,"sources":[{"source":1,"begin":9658,"end":9729},{"source":1,"begin":9739,"end":9852},{"source":1,"begin":9848,"end":9850},{"source":1,"begin":9837,"end":9846},{"source":1,"begin":9833,"end":9851},{"source":1,"begin":9824,"end":9830}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1491,"bytecodeCount":15,"sources":[{"source":1,"begin":7670,"end":9438},{"source":1,"begin":7808,"end":7812},{"source":1,"begin":7803,"end":7806},{"source":1,"begin":7799,"end":7813},{"source":1,"begin":7839,"end":7840},{"source":1,"begin":7911,"end":7915},{"source":1,"begin":7904,"end":7909},{"source":1,"begin":7900,"end":7916},{"source":1,"begin":7894,"end":7917},{"source":1,"begin":7881,"end":7917},{"source":1,"begin":7950,"end":8005},{"source":1,"begin":7995,"end":8004}]}}
		AssignExpCmd:128 R50:30 AnnotationExp(Select(CANON47!!7:10 R44:129 ) JSON{"key":{"name":"tac.storage.access-paths","type":"analysis.storage.StorageAnalysisResult$AccessPaths","erasureStrategy":"Canonical"},"value":{"paths":[{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.StructAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.MapAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.Root","slot":"0"},"key":{"#class":"vc.data.TACSymbol.Const","value":"0"},"baseSlot":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R8","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"hashResult":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R44","tag":{"#class":"tac.Tag.UserDefined.UninterpretedSort","name":"skey"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]}},"offset":{"#class":"analysis.storage.StorageAnalysis.Offset.Words","numWords":"0"}}]}})
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R50","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1009}]},"displayPath":{"#class":"analysis.storage.DisplayPath.FieldAccess","field":"x","base":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Const","value":"0"},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"uint256","numBytes":"20","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"m"}}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000001","range":{"specFile":"TestContract.sol","start":{"line":16,"charByteOffset":8},"end":{"line":16,"charByteOffset":29}},"linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":0}}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1178,"bytecodeCount":7,"sources":[{"source":1,"begin":5454,"end":5620},{"source":1,"begin":5523,"end":5528},{"source":1,"begin":5548,"end":5614},{"source":1,"begin":5579,"end":5613},{"source":1,"begin":5602,"end":5612}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1155,"bytecodeCount":11,"sources":[{"source":1,"begin":5250,"end":5352},{"source":1,"begin":5292,"end":5300},{"source":1,"begin":5339,"end":5344},{"source":1,"begin":5336,"end":5337},{"source":1,"begin":5332,"end":5345},{"source":1,"begin":5311,"end":5345}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1192,"bytecodeCount":3,"sources":[{"source":1,"begin":5579,"end":5613},{"source":1,"begin":5548,"end":5614}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1168,"bytecodeCount":9,"sources":[{"source":1,"begin":5358,"end":5448},{"source":1,"begin":5408,"end":5415},{"source":1,"begin":5437,"end":5442},{"source":1,"begin":5426,"end":5442}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1197,"bytecodeCount":7,"sources":[{"source":1,"begin":5548,"end":5614},{"source":1,"begin":5539,"end":5614},{"source":1,"begin":5454,"end":5620}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1512,"bytecodeCount":8,"sources":[{"source":1,"begin":7950,"end":8005},{"source":1,"begin":8018,"end":8081},{"source":1,"begin":8075,"end":8079},{"source":1,"begin":8070,"end":8073},{"source":1,"begin":8066,"end":8080},{"source":1,"begin":8052,"end":8064}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1204,"bytecodeCount":5,"sources":[{"source":1,"begin":5626,"end":5734},{"source":1,"begin":5703,"end":5727},{"source":1,"begin":5721,"end":5726}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":444,"bytecodeCount":9,"sources":[{"source":1,"begin":334,"end":411},{"source":1,"begin":371,"end":378},{"source":1,"begin":400,"end":405},{"source":1,"begin":389,"end":405}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1213,"bytecodeCount":6,"sources":[{"source":1,"begin":5703,"end":5727},{"source":1,"begin":5698,"end":5701},{"source":1,"begin":5691,"end":5728},{"source":1,"begin":5626,"end":5734}]}}
		AssignExpCmd:125 tacMCANON0!!52:0 Store(tacMCANON0!!48:0 0xa4 R50:30 )
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1525,"bytecodeCount":12,"sources":[{"source":1,"begin":8018,"end":8081},{"source":1,"begin":7850,"end":8091},{"source":1,"begin":8162,"end":8166},{"source":1,"begin":8155,"end":8160},{"source":1,"begin":8151,"end":8167},{"source":1,"begin":8145,"end":8168},{"source":1,"begin":8132,"end":8168},{"source":1,"begin":8201,"end":8256},{"source":1,"begin":8246,"end":8255}]}}
		AssignExpCmd:125 R53:30 Apply(skey_add:bif R44:28 0x1)
		AssignExpCmd:130 R54:30 AnnotationExp(Select(CANON50!!9:11 R53:131 ) JSON{"key":{"name":"tac.storage.access-paths","type":"analysis.storage.StorageAnalysisResult$AccessPaths","erasureStrategy":"Canonical"},"value":{"paths":[{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.StructAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.MapAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.Root","slot":"0"},"key":{"#class":"vc.data.TACSymbol.Const","value":"0"},"baseSlot":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R8","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"hashResult":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R44","tag":{"#class":"tac.Tag.UserDefined.UninterpretedSort","name":"skey"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]}},"offset":{"#class":"analysis.storage.StorageAnalysis.Offset.Bytes","numBytes":"20"}}]}})
		AssumeExpCmd Le(R54:30 0xffffffffffffffffffffffffffffffffffffffff )
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R54","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1009}]},"displayPath":{"#class":"analysis.storage.DisplayPath.FieldAccess","field":"y","base":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Const","value":"0"},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"uint256","numBytes":"20","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"m"}}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"},"contractInstance":"ce4604a0000000000000000000000001","range":{"specFile":"TestContract.sol","start":{"line":16,"charByteOffset":8},"end":{"line":16,"charByteOffset":29}},"linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":1}}}
		AssignExpCmd:130 R55:30 AnnotationExp(Select(CANON51!!10:16 R53:132 ) JSON{"key":{"name":"tac.storage.access-paths","type":"analysis.storage.StorageAnalysisResult$AccessPaths","erasureStrategy":"Canonical"},"value":{"paths":[{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.StructAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.MapAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.Root","slot":"0"},"key":{"#class":"vc.data.TACSymbol.Const","value":"0"},"baseSlot":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R8","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"hashResult":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R44","tag":{"#class":"tac.Tag.UserDefined.UninterpretedSort","name":"skey"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]}},"offset":{"#class":"analysis.storage.StorageAnalysis.Offset.Bytes","numBytes":"34"}}]}})
		AssumeExpCmd Le(R55:30 0xff )
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R55","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1009}]},"displayPath":{"#class":"analysis.storage.DisplayPath.FieldAccess","field":"z1","base":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Const","value":"0"},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"uint256","numBytes":"20","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"m"}}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8},"contractInstance":"ce4604a0000000000000000000000001","range":{"specFile":"TestContract.sol","start":{"line":16,"charByteOffset":8},"end":{"line":16,"charByteOffset":29}},"linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":1}}}
		AssignExpCmd:130 R56:30 AnnotationExp(Select(CANON52!!11:17 R53:133 ) JSON{"key":{"name":"tac.storage.access-paths","type":"analysis.storage.StorageAnalysisResult$AccessPaths","erasureStrategy":"Canonical"},"value":{"paths":[{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.StructAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.MapAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.Root","slot":"0"},"key":{"#class":"vc.data.TACSymbol.Const","value":"0"},"baseSlot":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R8","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"hashResult":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R44","tag":{"#class":"tac.Tag.UserDefined.UninterpretedSort","name":"skey"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]}},"offset":{"#class":"analysis.storage.StorageAnalysis.Offset.Bytes","numBytes":"35"}}]}})
		AssumeExpCmd Le(R56:30 0xff )
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R56","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1009}]},"displayPath":{"#class":"analysis.storage.DisplayPath.FieldAccess","field":"z2","base":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Const","value":"0"},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"uint256","numBytes":"20","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"m"}}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8},"contractInstance":"ce4604a0000000000000000000000001","range":{"specFile":"TestContract.sol","start":{"line":16,"charByteOffset":8},"end":{"line":16,"charByteOffset":29}},"linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":1}}}
		AssignExpCmd:130 R57:30 AnnotationExp(Select(CANON53!!12:18 R53:134 ) JSON{"key":{"name":"tac.storage.access-paths","type":"analysis.storage.StorageAnalysisResult$AccessPaths","erasureStrategy":"Canonical"},"value":{"paths":[{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.StructAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.MapAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.Root","slot":"0"},"key":{"#class":"vc.data.TACSymbol.Const","value":"0"},"baseSlot":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R8","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"hashResult":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R44","tag":{"#class":"tac.Tag.UserDefined.UninterpretedSort","name":"skey"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]}},"offset":{"#class":"analysis.storage.StorageAnalysis.Offset.Bytes","numBytes":"36"}}]}})
		AssumeExpCmd Le(R57:30 0xff )
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R57","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1009}]},"displayPath":{"#class":"analysis.storage.DisplayPath.FieldAccess","field":"b1","base":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Const","value":"0"},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"uint256","numBytes":"20","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"m"}}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"},"contractInstance":"ce4604a0000000000000000000000001","range":{"specFile":"TestContract.sol","start":{"line":16,"charByteOffset":8},"end":{"line":16,"charByteOffset":29}},"linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":1}}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1251,"bytecodeCount":7,"sources":[{"source":1,"begin":5885,"end":6051},{"source":1,"begin":5954,"end":5959},{"source":1,"begin":5979,"end":6045},{"source":1,"begin":6010,"end":6044},{"source":1,"begin":6033,"end":6043}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1155,"bytecodeCount":11,"sources":[{"source":1,"begin":5250,"end":5352},{"source":1,"begin":5292,"end":5300},{"source":1,"begin":5339,"end":5344},{"source":1,"begin":5336,"end":5337},{"source":1,"begin":5332,"end":5345},{"source":1,"begin":5311,"end":5345}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1265,"bytecodeCount":3,"sources":[{"source":1,"begin":6010,"end":6044},{"source":1,"begin":5979,"end":6045}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1219,"bytecodeCount":11,"sources":[{"source":1,"begin":5740,"end":5879},{"source":1,"begin":5790,"end":5797},{"source":1,"begin":5830,"end":5872},{"source":1,"begin":5823,"end":5828},{"source":1,"begin":5819,"end":5873},{"source":1,"begin":5808,"end":5873}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1270,"bytecodeCount":7,"sources":[{"source":1,"begin":5979,"end":6045},{"source":1,"begin":5970,"end":6045},{"source":1,"begin":5885,"end":6051}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1542,"bytecodeCount":8,"sources":[{"source":1,"begin":8201,"end":8256},{"source":1,"begin":8269,"end":8332},{"source":1,"begin":8326,"end":8330},{"source":1,"begin":8321,"end":8324},{"source":1,"begin":8317,"end":8331},{"source":1,"begin":8303,"end":8315}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1277,"bytecodeCount":5,"sources":[{"source":1,"begin":6057,"end":6165},{"source":1,"begin":6134,"end":6158},{"source":1,"begin":6152,"end":6157}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":720,"bytecodeCount":6,"sources":[{"source":1,"begin":2119,"end":2215},{"source":1,"begin":2156,"end":2163},{"source":1,"begin":2185,"end":2209},{"source":1,"begin":2203,"end":2208}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":688,"bytecodeCount":11,"sources":[{"source":1,"begin":1987,"end":2113},{"source":1,"begin":2024,"end":2031},{"source":1,"begin":2064,"end":2106},{"source":1,"begin":2057,"end":2062},{"source":1,"begin":2053,"end":2107},{"source":1,"begin":2042,"end":2107}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":731,"bytecodeCount":7,"sources":[{"source":1,"begin":2185,"end":2209},{"source":1,"begin":2174,"end":2209},{"source":1,"begin":2119,"end":2215}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1286,"bytecodeCount":6,"sources":[{"source":1,"begin":6134,"end":6158},{"source":1,"begin":6129,"end":6132},{"source":1,"begin":6122,"end":6159},{"source":1,"begin":6057,"end":6165}]}}
		AssignExpCmd:125 tacMCANON0!!59:0 Store(tacMCANON0!!52:0 0xc4 R54:30 )
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1555,"bytecodeCount":6,"sources":[{"source":1,"begin":8269,"end":8332},{"source":1,"begin":8101,"end":8342},{"source":1,"begin":8405,"end":8459},{"source":1,"begin":8449,"end":8458}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1318,"bytecodeCount":7,"sources":[{"source":1,"begin":6388,"end":6553},{"source":1,"begin":6456,"end":6461},{"source":1,"begin":6481,"end":6547},{"source":1,"begin":6510,"end":6546},{"source":1,"begin":6535,"end":6545}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1292,"bytecodeCount":11,"sources":[{"source":1,"begin":6171,"end":6277},{"source":1,"begin":6215,"end":6223},{"source":1,"begin":6264,"end":6269},{"source":1,"begin":6259,"end":6262},{"source":1,"begin":6255,"end":6270},{"source":1,"begin":6234,"end":6270}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1332,"bytecodeCount":3,"sources":[{"source":1,"begin":6510,"end":6546},{"source":1,"begin":6481,"end":6547}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1305,"bytecodeCount":11,"sources":[{"source":1,"begin":6283,"end":6382},{"source":1,"begin":6331,"end":6338},{"source":1,"begin":6371,"end":6375},{"source":1,"begin":6364,"end":6369},{"source":1,"begin":6360,"end":6376},{"source":1,"begin":6349,"end":6376}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1337,"bytecodeCount":7,"sources":[{"source":1,"begin":6481,"end":6547},{"source":1,"begin":6472,"end":6547},{"source":1,"begin":6388,"end":6553}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1565,"bytecodeCount":8,"sources":[{"source":1,"begin":8405,"end":8459},{"source":1,"begin":8472,"end":8531},{"source":1,"begin":8525,"end":8529},{"source":1,"begin":8520,"end":8523},{"source":1,"begin":8516,"end":8530},{"source":1,"begin":8502,"end":8514}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1344,"bytecodeCount":5,"sources":[{"source":1,"begin":6559,"end":6661},{"source":1,"begin":6632,"end":6654},{"source":1,"begin":6648,"end":6653}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":782,"bytecodeCount":11,"sources":[{"source":1,"begin":2494,"end":2580},{"source":1,"begin":2529,"end":2536},{"source":1,"begin":2569,"end":2573},{"source":1,"begin":2562,"end":2567},{"source":1,"begin":2558,"end":2574},{"source":1,"begin":2547,"end":2574}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1353,"bytecodeCount":6,"sources":[{"source":1,"begin":6632,"end":6654},{"source":1,"begin":6627,"end":6630},{"source":1,"begin":6620,"end":6655},{"source":1,"begin":6559,"end":6661}]}}
		AssignExpCmd:125 tacMCANON0!!61:0 Store(tacMCANON0!!59:0 0xe4 R55:30 )
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1578,"bytecodeCount":6,"sources":[{"source":1,"begin":8472,"end":8531},{"source":1,"begin":8352,"end":8541},{"source":1,"begin":8604,"end":8658},{"source":1,"begin":8648,"end":8657}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1372,"bytecodeCount":7,"sources":[{"source":1,"begin":6779,"end":6944},{"source":1,"begin":6847,"end":6852},{"source":1,"begin":6872,"end":6938},{"source":1,"begin":6901,"end":6937},{"source":1,"begin":6926,"end":6936}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1359,"bytecodeCount":11,"sources":[{"source":1,"begin":6667,"end":6773},{"source":1,"begin":6711,"end":6719},{"source":1,"begin":6760,"end":6765},{"source":1,"begin":6755,"end":6758},{"source":1,"begin":6751,"end":6766},{"source":1,"begin":6730,"end":6766}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1386,"bytecodeCount":3,"sources":[{"source":1,"begin":6901,"end":6937},{"source":1,"begin":6872,"end":6938}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1305,"bytecodeCount":11,"sources":[{"source":1,"begin":6283,"end":6382},{"source":1,"begin":6331,"end":6338},{"source":1,"begin":6371,"end":6375},{"source":1,"begin":6364,"end":6369},{"source":1,"begin":6360,"end":6376},{"source":1,"begin":6349,"end":6376}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1391,"bytecodeCount":7,"sources":[{"source":1,"begin":6872,"end":6938},{"source":1,"begin":6863,"end":6938},{"source":1,"begin":6779,"end":6944}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1588,"bytecodeCount":8,"sources":[{"source":1,"begin":8604,"end":8658},{"source":1,"begin":8671,"end":8730},{"source":1,"begin":8724,"end":8728},{"source":1,"begin":8719,"end":8722},{"source":1,"begin":8715,"end":8729},{"source":1,"begin":8701,"end":8713}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1344,"bytecodeCount":5,"sources":[{"source":1,"begin":6559,"end":6661},{"source":1,"begin":6632,"end":6654},{"source":1,"begin":6648,"end":6653}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":782,"bytecodeCount":11,"sources":[{"source":1,"begin":2494,"end":2580},{"source":1,"begin":2529,"end":2536},{"source":1,"begin":2569,"end":2573},{"source":1,"begin":2562,"end":2567},{"source":1,"begin":2558,"end":2574},{"source":1,"begin":2547,"end":2574}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1353,"bytecodeCount":6,"sources":[{"source":1,"begin":6632,"end":6654},{"source":1,"begin":6627,"end":6630},{"source":1,"begin":6620,"end":6655},{"source":1,"begin":6559,"end":6661}]}}
		AssignExpCmd:125 tacMCANON0!!63:0 Store(tacMCANON0!!61:0 0x104 R56:30 )
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1601,"bytecodeCount":6,"sources":[{"source":1,"begin":8671,"end":8730},{"source":1,"begin":8551,"end":8740},{"source":1,"begin":8803,"end":8856},{"source":1,"begin":8846,"end":8855}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1424,"bytecodeCount":7,"sources":[{"source":1,"begin":7166,"end":7329},{"source":1,"begin":7233,"end":7238},{"source":1,"begin":7258,"end":7323},{"source":1,"begin":7286,"end":7322},{"source":1,"begin":7311,"end":7321}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1398,"bytecodeCount":11,"sources":[{"source":1,"begin":6950,"end":7056},{"source":1,"begin":6994,"end":7002},{"source":1,"begin":7043,"end":7048},{"source":1,"begin":7038,"end":7041},{"source":1,"begin":7034,"end":7049},{"source":1,"begin":7013,"end":7049}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1438,"bytecodeCount":3,"sources":[{"source":1,"begin":7286,"end":7322},{"source":1,"begin":7258,"end":7323}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1411,"bytecodeCount":11,"sources":[{"source":1,"begin":7062,"end":7160},{"source":1,"begin":7109,"end":7116},{"source":1,"begin":7149,"end":7153},{"source":1,"begin":7142,"end":7147},{"source":1,"begin":7138,"end":7154},{"source":1,"begin":7127,"end":7154}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1443,"bytecodeCount":7,"sources":[{"source":1,"begin":7258,"end":7323},{"source":1,"begin":7249,"end":7323},{"source":1,"begin":7166,"end":7329}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1611,"bytecodeCount":8,"sources":[{"source":1,"begin":8803,"end":8856},{"source":1,"begin":8869,"end":8926},{"source":1,"begin":8920,"end":8924},{"source":1,"begin":8915,"end":8918},{"source":1,"begin":8911,"end":8925},{"source":1,"begin":8897,"end":8909}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1450,"bytecodeCount":5,"sources":[{"source":1,"begin":7335,"end":7434},{"source":1,"begin":7406,"end":7427},{"source":1,"begin":7421,"end":7426}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":839,"bytecodeCount":11,"sources":[{"source":1,"begin":2851,"end":2941},{"source":1,"begin":2885,"end":2892},{"source":1,"begin":2928,"end":2933},{"source":1,"begin":2921,"end":2934},{"source":1,"begin":2914,"end":2935},{"source":1,"begin":2903,"end":2935}]}}
		AssignExpCmd:105 R65:22 Ite(Eq(R57:30 0x0 ) 0x0 0x1 )
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1459,"bytecodeCount":6,"sources":[{"source":1,"begin":7406,"end":7427},{"source":1,"begin":7401,"end":7404},{"source":1,"begin":7394,"end":7428},{"source":1,"begin":7335,"end":7434}]}}
		AssignExpCmd:125 tacMCANON0!!67:0 Store(tacMCANON0!!63:0 0x124 R65:22 )
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1624,"bytecodeCount":12,"sources":[{"source":1,"begin":8869,"end":8926},{"source":1,"begin":8750,"end":8936},{"source":1,"begin":9008,"end":9012},{"source":1,"begin":9001,"end":9006},{"source":1,"begin":8997,"end":9013},{"source":1,"begin":8991,"end":9014},{"source":1,"begin":8978,"end":9014},{"source":1,"begin":9047,"end":9102},{"source":1,"begin":9092,"end":9101}]}}
		AssignExpCmd:105 R68:30 Apply(skey_add:bif R53:30 0x1)
		AssignExpCmd:135 R69:30 AnnotationExp(Select(CANON58!!13:19 R68:136 ) JSON{"key":{"name":"tac.storage.access-paths","type":"analysis.storage.StorageAnalysisResult$AccessPaths","erasureStrategy":"Canonical"},"value":{"paths":[{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.StructAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.MapAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.Root","slot":"0"},"key":{"#class":"vc.data.TACSymbol.Const","value":"0"},"baseSlot":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R8","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"hashResult":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R44","tag":{"#class":"tac.Tag.UserDefined.UninterpretedSort","name":"skey"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]}},"offset":{"#class":"analysis.storage.StorageAnalysis.Offset.Words","numWords":"2"}}]}})
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R69","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1009}]},"displayPath":{"#class":"analysis.storage.DisplayPath.FieldAccess","field":"x2","base":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Const","value":"0"},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"uint256","numBytes":"20","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"m"}}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000001","range":{"specFile":"TestContract.sol","start":{"line":16,"charByteOffset":8},"end":{"line":16,"charByteOffset":29}},"linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":2}}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1178,"bytecodeCount":7,"sources":[{"source":1,"begin":5454,"end":5620},{"source":1,"begin":5523,"end":5528},{"source":1,"begin":5548,"end":5614},{"source":1,"begin":5579,"end":5613},{"source":1,"begin":5602,"end":5612}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1155,"bytecodeCount":11,"sources":[{"source":1,"begin":5250,"end":5352},{"source":1,"begin":5292,"end":5300},{"source":1,"begin":5339,"end":5344},{"source":1,"begin":5336,"end":5337},{"source":1,"begin":5332,"end":5345},{"source":1,"begin":5311,"end":5345}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1192,"bytecodeCount":3,"sources":[{"source":1,"begin":5579,"end":5613},{"source":1,"begin":5548,"end":5614}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1168,"bytecodeCount":9,"sources":[{"source":1,"begin":5358,"end":5448},{"source":1,"begin":5408,"end":5415},{"source":1,"begin":5437,"end":5442},{"source":1,"begin":5426,"end":5442}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1197,"bytecodeCount":7,"sources":[{"source":1,"begin":5548,"end":5614},{"source":1,"begin":5539,"end":5614},{"source":1,"begin":5454,"end":5620}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1641,"bytecodeCount":8,"sources":[{"source":1,"begin":9047,"end":9102},{"source":1,"begin":9115,"end":9178},{"source":1,"begin":9172,"end":9176},{"source":1,"begin":9167,"end":9170},{"source":1,"begin":9163,"end":9177},{"source":1,"begin":9149,"end":9161}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1204,"bytecodeCount":5,"sources":[{"source":1,"begin":5626,"end":5734},{"source":1,"begin":5703,"end":5727},{"source":1,"begin":5721,"end":5726}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":444,"bytecodeCount":9,"sources":[{"source":1,"begin":334,"end":411},{"source":1,"begin":371,"end":378},{"source":1,"begin":400,"end":405},{"source":1,"begin":389,"end":405}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1213,"bytecodeCount":6,"sources":[{"source":1,"begin":5703,"end":5727},{"source":1,"begin":5698,"end":5701},{"source":1,"begin":5691,"end":5728},{"source":1,"begin":5626,"end":5734}]}}
		AssignExpCmd:125 tacMCANON0!!71:0 Store(tacMCANON0!!67:0 0x144 R69:30 )
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1654,"bytecodeCount":12,"sources":[{"source":1,"begin":9115,"end":9178},{"source":1,"begin":8946,"end":9188},{"source":1,"begin":9260,"end":9264},{"source":1,"begin":9253,"end":9258},{"source":1,"begin":9249,"end":9265},{"source":1,"begin":9243,"end":9266},{"source":1,"begin":9230,"end":9266},{"source":1,"begin":9299,"end":9351},{"source":1,"begin":9341,"end":9350}]}}
		AssignExpCmd:105 R72:30 Apply(skey_add:bif R68:30 0x1)
		AssignExpCmd:137 R73:30 AnnotationExp(Select(CANON60!!14:45 R72:138 ) JSON{"key":{"name":"tac.storage.access-paths","type":"analysis.storage.StorageAnalysisResult$AccessPaths","erasureStrategy":"Canonical"},"value":{"paths":[{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.StructAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.MapAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.Root","slot":"0"},"key":{"#class":"vc.data.TACSymbol.Const","value":"0"},"baseSlot":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R8","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"hashResult":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R44","tag":{"#class":"tac.Tag.UserDefined.UninterpretedSort","name":"skey"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1018}]}},"offset":{"#class":"analysis.storage.StorageAnalysis.Offset.Bytes","numBytes":"60"}}]}})
		AssumeExpCmd Le(R73:30 0xff )
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R73","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1009}]},"displayPath":{"#class":"analysis.storage.DisplayPath.FieldAccess","field":"b2","base":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Const","value":"0"},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"uint256","numBytes":"20","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"m"}}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"},"contractInstance":"ce4604a0000000000000000000000001","range":{"specFile":"TestContract.sol","start":{"line":16,"charByteOffset":8},"end":{"line":16,"charByteOffset":29}},"linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.None"}}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1465,"bytecodeCount":7,"sources":[{"source":1,"begin":7440,"end":7600},{"source":1,"begin":7506,"end":7511},{"source":1,"begin":7531,"end":7594},{"source":1,"begin":7559,"end":7593},{"source":1,"begin":7582,"end":7592}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1155,"bytecodeCount":11,"sources":[{"source":1,"begin":5250,"end":5352},{"source":1,"begin":5292,"end":5300},{"source":1,"begin":5339,"end":5344},{"source":1,"begin":5336,"end":5337},{"source":1,"begin":5332,"end":5345},{"source":1,"begin":5311,"end":5345}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1479,"bytecodeCount":3,"sources":[{"source":1,"begin":7559,"end":7593},{"source":1,"begin":7531,"end":7594}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1411,"bytecodeCount":11,"sources":[{"source":1,"begin":7062,"end":7160},{"source":1,"begin":7109,"end":7116},{"source":1,"begin":7149,"end":7153},{"source":1,"begin":7142,"end":7147},{"source":1,"begin":7138,"end":7154},{"source":1,"begin":7127,"end":7154}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1484,"bytecodeCount":7,"sources":[{"source":1,"begin":7531,"end":7594},{"source":1,"begin":7522,"end":7594},{"source":1,"begin":7440,"end":7600}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1671,"bytecodeCount":8,"sources":[{"source":1,"begin":9299,"end":9351},{"source":1,"begin":9364,"end":9421},{"source":1,"begin":9415,"end":9419},{"source":1,"begin":9410,"end":9413},{"source":1,"begin":9406,"end":9420},{"source":1,"begin":9392,"end":9404}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1450,"bytecodeCount":5,"sources":[{"source":1,"begin":7335,"end":7434},{"source":1,"begin":7406,"end":7427},{"source":1,"begin":7421,"end":7426}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":839,"bytecodeCount":11,"sources":[{"source":1,"begin":2851,"end":2941},{"source":1,"begin":2885,"end":2892},{"source":1,"begin":2928,"end":2933},{"source":1,"begin":2921,"end":2934},{"source":1,"begin":2914,"end":2935},{"source":1,"begin":2903,"end":2935}]}}
		AssignExpCmd:105 R75:22 Ite(Eq(R73:30 0x0 ) 0x0 0x1 )
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1459,"bytecodeCount":6,"sources":[{"source":1,"begin":7406,"end":7427},{"source":1,"begin":7401,"end":7404},{"source":1,"begin":7394,"end":7428},{"source":1,"begin":7335,"end":7434}]}}
		AssignExpCmd:125 tacMCANON0!!77:0 Store(tacMCANON0!!71:0 0x164 R75:22 )
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1684,"bytecodeCount":7,"sources":[{"source":1,"begin":9364,"end":9421},{"source":1,"begin":9198,"end":9431},{"source":1,"begin":7777,"end":9438},{"source":1,"begin":7670,"end":9438}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":1726,"bytecodeCount":7,"sources":[{"source":1,"begin":9739,"end":9852},{"source":1,"begin":9444,"end":9859}]}}
		AnnotationCmd:126 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":191,"bytecodeCount":17,"sources":[{"source":0,"begin":282,"end":303}]}}
		AssignExpCmd:125 R78:38 0x80
		AssignExpCmd:125 R79:39 0x104
		AssignExpCmd:125 R80:40 Select(tacExtcodesize!!3:9 Apply(to_skey:bif R18:139) )
		AssumeExpCmd Ge(R80:40 0x1 )
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.RawStorageAccess.WithLocSym","isLoad":true,"loc":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R18","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.contract.sym.addr.name","type":"java.lang.String","erasureStrategy":"Erased"},"value":"TestContract"},{"key":{"name":"tac.contract.sym.addr","type":"java.math.BigInteger","erasureStrategy":"Erased"},"value":"ce4604a0000000000000000000000001"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1021}]},"contractInstance":"ce4604a0000000000000000000000001","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R80","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1012}]},"storageType":null,"range":{"specFile":"TestContract.sol","start":{"line":16,"charByteOffset":8},"end":{"line":16,"charByteOffset":29}}}}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.StartBranchSnippet","branchIndex":2,"branchSource":{"range":{"specFile":"TestContract.sol","start":{"line":16,"charByteOffset":8},"end":{"line":16,"charByteOffset":29}},"content":"this.workOnS(x, m[0])"}}}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.EndBranchSnippet","branchIndex":2}}
		AnnotationCmd:125 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":217,"bytecodeCount":9,"sources":[{"source":0,"begin":282,"end":303}]}}
		AssignHavocCmd:125 R81:40
		AnnotationCmd:125 JSON{"key":{"name":"tac.decompiler.call-start","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AssignHavocCmd:125 tacReturndata!!82:1
		JumpCmd 2_0_0_2_0_1
	}
	Block 2_0_0_2_0_1 Succ [3_0_0_1_0_0] {
		AnnotationCmd JSON{"key":{"name":"call.trace.external.summary.start","type":"analysis.icfg.SummaryStack$SummaryStart$External","erasureStrategy":"CallTrace"},"value":"rO0ABXNyADBhbmFseXNpcy5pY2ZnLlN1bW1hcnlTdGFjayRTdW1tYXJ5U3RhcnQkRXh0ZXJuYWyjNkk2r+9AZAIABUwADmFwcGxpZWRTdW1tYXJ5dAAsTGFuYWx5c2lzL2ljZmcvU3VtbWFyaXphdGlvbiRBcHBsaWVkU3VtbWFyeTtMAAhjYWxsTm9kZXQAFUx2Yy9kYXRhL0NhbGxTdW1tYXJ5O0wAF2NhbGxSZXNvbHV0aW9uVGFibGVJbmZvdAA2THJlcG9ydC9jYWxscmVzb2x1dGlvbi9DYWxsUmVzb2x1dGlvblRhYmxlU3VtbWFyeUluZm87TAALY2FsbFNpdGVTcmN0ABVMdmMvZGF0YS9UQUNNZXRhSW5mbztMAAdzdXBwb3J0dAAPTGphdmEvdXRpbC9TZXQ7eHIAJ2FuYWx5c2lzLmljZmcuU3VtbWFyeVN0YWNrJFN1bW1hcnlTdGFydM6P29O9R0c9AgAAeHBzcgA3YW5hbHlzaXMuaWNmZy5TdW1tYXJpemF0aW9uJEFwcGxpZWRTdW1tYXJ5JE1ldGhvZHNCbG9ja8QZaUG9nkK8AgACTAAMc3BlY0NhbGxTdW1tdAAuTHNwZWMvY3ZsYXN0L1NwZWNDYWxsU3VtbWFyeSRFeHByZXNzaWJsZUluQ1ZMO0wAEHN1bW1hcml6ZWRNZXRob2R0ABtMc3BlYy9DVkwkU3VtbWFyeVNpZ25hdHVyZTt4cHNyAB9zcGVjLmN2bGFzdC5TcGVjQ2FsbFN1bW1hcnkkRXhwiLXACP96VR8CAAdMAANleHB0ABRMc3BlYy9jdmxhc3QvQ1ZMRXhwO0wADGV4cGVjdGVkVHlwZXQAEExqYXZhL3V0aWwvTGlzdDtMAAlmdW5QYXJhbXNxAH4ADkwABXJhbmdldAANTHV0aWxzL1JhbmdlO0wABXNjb3BldAAWTHNwZWMvY3ZsYXN0L0NWTFNjb3BlO0wAEXN1bW1hcml6YXRpb25Nb2RldAAvTHNwZWMvY3ZsYXN0L1NwZWNDYWxsU3VtbWFyeSRTdW1tYXJpemF0aW9uTW9kZTtMAAp3aXRoQ2xhdXNldAAsTHNwZWMvY3ZsYXN0L1NwZWNDYWxsU3VtbWFyeSRFeHAkV2l0aENsYXVzZTt4cgAsc3BlYy5jdmxhc3QuU3BlY0NhbGxTdW1tYXJ5JEV4cHJlc3NpYmxlSW5DVkw5jBEFxNlONwIAAHhyABtzcGVjLmN2bGFzdC5TcGVjQ2FsbFN1bW1hcnmf4QieXcWlAQIAAHhwc3IAJ3NwZWMuY3ZsYXN0LkNWTEV4cCRBcHBseUV4cCRDVkxGdW5jdGlvbghf8sf20DA6AgAFWgAIbm9SZXZlcnRMAARhcmdzcQB+AA5MAAJpZHQAEkxqYXZhL2xhbmcvU3RyaW5nO0wAF21ldGhvZElkV2l0aENhbGxDb250ZXh0dAAdTHNwZWMvY3ZsYXN0L1NwZWNEZWNsYXJhdGlvbjtMAAN0YWd0ABdMc3BlYy9jdmxhc3QvQ1ZMRXhwVGFnO3hyABtzcGVjLmN2bGFzdC5DVkxFeHAkQXBwbHlFeHAF3JlNR+1SuwIAAHhyACFzcGVjLmN2bGFzdC5DVkxFeHAkQXBwbGljYXRpb25FeHAEe7zFegP5fQIAAHhyABJzcGVjLmN2bGFzdC5DVkxFeHAB+J/cNeGTiAIAAHhwAXNyABNqYXZhLnV0aWwuQXJyYXlMaXN0eIHSHZnHYZ0DAAFJAARzaXpleHAAAAACdwQAAAACc3IAHnNwZWMuY3ZsYXN0LkNWTEV4cCRWYXJpYWJsZUV4cJ0ULkp52IKNAgAETAACaWRxAH4AF0wADG9yaWdpbmFsTmFtZXEAfgAXTAADdGFncQB+ABlMAA10d29TdGF0ZUluZGV4dAAbTHNwZWMvY3ZsYXN0L1R3b1N0YXRlSW5kZXg7eHEAfgAcdAABeHEAfgAjc3IAFXNwZWMuY3ZsYXN0LkNWTEV4cFRhZ9WLKphaC/tTAgAFWgAJaGFzUGFyZW5zTAAKYW5ub3RhdGlvbnQAIkxzcGVjL2N2bGFzdC9FeHByZXNzaW9uQW5ub3RhdGlvbjtMAAVyYW5nZXEAfgAPTAAFc2NvcGVxAH4AEEwABHR5cGV0ABVMc3BlYy9jdmxhc3QvQ1ZMVHlwZTt4cABwc3IAEXV0aWxzLlJhbmdlJFJhbmdlelevcoxEsQYCAANMAANlbmR0ABZMdXRpbHMvU291cmNlUG9zaXRpb247TAAIc3BlY0ZpbGVxAH4AF0wABXN0YXJ0cQB+ACl4cgALdXRpbHMuUmFuZ2XoA/TylWV/VwIAAHhwc3IAFHV0aWxzLlNvdXJjZVBvc2l0aW9ulfTn1OqZxI0CAAJJAA5jaGFyQnl0ZU9mZnNldEkABGxpbmV4cAAAAEwAAAADdAAJdGVzdC5zcGVjc3EAfgAsAAAASwAAAANzcgAUc3BlYy5jdmxhc3QuQ1ZMU2NvcGUiyWBY1B1dVAIAA0wAFmhhc2hDb2RlQ2FjaGUkZGVsZWdhdGV0AA1Ma290bGluL0xhenk7TAAKaW5uZXJTY29wZXEAfgAQTAAKc2NvcGVTdGFja3EAfgAOeHBzcgAaa290bGluLkluaXRpYWxpemVkTGF6eUltcGx7x3/xICqBjQIAAUwABXZhbHVldAASTGphdmEvbGFuZy9PYmplY3Q7eHBzcgARamF2YS5sYW5nLkludGVnZXIS4qCk94GHOAIAAUkABXZhbHVleHIAEGphdmEubGFuZy5OdW1iZXKGrJUdC5TgiwIAAHhwzPGoX3NxAH4AMHNxAH4AM3NxAH4ANk5njWFzcQB+ADBzcQB+ADNzcQB+ADYAAAAfcHNyABxrb3RsaW4uY29sbGVjdGlvbnMuRW1wdHlMaXN0mW/H0KfgYDICAAB4cHNyACNqYXZhLnV0aWwuQ29sbGVjdGlvbnMkU2luZ2xldG9uTGlzdCrvKRA8p5uXAgABTAAHZWxlbWVudHEAfgA0eHBzcgAmc3BlYy5jdmxhc3QuQ1ZMU2NvcGUkSXRlbSRBc3RTY29wZUl0ZW2Hm6f3BtWhkwIAAHhyABlzcGVjLmN2bGFzdC5DVkxTY29wZSRJdGVtLwOv/543VkUCAAB4cHNxAH4AHgAAAAJ3BAAAAAJxAH4ARXNyACtzcGVjLmN2bGFzdC5DVkxTY29wZSRJdGVtJEV4cHJlc3Npb25TdW1tYXJ5DzManVpfqWgCAAFJAAdzY29wZUlkeHIAKXNwZWMuY3ZsYXN0LkNWTFNjb3BlJEl0ZW0kQVNURWxlbWVudFNjb3BlUquPEVHkIpYCAAFMAAdlbGVtZW50dAAaTHNwZWMvY3ZsYXN0L0NyZWF0ZXNTY29wZTt4cQB+AERzcQB+AAxzcgAlc3BlYy5jdmxhc3QuQ1ZMRXhwJFVucmVzb2x2ZWRBcHBseUV4cDU+F4IbuX3IAgAIWgAMaW52b2tlSXNTYWZlWgANaW52b2tlSXNXaG9sZUwABGFyZ3NxAH4ADkwABGJhc2VxAH4ADUwADWludm9rZVN0b3JhZ2V0ACBMc3BlYy9jdmxhc3QvQ1ZMRXhwJFZhcmlhYmxlRXhwO0wACG1ldGhvZElkcQB+ABdMAAN0YWdxAH4AGUwADXR3b1N0YXRlSW5kZXhxAH4AIXhxAH4AGwEAc3EAfgAeAAAAAncEAAAAAnNxAH4AIHEAfgAjcQB+ACNzcQB+ACQAcHEAfgArcQB+ADJwfnIAGXNwZWMuY3ZsYXN0LlR3b1N0YXRlSW5kZXgAAAAAAAAAABIAAHhyAA5qYXZhLmxhbmcuRW51bQAAAAAAAAAAEgAAeHB0AAdORUlUSEVSc3EAfgAgdAABc3EAfgBXc3EAfgAkAHBzcQB+AChzcQB+ACwAAABPAAAAA3EAfgAuc3EAfgAsAAAATgAAAANxAH4AMnBxAH4AVHhwc3EAfgAgdAALbGFzdFN0b3JhZ2VxAH4AXXNxAH4AJABwc3IAEXV0aWxzLlJhbmdlJEVtcHR5xIMekl54ldcCAAFMAAdjb21tZW50cQB+ABd4cQB+ACp0ABJlbXB0eSBzdG9yYWdlIHR5cGVxAH4AMnBxAH4AVHQACndvcmtPblNDVkxzcQB+ACQAcHNxAH4AKHNxAH4ALAAAAFAAAAADcQB+AC5zcQB+ACwAAABAAAAAA3EAfgAycHEAfgBUcHNxAH4AHgAAAAJ3BAAAAAJzcgAZc3BlYy5jdmxhc3QuVk1QYXJhbSROYW1lZABd7PCOutCNAgAETAAEbmFtZXEAfgAXTAAMb3JpZ2luYWxOYW1lcQB+ABdMAAVyYW5nZXEAfgAPTAAGdm1UeXBldAAuTHNwZWMvY3ZsYXN0L3R5cGVkZXNjcmlwdG9ycy9WTVR5cGVEZXNjcmlwdG9yO3hyABNzcGVjLmN2bGFzdC5WTVBhcmFtoDmogPswXr8CAAB4cHEAfgAjcQB+ACNzcQB+AChzcQB+ACwAAAAbAAAAA3EAfgAuc3EAfgAsAAAAFQAAAANzcgAzc3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yJFVJbnRLqHosSzB6DiUCAAFJAAhiaXR3aWR0aHhyAERzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkRVZNSXNvbW9ycGhpY1ZhbHVlVHlwZZbjlXdq3fF/AgAAeHIAOnNwZWMuY3ZsYXN0LnR5cGVkZXNjcmlwdG9ycy5FVk1UeXBlRGVzY3JpcHRvciRFVk1WYWx1ZVR5cGUQ5NL1qK834QIAAHhyAC1zcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3JeVh3cxo4+6AIAAHhwAAABAHNxAH4AaHEAfgBXcQB+AFdzcQB+AChzcQB+ACwAAAAyAAAAA3EAfgAuc3EAfgAsAAAAHQAAAANzcgBBc3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yJEVWTVN0cnVjdERlc2NyaXB0b3KmDdePEwDhSgIABEwAC2Nhbm9uaWNhbElkcQB+ABdMAAZmaWVsZHNxAH4ADkwACGxvY2F0aW9udAAyTHNwZWMvY3ZsYXN0L3R5cGVkZXNjcmlwdG9ycy9FVk1Mb2NhdGlvblNwZWNpZmllcjtMAARuYW1lcQB+ABd4cQB+AHJ0ACRUZXN0Q29udHJhY3Quc29sfFRlc3RDb250cmFjdC5TaW1wbGVzcQB+AB4AAAAHdwQAAAAHc3IAUHNwZWMuY3ZsYXN0LnR5cGVkZXNjcmlwdG9ycy5FVk1UeXBlRGVzY3JpcHRvciRFVk1TdHJ1Y3REZXNjcmlwdG9yJEVWTVN0cnVjdEVudHJ5H13fBPhr4ZsCAAJMAAlmaWVsZE5hbWVxAH4AF0wACWZpZWxkVHlwZXQAL0xzcGVjL2N2bGFzdC90eXBlZGVzY3JpcHRvcnMvRVZNVHlwZURlc2NyaXB0b3I7eHBxAH4AI3NxAH4AbwAAAQBzcQB+AH10AAF5c3IANXNwZWMuY3ZsYXN0LnR5cGVkZXNjcmlwdG9ycy5FVk1UeXBlRGVzY3JpcHRvciRhZGRyZXNzxLEwUfZ5aggCAAB4cQB+AHBzcQB+AH10AAJ6MXNxAH4AbwAAAAhzcQB+AH10AAJ6MnNxAH4AbwAAAAhzcQB+AH10AAJiMXNyADJzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkYm9vbAVCsuAjex/JAgAAeHEAfgBwc3EAfgB9dAACeDJzcQB+AG8AAAEAc3EAfgB9dAACYjJxAH4AjnhwdAATVGVzdENvbnRyYWN0LlNpbXBsZXhzcQB+AChzcQB+ACwAAABQAAAAA3EAfgAuc3EAfgAsAAAAQAAAAANxAH4AMn5yAC1zcGVjLmN2bGFzdC5TcGVjQ2FsbFN1bW1hcnkkU3VtbWFyaXphdGlvbk1vZGUAAAAAAAAAABIAAHhxAH4AU3QAA0FMTHAAAAAAeHNyABZzcGVjLmN2bGFzdC5DVkxUeXBlJFZNo6s7LR18330CAAJMAAdjb250ZXh0dAArTHNwZWMvY3ZsYXN0L3R5cGVkZXNjcmlwdG9ycy9Gcm9tVk1Db250ZXh0O0wACmRlc2NyaXB0b3JxAH4AaXhyABNzcGVjLmN2bGFzdC5DVkxUeXBldDETlbfBZVACAAB4cHNyAENzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRnJvbVZNQ29udGV4dCRFeHRlcm5hbFN1bW1hcnlBcmdCaW5kaW5nwnRM6fhMP3sCAAB4cgApc3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkZyb21WTUNvbnRleHTF2vGG93fwZQIAAHhwcQB+AHNxAH4AVHNxAH4AIHEAfgBXcQB+AFdzcQB+ACQAcHEAfgBZcQB+ADJzcQB+AJtxAH4AoXEAfgB6cQB+AFR4cQB+AGJzcgAbc3BlYy5jdmxhc3QuU3BlY0RlY2xhcmF0aW9ujRb0DzyoobcCAAFMAAhtZXRob2RJZHEAfgAXeHBxAH4AYnNxAH4AJABzcgAXc3BlYy5jdmxhc3QuQ1ZMRnVuY3Rpb24uWdWoiYfIYQIACUwABWJsb2NrcQB+AA5MAA1kZWNsYXJhdGlvbklkcQB+ABdMABJmdW5jdGlvbklkZW50aWZpZXJxAH4AGEwACnBhcmFtVHlwZXNxAH4ADkwABnBhcmFtc3EAfgAOTAAFcmFuZ2VxAH4AD0wABHJldHN0ACFMc3BlYy9jdmxhc3QvQ1ZMVHlwZSRQdXJlQ1ZMVHlwZTtMAAVzY29wZXEAfgAQTAAPdHlwZURlc2NyaXB0aW9ucQB+ABd4cHNxAH4AHgAAAAJ3BAAAAAJzcgAfc3BlYy5jdmxhc3QuQ1ZMQ21kJFNpbXBsZSRIYXZvY0G+wg9MNoBdAgAETAALYXNzdW1pbmdFeHBxAH4ADUwABXJhbmdlcQB+AA9MAAVzY29wZXEAfgAQTAAHdGFyZ2V0c3EAfgAOeHIAGXNwZWMuY3ZsYXN0LkNWTENtZCRTaW1wbGWA/5FLCuaTSAIAAHhyABJzcGVjLmN2bGFzdC5DVkxDbWR9T7T2R5OokgIAAHhwcHNxAH4AKHNxAH4ALAAAAB8AAAAHcQB+AC5zcQB+ACwAAAAEAAAAB3NxAH4AMHNxAH4AM3NxAH4ANszxqLxxAH4AOXNxAH4AHgAAAAJ3BAAAAAJxAH4ARXNyAC5zcGVjLmN2bGFzdC5DVkxTY29wZSRJdGVtJENWTEZ1bmN0aW9uU2NvcGVJdGVte1vIQGGDSjkCAAFJAAdzY29wZUlkeHEAfgBIc3EAfgCoc3EAfgAeAAAAAncEAAAAAnNxAH4ArHBxAH4AsHEAfgCzc3EAfgAeAAAAAXcEAAAAAXNyACFzcGVjLmN2bGFzdC5DVkxFeHAkRmllbGRTZWxlY3RFeHBTO4ABfNpZrgIAA0wACWZpZWxkTmFtZXEAfgAXTAAJc3RydWN0RXhwcQB+AA1MAAN0YWdxAH4AGXhxAH4AHHEAfgCMc3IAIHNwZWMuY3ZsYXN0LkNWTEV4cCRBcnJheURlcmVmRXhw5CTb4GwIYAYCAANMAAVhcnJheXEAfgANTAAFaW5kZXhxAH4ADUwAA3RhZ3EAfgAZeHEAfgAcc3EAfgC9dAABbXNxAH4AIHQADHRlc3RDb250cmFjdHEAfgDEc3EAfgAkAHBzcQB+AChzcQB+ACwAAAAWAAAAB3EAfgAuc3EAfgAsAAAACgAAAAdxAH4As3BxAH4AVHNxAH4AJABwc3EAfgAoc3EAfgAsAAAAGAAAAAdxAH4ALnNxAH4ALAAAAAoAAAAHcQB+ALNwc3IAJXNwZWMuY3ZsYXN0LkNWTEV4cCRDb25zdGFudCROdW1iZXJMaXQAXZb+I542BQIAA0wAAW50ABZMamF2YS9tYXRoL0JpZ0ludGVnZXI7TAAJcHJpbnRIaW50cQB+ABdMAAN0YWdxAH4AGXhyABtzcGVjLmN2bGFzdC5DVkxFeHAkQ29uc3RhbnS7VbSpZ6efmwIAAHhxAH4AHHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cQB+ADf///////////////7////+AAAAAHVyAAJbQqzzF/gGCFTgAgAAeHAAAAAAeHQAAjEwc3EAfgAkAHBzcQB+AChzcQB+ACwAAAAaAAAAB3EAfgAuc3EAfgAsAAAAGQAAAAdxAH4As3BzcQB+ACQAcHNxAH4AKHNxAH4ALAAAABsAAAAHcQB+AC5zcQB+ACwAAAAKAAAAB3EAfgCzcHNxAH4AJABwc3EAfgAoc3EAfgAsAAAAHgAAAAdxAH4ALnNxAH4ALAAAAAoAAAAHcQB+ALNweHNyACpzcGVjLmN2bGFzdC5DVkxDbWQkU2ltcGxlJEFzc3VtZUNtZCRBc3N1bWWYLjUIZbQISgIABVoAEGludmFyaWFudFByZUNvbmRMAAtkZXNjcmlwdGlvbnEAfgAXTAADZXhwcQB+AA1MAAVyYW5nZXEAfgAPTAAFc2NvcGVxAH4AEHhyACNzcGVjLmN2bGFzdC5DVkxDbWQkU2ltcGxlJEFzc3VtZUNtZG9e2sLcjguEAgAAeHEAfgCtAHBzcgAhc3BlYy5jdmxhc3QuQ1ZMRXhwJFJlbG9wRXhwJEVxRXhwSA5Rt59W1MoCAANMAAFscQB+AA1MAAFycQB+AA1MAAN0YWdxAH4AGXhyABtzcGVjLmN2bGFzdC5DVkxFeHAkUmVsb3BFeHDU/s1EWO+7ogIAAHhxAH4AHHNxAH4AvXEAfgCMc3EAfgC/c3EAfgC9cQB+AMJzcQB+ACBxAH4AxHEAfgDEc3EAfgAkAHBzcQB+AChzcQB+ACwAAAAYAAAACHEAfgAuc3EAfgAsAAAADAAAAAhxAH4As3BxAH4AVHNxAH4AJABwc3EAfgAoc3EAfgAsAAAAGgAAAAhxAH4ALnNxAH4ALAAAAAwAAAAIcQB+ALNwc3EAfgDNcQB+ANNxAH4A1nNxAH4AJABwc3EAfgAoc3EAfgAsAAAAHAAAAAhxAH4ALnNxAH4ALAAAABsAAAAIcQB+ALNwc3EAfgAkAHBzcQB+AChzcQB+ACwAAAAdAAAACHEAfgAuc3EAfgAsAAAADAAAAAhxAH4As3BzcQB+ACQAcHNxAH4AKHNxAH4ALAAAACAAAAAIcQB+AC5zcQB+ACwAAAAMAAAACHEAfgCzcHNyAC9zcGVjLmN2bGFzdC5DVkxFeHAkUmVsb3BFeHAkQXJpdGhSZWxvcEV4cCRHdEV4cIpaLJJfNbWrAgADTAABbHEAfgANTAABcnEAfgANTAADdGFncQB+ABl4cgApc3BlYy5jdmxhc3QuQ1ZMRXhwJFJlbG9wRXhwJEFyaXRoUmVsb3BFeHCO6KQpLerLZwIAAHhxAH4A53NxAH4AIHEAfgAjcQB+ACNzcQB+ACQAcHNxAH4AKHNxAH4ALAAAACYAAAAIcQB+AC5zcQB+ACwAAAAlAAAACHEAfgCzcHEAfgBUc3EAfgDNc3EAfgDR///////////////+/////gAAAAF1cQB+ANQAAAABA3hxAH4A1nNxAH4AJABwc3EAfgAoc3EAfgAsAAAAKgAAAAhxAH4ALnNxAH4ALAAAACkAAAAIcQB+ALNwc3EAfgAkAXBzcQB+AChzcQB+ACwAAAAqAAAACHEAfgAuc3EAfgAsAAAAJQAAAAhxAH4As3BzcQB+ACQAcHNxAH4AKHNxAH4ALAAAACsAAAAIcQB+AC5zcQB+ACwAAAAMAAAACHEAfgCzcHNxAH4AKHNxAH4ALAAAACwAAAAIcQB+AC5zcQB+ACwAAAAEAAAACHEAfgCzeHEAfgBic3EAfgClcQB+AGJzcQB+AB4AAAACdwQAAAACc3IAL3NwZWMuY3ZsYXN0LkNWTFR5cGUkUHVyZUNWTFR5cGUkUHJpbWl0aXZlJFVJbnRLuQuajikSRikCAAJJAAhiaXRXaWR0aEkAAWt4cgApc3BlYy5jdmxhc3QuQ1ZMVHlwZSRQdXJlQ1ZMVHlwZSRQcmltaXRpdmUKm9v/NH7COwIAAHhyAB9zcGVjLmN2bGFzdC5DVkxUeXBlJFB1cmVDVkxUeXBl/Qa0FlO2KLECAAB4cQB+AJ0AAAEAAAABAHNyACZzcGVjLmN2bGFzdC5DVkxUeXBlJFB1cmVDVkxUeXBlJFN0cnVjdDVJoRRpEzmDAgACTAAGZmllbGRzcQB+AA5MAARuYW1lcQB+ABd4cQB+ASBzcQB+AB4AAAAHdwQAAAAHc3IAMnNwZWMuY3ZsYXN0LkNWTFR5cGUkUHVyZUNWTFR5cGUkU3RydWN0JFN0cnVjdEVudHJ5Mx8aM/226g0CAAJMAAdjdmxUeXBlcQB+AKlMAAlmaWVsZE5hbWVxAH4AF3hwc3EAfgEeAAABAAAAAQBxAH4AI3NxAH4BJXNyADtzcGVjLmN2bGFzdC5DVkxUeXBlJFB1cmVDVkxUeXBlJFByaW1pdGl2ZSRBY2NvdW50SWRlbnRpZmllciBFCkT8AptxAgAAeHEAfgEfcQB+AIJzcQB+ASVzcQB+AR4AAAAIAAAACHEAfgCGc3EAfgElc3EAfgEeAAAACAAAAAhxAH4AiXNxAH4BJXNyAC5zcGVjLmN2bGFzdC5DVkxUeXBlJFB1cmVDVkxUeXBlJFByaW1pdGl2ZSRCb29s26vBaNgwss8CAAB4cQB+AR9xAH4AjHNxAH4BJXNxAH4BHgAAAQAAAAEAcQB+AJBzcQB+ASVxAH4BMXEAfgCTeHEAfgCUeHNxAH4AHgAAAAJ3BAAAAAJzcgAUc3BlYy5jdmxhc3QuQ1ZMUGFyYW2VIEMsLC1O2QIABEwAAmlkcQB+ABdMAApvcmlnaW5hbElkcQB+ABdMAAVyYW5nZXEAfgAPTAAEdHlwZXEAfgCpeHBxAH4AI3EAfgAjc3EAfgAoc3EAfgAsAAAAGgAAAAZxAH4ALnNxAH4ALAAAABQAAAAGcQB+ASFzcQB+ATZxAH4AV3EAfgBXc3EAfgAoc3EAfgAsAAAAMQAAAAZxAH4ALnNxAH4ALAAAABwAAAAGcQB+ASN4c3EAfgAoc3EAfgAsAAAAAQAAAAlxAH4ALnNxAH4ALAAAAAAAAAAGc3IAJHNwZWMuY3ZsYXN0LkNWTFR5cGUkUHVyZUNWTFR5cGUkVm9pZIugZNWN+HVnAgAAeHEAfgEgcQB+ALN0AAxDVkwgZnVuY3Rpb24AAAADeHNxAH4AHgAAAAF3BAAAAAFzcQB+AL1xAH4AjHNxAH4Av3NxAH4AvXEAfgDCc3EAfgAgcQB+AMRxAH4AxHEAfgDFcQB+AFRxAH4AyXEAfgDQcQB+ANtxAH4A33hzcQB+AOMAcHNxAH4A5nNxAH4AvXEAfgCMc3EAfgC/c3EAfgC9cQB+AMJzcQB+ACBxAH4AxHEAfgDEcQB+AO1xAH4AVHEAfgDxcQB+APVxAH4A+nEAfgD+c3EAfgECc3EAfgAgcQB+ACNxAH4AI3EAfgEGcQB+AFRxAH4BCnEAfgERcQB+ARVxAH4BGXEAfgCzeHEAfgBic3EAfgClcQB+AGJzcQB+AB4AAAACdwQAAAACcQB+ASFxAH4BI3hzcQB+AB4AAAACdwQAAAACcQB+ATdxAH4BO3hxAH4BP3EAfgFDcQB+ALNxAH4BRHEAfgBkcQB+ADJxAH4BQ3BzcQB+AB4AAAACdwQAAAACcQB+AGtxAH4AdHhxAH4AlXEAfgAycQB+AJlwc3IAFnNwZWMuQ1ZMJEV4dGVybmFsRXhhY3TnMJk7lNdBOAIAAkwACnNpZ2hhc2hJbnR0ABBMZXZtL1NpZ2hhc2hJbnQ7TAAJc2lnbmF0dXJldAAvTHNwZWMvY3ZsYXN0L1F1YWxpZmllZE1ldGhvZFBhcmFtZXRlclNpZ25hdHVyZTt4cHNyAA5ldm0uU2lnaGFzaEludD27anqQ+KbVAgABTAABbnEAfgDOeHBzcQB+ANH///////////////7////+AAAAAXVxAH4A1AAAAASMQ6RBeHNyADdzcGVjLmN2bGFzdC5RdWFsaWZpZWRNZXRob2RTaWduYXR1cmUkUXVhbGlmaWVkTWV0aG9kU2lnGH1MtG0dbPUCAANMAAZwYXJhbXNxAH4ADkwAE3F1YWxpZmllZE1ldGhvZE5hbWV0AChMc3BlYy9jdmxhc3QvQ29udHJhY3RGdW5jdGlvbklkZW50aWZpZXI7TAADcmVzcQB+AA54cHEAfgBnc3IAHXNwZWMuY3ZsYXN0LlF1YWxpZmllZEZ1bmN0aW9u5SlM8uQ5UYMCAAJMAARob3N0dAAeTHNwZWMvY3ZsYXN0L1NvbGlkaXR5Q29udHJhY3Q7TAAIbWV0aG9kSWRxAH4AF3hwc3IAHHNwZWMuY3ZsYXN0LlNvbGlkaXR5Q29udHJhY3QjaX13GoE9ogIAAUwABG5hbWVxAH4AF3hwdAAMVGVzdENvbnRyYWN0dAAHd29ya09uU3EAfgBAc3IAE3ZjLmRhdGEuQ2FsbFN1bW1hcnlCLSM8Y2HMggIAEUkACXN1bW1hcnlJZEwADmNhbGxDb252ZW50aW9udAAmTGluc3RydW1lbnRhdGlvbi9jYWxscy9DYWxsQ29udmVudGlvbjtMAApjYWxsVGFyZ2V0cQB+AAVMAAhjYWxsVHlwZXQAFUx2Yy9kYXRhL1RBQ0NhbGxUeXBlO0wAD2Nhbm5vdEJlSW5saW5lZHQALUxhbmFseXNpcy9pY2ZnL0lubGluZXIkSWxsZWdhbElubGluaW5nUmVhc29uO0wABmdhc1ZhcnQAE0x2Yy9kYXRhL1RBQ1N5bWJvbDtMAAZpbkJhc2V0ABdMdmMvZGF0YS9UQUNTeW1ib2wkVmFyO0wACGluT2Zmc2V0cQB+AWxMAAZpblNpemVxAH4BbEwADG9yaWdDYWxsY29yZXQAIEx2Yy9kYXRhL1RBQ0NtZCRTaW1wbGUkQ2FsbENvcmU7TAAHb3V0QmFzZXEAfgFtTAAJb3V0T2Zmc2V0cQB+AWxMAAdvdXRTaXplcQB+AWxMAA1zaWdSZXNvbHV0aW9ucQB+AAVMABVzeW1ib2xpY1NpZ1Jlc29sdXRpb250ADNMYW5hbHlzaXMvcHRhL2FiaS9EZWNvZGVyQW5hbHlzaXMkQnVmZmVyQWNjZXNzUGF0aDtMAAV0b1ZhcnEAfgFsTAAIdmFsdWVWYXJxAH4BbHhwAAAAAHNyACRpbnN0cnVtZW50YXRpb24uY2FsbHMuQ2FsbENvbnZlbnRpb2591riWaBgUXgIAA0kACGNhbGxlcklkTAAFaW5wdXR0ABlMYW5hbHlzaXMvaWNmZy9DYWxsSW5wdXQ7TAAGcmF3T3V0dAAiTGluc3RydW1lbnRhdGlvbi9jYWxscy9DYWxsT3V0cHV0O3hwAAAAAHNyABdhbmFseXNpcy5pY2ZnLkNhbGxJbnB1dAPz2322YQJyAgAHTAAHYmFzZVZhcnQAGUx2Yy9kYXRhL1RBQ0V4cHIkU3ltJFZhcjtMABBlbmNvZGVkQXJndW1lbnRzdAAjTGFuYWx5c2lzL2ljZmcvQUJJQXJndW1lbnRFbmNvZGluZztMABNpbnB1dFNpemVMb3dlckJvdW5kcQB+AM5MAAZvZmZzZXR0ABVMdmMvZGF0YS9UQUNFeHByJFN5bTtMABRyYW5nZVRvRGVjb21wb3NlZEFyZ3QAD0xqYXZhL3V0aWwvTWFwO0wAEHNpbXBsaWZpZWRPZmZzZXR0ABtMdmMvZGF0YS9UQUNFeHByJFN5bSRDb25zdDtMAARzaXplcQB+AXh4cHNyABd2Yy5kYXRhLlRBQ0V4cHIkU3ltJFZhcn3uZ6Lnk1XTAgACTAABc3EAfgFtTAADdGFndAAJTHRhYy9UYWc7eHIAE3ZjLmRhdGEuVEFDRXhwciRTeW2iVj0S4YSNUAIAAHhyAA92Yy5kYXRhLlRBQ0V4cHIF2oBG6eLQeQIAAHhwc3IANnZjLmRhdGEuVEFDU3ltYm9sJFZhciRXaXRoRGVmYXVsdENhbGxJbmRleCRXaXRoQnl0ZU1hcJQkZfdbh3knAgACTAAEbWV0YXQAHkxjb20vY2VydG9yYS9jb2xsZWN0L1RyZWFwTWFwO0wACm5hbWVQcmVmaXhxAH4AF3hyABV2Yy5kYXRhLlRBQ1N5bWJvbCRWYXL8SGvUvjBGEQIAAHhyABF2Yy5kYXRhLlRBQ1N5bWJvbBKTItjnrHLUAgAAeHBzcgAgY29tLmNlcnRvcmEuY29sbGVjdC5IYXNoVHJlYXBNYXDOJ/t6rqVynAIAA0wAA2tleXEAfgA0TAAEbmV4dHQAK0xjb20vY2VydG9yYS9jb2xsZWN0L0tleVZhbHVlUGFpckxpc3QkTW9yZTtMAAV2YWx1ZXEAfgA0eHIAJGNvbS5jZXJ0b3JhLmNvbGxlY3QuQWJzdHJhY3RUcmVhcE1hcC1u3UdoTQYZAgAAeHIAGWNvbS5jZXJ0b3JhLmNvbGxlY3QuVHJlYXD/3sPjttw/IwIAAkwABGxlZnR0ABtMY29tL2NlcnRvcmEvY29sbGVjdC9UcmVhcDtMAAVyaWdodHEAfgGKeHBwc3EAfgGGcHNxAH4BhnBwc3IAC3RhYy5NZXRhS2V5avYXikOyot0CAANMAA9lcmFzdXJlU3RyYXRlZ3l0AB1MdGFjL01ldGFLZXkkRXJhc3VyZVN0cmF0ZWd5O0wABG5hbWVxAH4AF0wAA3R5cHQAEUxqYXZhL2xhbmcvQ2xhc3M7eHB+cgAbdGFjLk1ldGFLZXkkRXJhc3VyZVN0cmF0ZWd5AAAAAAAAAAASAAB4cQB+AFN0AAlDYW5vbmljYWx0ABR0YWMubWVtb3J5LnBhcnRpdGlvbnZyACNhbmFseXNpcy5wdGEuYWJpLlVuaW5kZXhlZFBhcnRpdGlvbjDC1l5m1rSBAgABSQACaWR4cHBzcQB+AZYAAAAAc3EAfgGOcQB+AZN0ABJUYWMuc3ltYm9sLmtleXdvcmR2cgAidmMuZGF0YS5UQUNTeW1ib2wkVmFyJEtleXdvcmRFbnRyeU7jwOQ0dtx2AgAAeHBwc3IAMnZjLmRhdGEuVEFDU3ltYm9sJFZhciRLZXl3b3JkRW50cnkkVEFDS2V5d29yZEVudHJ5uJkWjywELK0CAAJJABZtYXliZVRBQ0tleXdvcmRPcmRpbmFsTAAEbmFtZXEAfgAXeHEAfgGbAAAAAXQABHRhY01zcQB+AY5xAH4Bk3QADXRhYy5pcy5tZW1vcnl2cgAidGFjLk1ldGFNYXAkQ29tcGFuaW9uJE5vdGhpbmdWYWx1ZZZFj9hbs7zKAgAAeHBwc3EAfgGidAAOdGFjTUNBTk9OMCEhNzdzcgAPdGFjLlRhZyRCeXRlTWFwNb/Ry6GDRgkCAAB4cgALdGFjLlRhZyRNYXABJytzDV3P/QIAAHhyAAd0YWMuVGFneiXiZp1BxfUCAAB4cHBzcQB+ANH///////////////7////+AAAAAXVxAH4A1AAAAAIBBHhzcQB+AXxzcgA1dmMuZGF0YS5UQUNTeW1ib2wkVmFyJFdpdGhEZWZhdWx0Q2FsbEluZGV4JFdpdGhCaXQyNTaereCTFyF7ZAIAAkwABG1ldGFxAH4BgkwACm5hbWVQcmVmaXhxAH4AF3hxAH4Bg3NxAH4BhnNxAH4BhnBwcQB+AZlwc3EAfgGdAAAALXQAAUxwc3EAfgGOcQB+AZN0ABB0YWMuc3RhY2suaGVpZ2h0dnEAfgA2cHNxAH4ANgAAA/l0AANSNzhzcgAOdGFjLlRhZyRCaXQyNTYMJPutC/yioAIAAHhyAAx0YWMuVGFnJEJpdHNUJ0qe/HOtDAIABkkACGJpdHdpZHRoTAAJbWF4U2lnbmVkcQB+AM5MAAttYXhVbnNpZ25lZHEAfgDOTAALbWluU2lnbmVkMnNxAH4AzkwADW1pblNpZ25lZE1hdGhxAH4AzkwAB21vZHVsdXNxAH4AznhxAH4BqAAAAQBzcQB+ANH///////////////7////+AAAAAXVxAH4A1AAAACB//////////////////////////////////////////3hzcQB+ANH///////////////7////+AAAAAXVxAH4A1AAAACD//////////////////////////////////////////3hzcQB+ANH///////////////7////+AAAAAXVxAH4A1AAAACCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHhzcQB+ANH///////////////7////+/////3VxAH4A1AAAACCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHhzcQB+ANH///////////////7////+AAAAAXVxAH4A1AAAACEBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB4c3IAIWRhdGFzdHJ1Y3R1cmVzLkxpbmtlZEFycmF5SGFzaE1hcAAAAAAAAAABAwACRgAKbG9hZEZhY3RvckwACWhhc2hUYWJsZXQALkxkYXRhc3RydWN0dXJlcy9hcnJheWhhc2h0YWJsZS9BcnJheUhhc2hUYWJsZTt4cHcIAAAACUAAAABzcgAeYW5hbHlzaXMuaWNmZy5TY3JhdGNoQnl0ZVJhbmdlcBVIN3XCpkQCAAJMAARmcm9tcQB+AM5MAAJ0b3EAfgDOeHBxAH4A03EAfgELc3IALWFuYWx5c2lzLmljZmcuRGVjb21wb3NlZENhbGxJbnB1dEFyZyRDb25zdGFudF9fDNjJ39jVAgADTAABY3QAGUx2Yy9kYXRhL1RBQ1N5bWJvbCRDb25zdDtMABFjb250cmFjdFJlZmVyZW5jZXQAL0xhbmFseXNpcy9pY2ZnL0NhbGxHcmFwaEJ1aWxkZXIkQ2FsbGVkQ29udHJhY3Q7TAAMc2NyYXRjaFJhbmdldAAgTGFuYWx5c2lzL2ljZmcvU2NyYXRjaEJ5dGVSYW5nZTt4cgAkYW5hbHlzaXMuaWNmZy5EZWNvbXBvc2VkQ2FsbElucHV0QXJngXMTDVRLyWECAAB4cHNyABd2Yy5kYXRhLlRBQ1N5bWJvbCRDb25zdMb0SZoqlnyhAgACTAADdGFncQB+AX1MAAV2YWx1ZXEAfgDOeHEAfgGEcQB+AbpzcQB+ANH///////////////7////+AAAAAXVxAH4A1AAAACCMQ6RBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHhwcQB+AclzcQB+AchzcQB+ANH///////////////7////+AAAAAXVxAH4A1AAAAAEEeHNxAH4A0f///////////////v////4AAAABdXEAfgDUAAAAASN4c3IALWFuYWx5c2lzLmljZmcuRGVjb21wb3NlZENhbGxJbnB1dEFyZyRWYXJpYWJsZUiTw5kIXbZOAgADTAARY29udHJhY3RSZWZlcmVuY2VxAH4BzEwADHNjcmF0Y2hSYW5nZXEAfgHNTAABdnEAfgFteHEAfgHOc3IAO2FuYWx5c2lzLmljZmcuQ2FsbEdyYXBoQnVpbGRlciRDYWxsZWRDb250cmFjdCRTeW1ib2xpY0lucHV03IokCIIfcoUCAAJMAAhpbnB1dEFyZ3EAfgFtTAAGb2Zmc2V0cQB+AM54cgAtYW5hbHlzaXMuaWNmZy5DYWxsR3JhcGhCdWlsZGVyJENhbGxlZENvbnRyYWN00wt1rN/LodcCAAB4cHNxAH4BrXNxAH4BhnNxAH4BhnNxAH4BhnBwc3EAfgGOcQB+AZN0ABN0YWMuaW1tdXRhYmxlLmFycmF5dnIAFnZjLmRhdGEuSW1tdXRhYmxlQm91bmToHHLEJ13InwIAAUwAA3N5bXEAfgFseHBwc3EAfgHkc3EAfgGtc3EAfgGGcHBxAH4BmXBzcQB+AZ0AAAAMdAAPdGFjQ2FsbGRhdGFzaXplcQB+AepzcQB+AYZzcQB+AYZwcHNxAH4BjnEAfgGTdAAPdGFjLndvcmRtYXAta2V5dnEAfgDRcHEAfgHVcHNxAH4BjnEAfgGTdAAWdGFjLnNjYWxhcml6YXRpb24uc29ydHZyABl2Yy5kYXRhLlNjYWxhcml6YXRpb25Tb3J0VmJ1DbieFckCAAB4cHBzcgAfdmMuZGF0YS5TY2FsYXJpemF0aW9uU29ydCRTcGxpdKd9SM1exp31AgABTAADaWR4cQB+AM54cQB+AfJxAH4B1XEAfgGZcHNxAH4BnQAAAA90AA50YWNDYWxsZGF0YWJ1ZnNxAH4BhnBzcQB+AYZwcHNxAH4BjnEAfgGTdAAPdGFjLmlzLmNhbGxkYXRhcQB+AaNwcQB+AaRzcQB+AY5xAH4Bk3QAE3RhYy5jYWxsZGF0YS5vZmZzZXRxAH4B73BxAH4B1XNxAH4BjnEAfgGTdAAVdGFjLnN0b3JhZ2UuYml0LXdpZHRocQB+AbVwc3EAfgA2AAABAHQAEHRhY0NhbGxkYXRhYnVmITRxAH4B1XEAfgHUc3EAfgGtc3EAfgGGcHBzcQB+AY5xAH4Bk3QAGHRhYy5kZWNvbXAtaW5zY2FsYXIuc29ydHZyAB10YWMuRGVjb21wb3NlZElucHV0U2NhbGFyU29ydCYB+zj6Hp5PAgAAeHBwc3IAJHRhYy5EZWNvbXBvc2VkSW5wdXRTY2FsYXJTb3J0JFNpbXBsZaV1M5E4YID4AgABTAAKYnl0ZU9mZnNldHEAfgDOeHEAfgIGcQB+AdV0AANSNDdzcQB+AchzcQB+ANH///////////////7////+AAAAAXVxAH4A1AAAAAEkeHNxAH4A0f///////////////v////4AAAABdXEAfgDUAAAAAUN4c3EAfgHZc3IAPGFuYWx5c2lzLmljZmcuQ2FsbEdyYXBoQnVpbGRlciRDYWxsZWRDb250cmFjdCRVbnJlc29sdmVkUmVhZLWn3+cgAa1fAgABSQANc3RvcmFnZVJlYWRJZHhxAH4B3AAAAABxAH4CC3NxAH4BrXNxAH4BhnNxAH4BhnBzcQB+AYZwcHEAfgGZcHEAfgGxcQB+AgRwc3EAfgIIcQB+AgxwcQB+AbNwc3EAfgA2AAAD8XQAA1I1MHNxAH4ByHNxAH4A0f///////////////v////4AAAABdXEAfgDUAAAAAUR4c3EAfgDR///////////////+/////gAAAAF1cQB+ANQAAAABY3hzcQB+AdlzcQB+AhEAAAABcQB+AhpzcQB+Aa1zcQB+AYZzcQB+AYZwc3EAfgGGcHBxAH4BmXBxAH4BsXEAfgIEcHNxAH4CCHEAfgIbcHEAfgGzcHEAfgIYdAADUjU0c3EAfgHIc3EAfgDR///////////////+/////gAAAAF1cQB+ANQAAAABZHhzcQB+ANH///////////////7////+AAAAAXVxAH4A1AAAAAGDeHNxAH4B2XBxAH4CJ3NxAH4BrXNxAH4BhnNxAH4BhnBzcQB+AYZwcHEAfgGZcHEAfgGxcQB+AgRwc3EAfgIIcQB+AihwcQB+AbNwcQB+Ahh0AANSNTVzcQB+AchzcQB+ANH///////////////7////+AAAAAXVxAH4A1AAAAAGEeHNxAH4A0f///////////////v////4AAAABdXEAfgDUAAAAAaN4c3EAfgHZcHEAfgIzc3EAfgGtc3EAfgGGc3EAfgGGcHNxAH4BhnBwcQB+AZlwcQB+AbFxAH4CBHBzcQB+AghxAH4CNHBxAH4Bs3BxAH4CGHQAA1I1NnNxAH4ByHNxAH4A0f///////////////v////4AAAABdXEAfgDUAAAAAaR4c3EAfgDR///////////////+/////gAAAAF1cQB+ANQAAAABw3hzcQB+AdlwcQB+Aj9zcQB+Aa1zcQB+AYZzcQB+AYZwc3EAfgGGcHBxAH4BmXBxAH4BsXEAfgIEcHNxAH4CCHEAfgJAcHEAfgGzcHNxAH4ANgAAA+p0AANSNjVzcQB+AchzcQB+ANH///////////////7////+AAAAAXVxAH4A1AAAAAHEeHNxAH4A0f///////////////v////4AAAABdXEAfgDUAAAAAeN4c3EAfgHZc3EAfgIRAAAAAnEAfgJMc3EAfgGtc3EAfgGGc3EAfgGGcHNxAH4BhnBwcQB+AZlwcQB+AbFxAH4CBHBzcQB+AghxAH4CTXBxAH4Bs3BxAH4CGHQAA1I2OXNxAH4ByHNxAH4A0f///////////////v////4AAAABdXEAfgDUAAAAAeR4c3EAfgDR///////////////+/////gAAAAF1cQB+ANQAAAACAQN4c3EAfgHZcHEAfgJZc3EAfgGtc3EAfgGGc3EAfgGGcHNxAH4BhnBwcQB+AZlwcQB+AbFxAH4CBHBzcQB+AghxAH4CWnBxAH4Bs3BxAH4CSnQAA1I3NXhwc3EAfgF8c3EAfgGtc3EAfgGGc3EAfgGGcHBxAH4BmXBxAH4BsXBxAH4Bs3BzcQB+ADYAAAP4dAADUjc5cQB+AbpzcgAgaW5zdHJ1bWVudGF0aW9uLmNhbGxzLkNhbGxPdXRwdXQYx4kDUqG9yQIAA0wABGJhc2VxAH4BbUwABm9mZnNldHEAfgFsTAAEc2l6ZXEAfgFseHBzcQB+AYFzcQB+AYZwc3EAfgGGcHNxAH4BhnBwcQB+AZFwc3EAfgGWAAAAAnEAfgGZcHEAfgGecQB+AaBwcQB+AaR0AA10YWNNQ0FOT04xISE0c3EAfgGtc3EAfgGGc3EAfgGGcHBxAH4BmXBxAH4BsXBxAH4Bs3BxAH4BtnEAfgG3c3EAfgHQcQB+AbpxAH4A03NyACFkYXRhc3RydWN0dXJlcy5MaW5rZWRBcnJheUhhc2hTZXQAAAAAAAAAAQMAAkYACmxvYWRGYWN0b3JMAAloYXNoVGFibGVxAH4BxnhwdwgAAAABQAAAAHNyAERhbmFseXNpcy5pY2ZnLkNhbGxHcmFwaEJ1aWxkZXIkQ2FsbGVkQ29udHJhY3QkRnVsbHlSZXNvbHZlZCRTZWxmTGlua31nqfExKDtSAgABTAAKY29udHJhY3RJZHEAfgDOeHIAO2FuYWx5c2lzLmljZmcuQ2FsbEdyYXBoQnVpbGRlciRDYWxsZWRDb250cmFjdCRGdWxseVJlc29sdmVk7v5wMSFvqG0CAAB4cQB+AdxzcQB+ANH///////////////7////+AAAAAXVxAH4A1AAAABDORgSgAAAAAAAAAAAAAAABeHh+cgATdmMuZGF0YS5UQUNDYWxsVHlwZQAAAAAAAAAAEgAAeHEAfgBTdAAMUkVHVUxBUl9DQUxMcHNxAH4BrXNxAH4BhnNxAH4BhnBwcQB+AZlwcQB+AbFwcQB+AbNwc3EAfgA2AAAD9HQAA1I4MXNxAH4BgXNxAH4BhnBzcQB+AYZwc3EAfgGGcHBxAH4BkXBxAH4BmHEAfgGZcHEAfgGecQB+AaBwcQB+AaRxAH4BpXNxAH4BrXEAfgGvcQB+AbdzcQB+AdBxAH4BunEAfgGqc3IAHnZjLmRhdGEuVEFDQ21kJFNpbXBsZSRDYWxsQ29yZSVks7ylOe8ZAgALTAAIY2FsbFR5cGVxAH4BakwAA2dhc3EAfgFsTAAGaW5CYXNlcQB+AW1MAAhpbk9mZnNldHEAfgFsTAAGaW5TaXplcQB+AWxMAARtZXRhcQB+AYJMAAdvdXRCYXNlcQB+AW1MAAlvdXRPZmZzZXRxAH4BbEwAB291dFNpemVxAH4BbEwAAnRvcQB+AWxMAAV2YWx1ZXEAfgFseHIAFXZjLmRhdGEuVEFDQ21kJFNpbXBsZU9DbfgHXXOhAgAAeHIAE3ZjLmRhdGEuVEFDQ21kJFNwZWN8MxDUuqEG3AIAAHhyAA52Yy5kYXRhLlRBQ0NtZNIaJZ/9W6P7AgAAeHBxAH4Cf3NxAH4BrXEAfgKCcQB+AoVzcQB+AYFzcQB+AYZwc3EAfgGGcHNxAH4BhnBwcQB+AZFwcQB+AZhxAH4BmXBxAH4BnnEAfgGgcHEAfgGkcQB+AaVzcQB+Aa1xAH4Br3EAfgG3c3EAfgGtcQB+AmdxAH4CanNxAH4BhnBwc3EAfgGOfnEAfgGSdAAJQ2FsbFRyYWNldAAIdGFjLm1ldGF2cgATdmMuZGF0YS5UQUNNZXRhSW5mb0W7USKtClXbAgAGSQAFYmVnaW5JAANsZW5JAAZzb3VyY2VMAAdhZGRyZXNzcQB+AM5MAAhqdW1wVHlwZXQAE0xjb21waWxlci9KdW1wVHlwZTtMAA1zb3VyY2VDb250ZXh0dAAYTGNvbXBpbGVyL1NvdXJjZUNvbnRleHQ7eHBwc3EAfgKdAAABGgAAABUAAAAAcQB+Anx+cgARY29tcGlsZXIuSnVtcFR5cGUAAAAAAAAAABIAAHhxAH4AU3QAB1JFR1VMQVJzcgAWY29tcGlsZXIuU291cmNlQ29udGV4dIN4td4RYtbLAgACTAAPaW5kZXhUb0ZpbGVQYXRocQB+AXlMAAlzb3VyY2VEaXJxAH4AF3hwc3EAfgHFdwgAAAABQAAAAHNxAH4ANgAAAAB0ABBUZXN0Q29udHJhY3Quc29seHQAEy5wb3N0X2F1dG9maW5kZXJzLjBzcQB+AYFzcQB+AYZwc3EAfgGGcHNxAH4BhnBwcQB+AZFwc3EAfgGWAAAAAnEAfgGZcHEAfgGecQB+AaBwcQB+AaRxAH4CcnNxAH4BrXEAfgJ0cQB+AbdxAH4CdnNxAH4BrXNxAH4BhnNxAH4BhnNxAH4BhnBzcQB+AYZwcHNxAH4Bjn5xAH4BknQABkVyYXNlZHQAGnRhYy5jb250cmFjdC5zeW0uYWRkci5uYW1ldnIAEGphdmEubGFuZy5TdHJpbmeg8KQ4ejuzQgIAAHhwcHEAfgFmcQB+AZlwcQB+AbFwc3EAfgGOcQB+Ard0ABV0YWMuY29udHJhY3Quc3ltLmFkZHJxAH4B73BxAH4CfHBxAH4Bs3BzcQB+ADYAAAP9dAADUjE4c3EAfgHQcQB+AbpxAH4A03NxAH4BgXNxAH4BhnBzcQB+AYZwc3EAfgGGcHBxAH4BkXBzcQB+AZYAAAACcQB+AZlwcQB+AZ5xAH4BoHBxAH4BpHEAfgJyc3EAfgGtcQB+AnRxAH4Bt3EAfgJ2c3IAImphdmEudXRpbC5Db2xsZWN0aW9ucyRTaW5nbGV0b25TZXQsUkGYKcCxvwIAAUwAB2VsZW1lbnRxAH4ANHhwcQB+AVxwc3EAfgGtc3EAfgGGc3EAfgGGc3EAfgGGcHNxAH4BhnBwcQB+ArZwcQB+AWZxAH4BmXBxAH4BsXBxAH4CvHBxAH4CfHBxAH4Bs3BxAH4CvnEAfgK/c3EAfgHQcQB+AbpxAH4A03NyAEByZXBvcnQuY2FsbHJlc29sdXRpb24uQ2FsbFJlc29sdXRpb25UYWJsZVN1bW1hcnlJbmZvJERlZmF1bHRJbmZv3XK/8JXJObUCAAFMABFhcHBsaWNhdGlvblJlYXNvbnQAKExhbmFseXNpcy9pY2ZnL1N1bW1hcnlBcHBsaWNhdGlvblJlYXNvbjt4cgA0cmVwb3J0LmNhbGxyZXNvbHV0aW9uLkNhbGxSZXNvbHV0aW9uVGFibGVTdW1tYXJ5SW5mbxq20EbaZsyGAgABTAANaW5mbyRkZWxlZ2F0ZXEAfgAxeHBzcQB+ADNzcQB+AcV3CAAAAAFAAAAAdAAac3VtbWFyeSBhcHBsaWNhdGlvbiByZWFzb250AD5kZWNsYXJlZCBhdCB0ZXN0LnNwZWM6NDo2NSB0byBhcHBseSB0byBhbGwgY2FsbHMgdG8gdGhlIGNhbGxlZXhzcgAvYW5hbHlzaXMuaWNmZy5TdW1tYXJ5QXBwbGljYXRpb25SZWFzb24kU3BlYyRBbGw1W33ZVBMA7QIAAkwAA2xvY3EAfgAPTAAPbWV0aG9kU2lnbmF0dXJlcQB+ABd4cgArYW5hbHlzaXMuaWNmZy5TdW1tYXJ5QXBwbGljYXRpb25SZWFzb24kU3BlY55PD9KbXiwdAgAAeHIAJmFuYWx5c2lzLmljZmcuU3VtbWFyeUFwcGxpY2F0aW9uUmVhc29uQpw/oqvoOJoCAAB4cHEAfgCVdAAld29ya09uUyh1aW50MjU2LCBUZXN0Q29udHJhY3QuU2ltcGxlKXEAfgKhc3IAIGNvbS5jZXJ0b3JhLmNvbGxlY3QuSGFzaFRyZWFwU2V0jmFHQLssXfQCAAJMAAdlbGVtZW50cQB+ADRMAARuZXh0dAAmTGNvbS9jZXJ0b3JhL2NvbGxlY3QvRWxlbWVudExpc3QkTW9yZTt4cgAkY29tLmNlcnRvcmEuY29sbGVjdC5BYnN0cmFjdFRyZWFwU2V0qaFSgJbf+3YCAAB4cQB+AYlzcQB+AtxzcQB+AtxzcQB+AtxzcQB+AtxwcHEAfgKGcHBxAH4CwXBwcQB+Aslwc3EAfgLcc3EAfgLccHNxAH4C3HNxAH4C3HBzcQB+AtxwcHEAfgItcHEAfgIhcHNxAH4C3HBwcQB+AkVwcQB+AjlwcQB+AhNwc3EAfgLcc3EAfgLccHBxAH4CX3BwcQB+Aa5wcQB+AlNwcQB+AgJwc3EAfgLccHBxAH4CgXBxAH4CZnA="}
		AssignExpCmd calledContract:13 R18:78
		AssignExpCmd executingContract:69 R18:78
		AssignExpCmd CANON2!!83:8 R18:78
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.CVLSnippetCmd.CVLFunctionStart","callIndex":3,"name":"workOnSCVL","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":3,"charByteOffset":64},"end":{"line":3,"charByteOffset":80}},"isNoRevert":true}}
		LabelCmd "1: Move primitive value for variable x462463:int..."
		LabelCmd "...done 1"
		AssignExpCmd CANON62:55 tacCalldatabufCANON0@1:140
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.CVLSnippetCmd.CVLArg.PrimitiveArg","callIndex":3,"index":0,"sym":{"namePrefix":"CANON62","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Function","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":6,"charByteOffset":20},"end":{"line":6,"charByteOffset":26}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"x"}]},"param":{"Named_type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"id":"x","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":6,"charByteOffset":20},"end":{"line":6,"charByteOffset":26}}}}}
		LabelCmd "16: Write struct..."
		LabelCmd "3: Write field x for variable s464465:TestContract.Simple..."
		LabelCmd "2: Move primitive value for variable tacTmp!fieldx522:int..."
		LabelCmd "...done 2"
		LabelCmd "...done 3"
		LabelCmd "5: Write field y for variable s464465:TestContract.Simple..."
		LabelCmd "4: Move primitive value for variable tacTmp!fieldy527:int..."
		LabelCmd "...done 4"
		LabelCmd "...done 5"
		LabelCmd "7: Write field z1 for variable s464465:TestContract.Simple..."
		LabelCmd "6: Move primitive value for variable tacTmp!fieldz1532:int..."
		LabelCmd "...done 6"
		LabelCmd "...done 7"
		LabelCmd "9: Write field z2 for variable s464465:TestContract.Simple..."
		LabelCmd "8: Move primitive value for variable tacTmp!fieldz2537:int..."
		LabelCmd "...done 8"
		LabelCmd "...done 9"
		LabelCmd "11: Write field b1 for variable s464465:TestContract.Simple..."
		LabelCmd "10: Move primitive value for variable tacTmp!fieldb1542:bool..."
		LabelCmd "...done 10"
		LabelCmd "...done 11"
		LabelCmd "13: Write field x2 for variable s464465:TestContract.Simple..."
		LabelCmd "12: Move primitive value for variable tacTmp!fieldx2552:int..."
		LabelCmd "...done 12"
		LabelCmd "...done 13"
		LabelCmd "15: Write field b2 for variable s464465:TestContract.Simple..."
		LabelCmd "14: Move primitive value for variable tacTmp!fieldb2557:bool..."
		LabelCmd "...done 14"
		LabelCmd "...done 15"
		LabelCmd "...done 16"
		AnnotationCmd JSON{"key":{"name":"cvl.trace.data.movement","type":"spec.CVLCompiler$Companion$TraceMeta$CVLMovement","erasureStrategy":"Erased"},"value":{"dst":{"id":"s461"},"src":{"id":"s464465"}}}
		AssignExpCmd CANON67:56 R50:30
		AssignExpCmd CANON68:57 R54:30
		AssignExpCmd CANON69:58 R55:30
		AssignExpCmd CANON70:59 R56:30
		AssignExpCmd CANON71:60 LNot(Eq(R65:22 0x0 ) )
		AssignExpCmd CANON72:61 R69:30
		AssignExpCmd CANON73:62 LNot(Eq(R75:22 0x0 ) )
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.CVLSnippetCmd.CVLArg.StructArg","callIndex":3,"index":1,"symbols":[{"namePrefix":"CANON67","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Function","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":6,"charByteOffset":28},"end":{"line":6,"charByteOffset":49}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"s.x"}]},{"namePrefix":"CANON68","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"fields":[{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Function","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":6,"charByteOffset":28},"end":{"line":6,"charByteOffset":49}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"s.y"}]},{"namePrefix":"CANON69","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"fields":[{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Function","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":6,"charByteOffset":28},"end":{"line":6,"charByteOffset":49}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"s.z1"}]},{"namePrefix":"CANON70","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"fields":[{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Function","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":6,"charByteOffset":28},"end":{"line":6,"charByteOffset":49}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"s.z2"}]},{"namePrefix":"CANON71","tag":{"#class":"tac.Tag.Bool"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"fields":[{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Function","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":6,"charByteOffset":28},"end":{"line":6,"charByteOffset":49}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"s.b1"}]},{"namePrefix":"CANON72","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"fields":[{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Function","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":6,"charByteOffset":28},"end":{"line":6,"charByteOffset":49}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"s.x2"}]},{"namePrefix":"CANON73","tag":{"#class":"tac.Tag.Bool"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"fields":[{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Function","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":6,"charByteOffset":28},"end":{"line":6,"charByteOffset":49}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"s.b2"}]}],"param":{"Named_type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"TestContract.Simple","fields":[{"fieldName":"x","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"y","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"z1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"z2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":8}},{"fieldName":"b1","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}},{"fieldName":"x2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"b2","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"}}]},"id":"s","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":6,"charByteOffset":28},"end":{"line":6,"charByteOffset":49}}}}}
		AnnotationCmd:141 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Havoc","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":7,"charByteOffset":4},"end":{"line":7,"charByteOffset":31}},"targets":[{"#class":"spec.cvlast.CVLExp.FieldSelectExp","structExp":{"#class":"spec.cvlast.CVLExp.ArrayDerefExp","array":{"#class":"spec.cvlast.CVLExp.FieldSelectExp","structExp":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"testContract","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":3}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.CodeContract","name":{"name":"TestContract"}},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":7,"charByteOffset":10},"end":{"line":7,"charByteOffset":22}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.CVLExp$VariableExp$ContractInstanceId","instanceId":"ce4604a0000000000000000000000001"}},"twoStateIndex":"NEITHER"},"fieldName":"m","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":3}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.VM","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMMappingDescriptor","keyType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"valueType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.EVMStructDescriptor","canonicalId":"TestContract.sol|TestContract.Simple","location":null,"fields":[{"fieldName":"x","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"fieldName":"y","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}},{"fieldName":"z1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8}},{"fieldName":"z2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8}},{"fieldName":"b1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}},{"fieldName":"x2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"fieldName":"b2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}}],"name":"TestContract.Simple"},"location":null},"context":{"#class":"spec.cvlast.typedescriptors.FromVMContext.StateValue"}},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":7,"charByteOffset":10},"end":{"line":7,"charByteOffset":24}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.StorageAccessMarker"}}},"index":{"#class":"spec.cvlast.CVLExp.Constant.NumberLit","n":"0","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":3}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral","n":"0"},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":7,"charByteOffset":25},"end":{"line":7,"charByteOffset":26}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":3}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.VM","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMStructDescriptor","canonicalId":"TestContract.sol|TestContract.Simple","location":null,"fields":[{"fieldName":"x","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"fieldName":"y","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}},{"fieldName":"z1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8}},{"fieldName":"z2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8}},{"fieldName":"b1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}},{"fieldName":"x2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"fieldName":"b2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}}],"name":"TestContract.Simple"},"context":{"#class":"spec.cvlast.typedescriptors.FromVMContext.StateValue"}},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":7,"charByteOffset":10},"end":{"line":7,"charByteOffset":27}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.StorageAccessMarker"}}},"fieldName":"b1","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":3}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.VM","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$bool"},"context":{"#class":"spec.cvlast.typedescriptors.FromVMContext.StateValue"}},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":7,"charByteOffset":10},"end":{"line":7,"charByteOffset":30}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.StorageAccessMarker"}}}],"assumingExp":null,"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":3}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssignExpCmd:142 I88 0x0
		AssertCmd:143 true "sanity bounds check on cvl to vm encoding (unsigned int elements of a user array) of %1$s failed"
		AssignExpCmd:144 R89:21 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(skey_basic:bif 0x0) Apply(skey_basic:bif 0x0))
		AssignExpCmd:144 R90:21 Apply(skey_add:bif R89:21 0x1)
		AssignHavocCmd:144 B91:21
		AssignExpCmd:144 R92:21 Ite(B91:21 0x1 0x0 )
		AssignExpCmd:145 CANON53!!93:18 AnnotationExp(Store(CANON53!!12:18 R90:146 R92:21 ) JSON{"key":{"name":"tac.storage.access-paths","type":"analysis.storage.StorageAnalysisResult$AccessPaths","erasureStrategy":"Canonical"},"value":{"paths":[{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.StructAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.MapAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.Root","slot":"0"},"key":{"#class":"vc.data.TACSymbol.Const","value":"0"},"baseSlot":{"#class":"vc.data.TACSymbol.Const","value":"0"},"hashResult":{"#class":"vc.data.TACSymbol.Const","value":"0"}},"offset":{"#class":"analysis.storage.StorageAnalysis.Offset.Bytes","numBytes":"36"}}]}})
		AnnotationCmd:144 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.DirectStorageHavoc","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R92","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"displayPath":{"#class":"analysis.storage.DisplayPath.FieldAccess","field":"b1","base":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Const","value":"0"},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"uint256","numBytes":"20","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"m"}}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"},"contractInstance":"ce4604a0000000000000000000000001","range":{"specFile":"test.spec","start":{"line":7,"charByteOffset":10},"end":{"line":7,"charByteOffset":30}}}}
		AssignExpCmd:147 B94 true
		AnnotationCmd:144 JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":21}
		AnnotationCmd:148 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.AssumeCmd.Assume","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":8,"charByteOffset":4},"end":{"line":8,"charByteOffset":44}},"exp":{"#class":"spec.cvlast.CVLExp.RelopExp.EqExp","l":{"#class":"spec.cvlast.CVLExp.FieldSelectExp","structExp":{"#class":"spec.cvlast.CVLExp.ArrayDerefExp","array":{"#class":"spec.cvlast.CVLExp.FieldSelectExp","structExp":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"testContract","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":3}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.CodeContract","name":{"name":"TestContract"}},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":8,"charByteOffset":12},"end":{"line":8,"charByteOffset":24}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.CVLExp$VariableExp$ContractInstanceId","instanceId":"ce4604a0000000000000000000000001"}},"twoStateIndex":"NEITHER"},"fieldName":"m","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":3}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.VM","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMMappingDescriptor","keyType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"valueType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.EVMStructDescriptor","canonicalId":"TestContract.sol|TestContract.Simple","location":null,"fields":[{"fieldName":"x","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"fieldName":"y","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}},{"fieldName":"z1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8}},{"fieldName":"z2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8}},{"fieldName":"b1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}},{"fieldName":"x2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"fieldName":"b2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}}],"name":"TestContract.Simple"},"location":null},"context":{"#class":"spec.cvlast.typedescriptors.FromVMContext.StateValue"}},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":8,"charByteOffset":12},"end":{"line":8,"charByteOffset":26}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.StorageAccessMarker"}}},"index":{"#class":"spec.cvlast.CVLExp.Constant.NumberLit","n":"0","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":3}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral","n":"0"},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":8,"charByteOffset":27},"end":{"line":8,"charByteOffset":28}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":3}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.VM","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMStructDescriptor","canonicalId":"TestContract.sol|TestContract.Simple","location":null,"fields":[{"fieldName":"x","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"fieldName":"y","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}},{"fieldName":"z1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8}},{"fieldName":"z2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8}},{"fieldName":"b1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}},{"fieldName":"x2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"fieldName":"b2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}}],"name":"TestContract.Simple"},"context":{"#class":"spec.cvlast.typedescriptors.FromVMContext.StateValue"}},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":8,"charByteOffset":12},"end":{"line":8,"charByteOffset":29}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.StorageAccessMarker"}}},"fieldName":"b1","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":3}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.VM","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$bool"},"context":{"#class":"spec.cvlast.typedescriptors.FromVMContext.StateValue"}},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":8,"charByteOffset":12},"end":{"line":8,"charByteOffset":32}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.StorageAccessMarker"}}},"r":{"#class":"spec.cvlast.CVLExp.RelopExp.ArithRelopExp.GtExp","l":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"x","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":3}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":8,"charByteOffset":37},"end":{"line":8,"charByteOffset":38}}},"twoStateIndex":"NEITHER"},"r":{"#class":"spec.cvlast.CVLExp.Constant.NumberLit","n":"3","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":3}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral","n":"3"},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":8,"charByteOffset":41},"end":{"line":8,"charByteOffset":42}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":3}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":8,"charByteOffset":37},"end":{"line":8,"charByteOffset":42}},"hasParens":true}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":3}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":8,"charByteOffset":12},"end":{"line":8,"charByteOffset":43}}}},"description":null,"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":3}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssignExpCmd:149 I95 0x0
		AssertCmd:150 true "sanity bounds check on cvl to vm encoding (unsigned int elements of a user array) of %1$s failed"
		AssignExpCmd:151 R96:21 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(skey_basic:bif 0x0) Apply(skey_basic:bif 0x0))
		AssignExpCmd:151 R97:21 Apply(skey_add:bif R96:21 0x1)
		AssignExpCmd:152 R98:21 AnnotationExp(Select(CANON53!!93:153 R97:154 ) JSON{"key":{"name":"tac.storage.access-paths","type":"analysis.storage.StorageAnalysisResult$AccessPaths","erasureStrategy":"Canonical"},"value":{"paths":[{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.StructAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.MapAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.Root","slot":"0"},"key":{"#class":"vc.data.TACSymbol.Const","value":"0"},"baseSlot":{"#class":"vc.data.TACSymbol.Const","value":"0"},"hashResult":{"#class":"vc.data.TACSymbol.Const","value":"0"}},"offset":{"#class":"analysis.storage.StorageAnalysis.Offset.Bytes","numBytes":"36"}}]}})
		AssumeExpCmd Eq(R98:21 0x0 )
		AssignExpCmd:151 B99 false
		AnnotationCmd:151 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.DirectStorageLoad","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"B99","tag":{"#class":"tac.Tag.Bool"},"callIndex":0},"displayPath":{"#class":"analysis.storage.DisplayPath.FieldAccess","field":"b1","base":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Const","value":"0"},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"uint256","numBytes":"20","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"m"}}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"},"contractInstance":"ce4604a0000000000000000000000001","range":{"specFile":"test.spec","start":{"line":8,"charByteOffset":12},"end":{"line":8,"charByteOffset":32}}}}
		AssignExpCmd:155 I100 CANON62:55
		AssignExpCmd:156 I101 0x3
		AssignExpCmd:157 B102 false
		AssignExpCmd:158 CANON88:65 true
		AnnotationCmd:151 JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":22}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.CVLSnippetCmd.CVLFunctionEnd","callIndex":3,"name":"workOnSCVL"}}
		AnnotationCmd JSON{"key":{"name":"revert.confluence","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd "join point of revert handling"
		AnnotationCmd JSON{"key":{"name":"call.trace.external.summary.end","type":"analysis.icfg.SummaryStack$SummaryEnd$External","erasureStrategy":"CallTrace"},"value":"rO0ABXNyAC5hbmFseXNpcy5pY2ZnLlN1bW1hcnlTdGFjayRTdW1tYXJ5RW5kJEV4dGVybmFsH6pYA2Le9wICAAJJAAlzdW1tYXJ5SWRMAA5hcHBsaWVkU3VtbWFyeXQALExhbmFseXNpcy9pY2ZnL1N1bW1hcml6YXRpb24kQXBwbGllZFN1bW1hcnk7eHIAJWFuYWx5c2lzLmljZmcuU3VtbWFyeVN0YWNrJFN1bW1hcnlFbmQVlCYDx9Zr6QIAAHhwAAAAAnNyADdhbmFseXNpcy5pY2ZnLlN1bW1hcml6YXRpb24kQXBwbGllZFN1bW1hcnkkTWV0aG9kc0Jsb2NrxBlpQb2eQrwCAAJMAAxzcGVjQ2FsbFN1bW10AC5Mc3BlYy9jdmxhc3QvU3BlY0NhbGxTdW1tYXJ5JEV4cHJlc3NpYmxlSW5DVkw7TAAQc3VtbWFyaXplZE1ldGhvZHQAG0xzcGVjL0NWTCRTdW1tYXJ5U2lnbmF0dXJlO3hwc3IAH3NwZWMuY3ZsYXN0LlNwZWNDYWxsU3VtbWFyeSRFeHCItcAI/3pVHwIAB0wAA2V4cHQAFExzcGVjL2N2bGFzdC9DVkxFeHA7TAAMZXhwZWN0ZWRUeXBldAAQTGphdmEvdXRpbC9MaXN0O0wACWZ1blBhcmFtc3EAfgAKTAAFcmFuZ2V0AA1MdXRpbHMvUmFuZ2U7TAAFc2NvcGV0ABZMc3BlYy9jdmxhc3QvQ1ZMU2NvcGU7TAARc3VtbWFyaXphdGlvbk1vZGV0AC9Mc3BlYy9jdmxhc3QvU3BlY0NhbGxTdW1tYXJ5JFN1bW1hcml6YXRpb25Nb2RlO0wACndpdGhDbGF1c2V0ACxMc3BlYy9jdmxhc3QvU3BlY0NhbGxTdW1tYXJ5JEV4cCRXaXRoQ2xhdXNlO3hyACxzcGVjLmN2bGFzdC5TcGVjQ2FsbFN1bW1hcnkkRXhwcmVzc2libGVJbkNWTDmMEQXE2U43AgAAeHIAG3NwZWMuY3ZsYXN0LlNwZWNDYWxsU3VtbWFyeZ/hCJ5dxaUBAgAAeHBzcgAnc3BlYy5jdmxhc3QuQ1ZMRXhwJEFwcGx5RXhwJENWTEZ1bmN0aW9uCF/yx/bQMDoCAAVaAAhub1JldmVydEwABGFyZ3NxAH4ACkwAAmlkdAASTGphdmEvbGFuZy9TdHJpbmc7TAAXbWV0aG9kSWRXaXRoQ2FsbENvbnRleHR0AB1Mc3BlYy9jdmxhc3QvU3BlY0RlY2xhcmF0aW9uO0wAA3RhZ3QAF0xzcGVjL2N2bGFzdC9DVkxFeHBUYWc7eHIAG3NwZWMuY3ZsYXN0LkNWTEV4cCRBcHBseUV4cAXcmU1H7VK7AgAAeHIAIXNwZWMuY3ZsYXN0LkNWTEV4cCRBcHBsaWNhdGlvbkV4cAR7vMV6A/l9AgAAeHIAEnNwZWMuY3ZsYXN0LkNWTEV4cAH4n9w14ZOIAgAAeHABc3IAE2phdmEudXRpbC5BcnJheUxpc3R4gdIdmcdhnQMAAUkABHNpemV4cAAAAAJ3BAAAAAJzcgAec3BlYy5jdmxhc3QuQ1ZMRXhwJFZhcmlhYmxlRXhwnRQuSnnYgo0CAARMAAJpZHEAfgATTAAMb3JpZ2luYWxOYW1lcQB+ABNMAAN0YWdxAH4AFUwADXR3b1N0YXRlSW5kZXh0ABtMc3BlYy9jdmxhc3QvVHdvU3RhdGVJbmRleDt4cQB+ABh0AAF4cQB+AB9zcgAVc3BlYy5jdmxhc3QuQ1ZMRXhwVGFn1YsqmFoL+1MCAAVaAAloYXNQYXJlbnNMAAphbm5vdGF0aW9udAAiTHNwZWMvY3ZsYXN0L0V4cHJlc3Npb25Bbm5vdGF0aW9uO0wABXJhbmdlcQB+AAtMAAVzY29wZXEAfgAMTAAEdHlwZXQAFUxzcGVjL2N2bGFzdC9DVkxUeXBlO3hwAHBzcgARdXRpbHMuUmFuZ2UkUmFuZ2V6V69yjESxBgIAA0wAA2VuZHQAFkx1dGlscy9Tb3VyY2VQb3NpdGlvbjtMAAhzcGVjRmlsZXEAfgATTAAFc3RhcnRxAH4AJXhyAAt1dGlscy5SYW5nZegD9PKVZX9XAgAAeHBzcgAUdXRpbHMuU291cmNlUG9zaXRpb26V9OfU6pnEjQIAAkkADmNoYXJCeXRlT2Zmc2V0SQAEbGluZXhwAAAATAAAAAN0AAl0ZXN0LnNwZWNzcQB+ACgAAABLAAAAA3NyABRzcGVjLmN2bGFzdC5DVkxTY29wZSLJYFjUHV1UAgADTAAWaGFzaENvZGVDYWNoZSRkZWxlZ2F0ZXQADUxrb3RsaW4vTGF6eTtMAAppbm5lclNjb3BlcQB+AAxMAApzY29wZVN0YWNrcQB+AAp4cHNyABprb3RsaW4uSW5pdGlhbGl6ZWRMYXp5SW1wbHvHf/EgKoGNAgABTAAFdmFsdWV0ABJMamF2YS9sYW5nL09iamVjdDt4cHNyABFqYXZhLmxhbmcuSW50ZWdlchLioKT3gYc4AgABSQAFdmFsdWV4cgAQamF2YS5sYW5nLk51bWJlcoaslR0LlOCLAgAAeHDM8ahfc3EAfgAsc3EAfgAvc3EAfgAyTmeNYXNxAH4ALHNxAH4AL3NxAH4AMgAAAB9wc3IAHGtvdGxpbi5jb2xsZWN0aW9ucy5FbXB0eUxpc3SZb8fQp+BgMgIAAHhwc3IAI2phdmEudXRpbC5Db2xsZWN0aW9ucyRTaW5nbGV0b25MaXN0Ku8pEDynm5cCAAFMAAdlbGVtZW50cQB+ADB4cHNyACZzcGVjLmN2bGFzdC5DVkxTY29wZSRJdGVtJEFzdFNjb3BlSXRlbYebp/cG1aGTAgAAeHIAGXNwZWMuY3ZsYXN0LkNWTFNjb3BlJEl0ZW0vA6//njdWRQIAAHhwc3EAfgAaAAAAAncEAAAAAnEAfgBBc3IAK3NwZWMuY3ZsYXN0LkNWTFNjb3BlJEl0ZW0kRXhwcmVzc2lvblN1bW1hcnkPMxqdWl+paAIAAUkAB3Njb3BlSWR4cgApc3BlYy5jdmxhc3QuQ1ZMU2NvcGUkSXRlbSRBU1RFbGVtZW50U2NvcGVSq48RUeQilgIAAUwAB2VsZW1lbnR0ABpMc3BlYy9jdmxhc3QvQ3JlYXRlc1Njb3BlO3hxAH4AQHNxAH4ACHNyACVzcGVjLmN2bGFzdC5DVkxFeHAkVW5yZXNvbHZlZEFwcGx5RXhwNT4Xghu5fcgCAAhaAAxpbnZva2VJc1NhZmVaAA1pbnZva2VJc1dob2xlTAAEYXJnc3EAfgAKTAAEYmFzZXEAfgAJTAANaW52b2tlU3RvcmFnZXQAIExzcGVjL2N2bGFzdC9DVkxFeHAkVmFyaWFibGVFeHA7TAAIbWV0aG9kSWRxAH4AE0wAA3RhZ3EAfgAVTAANdHdvU3RhdGVJbmRleHEAfgAdeHEAfgAXAQBzcQB+ABoAAAACdwQAAAACc3EAfgAccQB+AB9xAH4AH3NxAH4AIABwcQB+ACdxAH4ALnB+cgAZc3BlYy5jdmxhc3QuVHdvU3RhdGVJbmRleAAAAAAAAAAAEgAAeHIADmphdmEubGFuZy5FbnVtAAAAAAAAAAASAAB4cHQAB05FSVRIRVJzcQB+ABx0AAFzcQB+AFNzcQB+ACAAcHNxAH4AJHNxAH4AKAAAAE8AAAADcQB+ACpzcQB+ACgAAABOAAAAA3EAfgAucHEAfgBQeHBzcQB+ABx0AAtsYXN0U3RvcmFnZXEAfgBZc3EAfgAgAHBzcgARdXRpbHMuUmFuZ2UkRW1wdHnEgx6SXniV1wIAAUwAB2NvbW1lbnRxAH4AE3hxAH4AJnQAEmVtcHR5IHN0b3JhZ2UgdHlwZXEAfgAucHEAfgBQdAAKd29ya09uU0NWTHNxAH4AIABwc3EAfgAkc3EAfgAoAAAAUAAAAANxAH4AKnNxAH4AKAAAAEAAAAADcQB+AC5wcQB+AFBwc3EAfgAaAAAAAncEAAAAAnNyABlzcGVjLmN2bGFzdC5WTVBhcmFtJE5hbWVkAF3s8I660I0CAARMAARuYW1lcQB+ABNMAAxvcmlnaW5hbE5hbWVxAH4AE0wABXJhbmdlcQB+AAtMAAZ2bVR5cGV0AC5Mc3BlYy9jdmxhc3QvdHlwZWRlc2NyaXB0b3JzL1ZNVHlwZURlc2NyaXB0b3I7eHIAE3NwZWMuY3ZsYXN0LlZNUGFyYW2gOaiA+zBevwIAAHhwcQB+AB9xAH4AH3NxAH4AJHNxAH4AKAAAABsAAAADcQB+ACpzcQB+ACgAAAAVAAAAA3NyADNzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkVUludEuoeixLMHoOJQIAAUkACGJpdHdpZHRoeHIARHNwZWMuY3ZsYXN0LnR5cGVkZXNjcmlwdG9ycy5FVk1UeXBlRGVzY3JpcHRvciRFVk1Jc29tb3JwaGljVmFsdWVUeXBlluOVd2rd8X8CAAB4cgA6c3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yJEVWTVZhbHVlVHlwZRDk0vWorzfhAgAAeHIALXNwZWMuY3ZsYXN0LnR5cGVkZXNjcmlwdG9ycy5FVk1UeXBlRGVzY3JpcHRvcl5WHdzGjj7oAgAAeHAAAAEAc3EAfgBkcQB+AFNxAH4AU3NxAH4AJHNxAH4AKAAAADIAAAADcQB+ACpzcQB+ACgAAAAdAAAAA3NyAEFzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkRVZNU3RydWN0RGVzY3JpcHRvcqYN148TAOFKAgAETAALY2Fub25pY2FsSWRxAH4AE0wABmZpZWxkc3EAfgAKTAAIbG9jYXRpb250ADJMc3BlYy9jdmxhc3QvdHlwZWRlc2NyaXB0b3JzL0VWTUxvY2F0aW9uU3BlY2lmaWVyO0wABG5hbWVxAH4AE3hxAH4AbnQAJFRlc3RDb250cmFjdC5zb2x8VGVzdENvbnRyYWN0LlNpbXBsZXNxAH4AGgAAAAd3BAAAAAdzcgBQc3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yJEVWTVN0cnVjdERlc2NyaXB0b3IkRVZNU3RydWN0RW50cnkfXd8E+GvhmwIAAkwACWZpZWxkTmFtZXEAfgATTAAJZmllbGRUeXBldAAvTHNwZWMvY3ZsYXN0L3R5cGVkZXNjcmlwdG9ycy9FVk1UeXBlRGVzY3JpcHRvcjt4cHEAfgAfc3EAfgBrAAABAHNxAH4AeXQAAXlzcgA1c3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yJGFkZHJlc3PEsTBR9nlqCAIAAHhxAH4AbHNxAH4AeXQAAnoxc3EAfgBrAAAACHNxAH4AeXQAAnoyc3EAfgBrAAAACHNxAH4AeXQAAmIxc3IAMnNwZWMuY3ZsYXN0LnR5cGVkZXNjcmlwdG9ycy5FVk1UeXBlRGVzY3JpcHRvciRib29sBUKy4CN7H8kCAAB4cQB+AGxzcQB+AHl0AAJ4MnNxAH4AawAAAQBzcQB+AHl0AAJiMnEAfgCKeHB0ABNUZXN0Q29udHJhY3QuU2ltcGxleHNxAH4AJHNxAH4AKAAAAFAAAAADcQB+ACpzcQB+ACgAAABAAAAAA3EAfgAufnIALXNwZWMuY3ZsYXN0LlNwZWNDYWxsU3VtbWFyeSRTdW1tYXJpemF0aW9uTW9kZQAAAAAAAAAAEgAAeHEAfgBPdAADQUxMcAAAAAB4c3IAFnNwZWMuY3ZsYXN0LkNWTFR5cGUkVk2jqzstHXzffQIAAkwAB2NvbnRleHR0ACtMc3BlYy9jdmxhc3QvdHlwZWRlc2NyaXB0b3JzL0Zyb21WTUNvbnRleHQ7TAAKZGVzY3JpcHRvcnEAfgBleHIAE3NwZWMuY3ZsYXN0LkNWTFR5cGV0MROVt8FlUAIAAHhwc3IAQ3NwZWMuY3ZsYXN0LnR5cGVkZXNjcmlwdG9ycy5Gcm9tVk1Db250ZXh0JEV4dGVybmFsU3VtbWFyeUFyZ0JpbmRpbmfCdEzp+Ew/ewIAAHhyAClzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRnJvbVZNQ29udGV4dMXa8Yb3d/BlAgAAeHBxAH4Ab3EAfgBQc3EAfgAccQB+AFNxAH4AU3NxAH4AIABwcQB+AFVxAH4ALnNxAH4Al3EAfgCdcQB+AHZxAH4AUHhxAH4AXnNyABtzcGVjLmN2bGFzdC5TcGVjRGVjbGFyYXRpb26NFvQPPKihtwIAAUwACG1ldGhvZElkcQB+ABN4cHEAfgBec3EAfgAgAHNyABdzcGVjLmN2bGFzdC5DVkxGdW5jdGlvbi5Z1aiJh8hhAgAJTAAFYmxvY2txAH4ACkwADWRlY2xhcmF0aW9uSWRxAH4AE0wAEmZ1bmN0aW9uSWRlbnRpZmllcnEAfgAUTAAKcGFyYW1UeXBlc3EAfgAKTAAGcGFyYW1zcQB+AApMAAVyYW5nZXEAfgALTAAEcmV0c3QAIUxzcGVjL2N2bGFzdC9DVkxUeXBlJFB1cmVDVkxUeXBlO0wABXNjb3BlcQB+AAxMAA90eXBlRGVzY3JpcHRpb25xAH4AE3hwc3EAfgAaAAAAAncEAAAAAnNyAB9zcGVjLmN2bGFzdC5DVkxDbWQkU2ltcGxlJEhhdm9jQb7CD0w2gF0CAARMAAthc3N1bWluZ0V4cHEAfgAJTAAFcmFuZ2VxAH4AC0wABXNjb3BlcQB+AAxMAAd0YXJnZXRzcQB+AAp4cgAZc3BlYy5jdmxhc3QuQ1ZMQ21kJFNpbXBsZYD/kUsK5pNIAgAAeHIAEnNwZWMuY3ZsYXN0LkNWTENtZH1PtPZHk6iSAgAAeHBwc3EAfgAkc3EAfgAoAAAAHwAAAAdxAH4AKnNxAH4AKAAAAAQAAAAHc3EAfgAsc3EAfgAvc3EAfgAyzPGovHEAfgA1c3EAfgAaAAAAAncEAAAAAnEAfgBBc3IALnNwZWMuY3ZsYXN0LkNWTFNjb3BlJEl0ZW0kQ1ZMRnVuY3Rpb25TY29wZUl0ZW17W8hAYYNKOQIAAUkAB3Njb3BlSWR4cQB+AERzcQB+AKRzcQB+ABoAAAACdwQAAAACc3EAfgCocHEAfgCscQB+AK9zcQB+ABoAAAABdwQAAAABc3IAIXNwZWMuY3ZsYXN0LkNWTEV4cCRGaWVsZFNlbGVjdEV4cFM7gAF82lmuAgADTAAJZmllbGROYW1lcQB+ABNMAAlzdHJ1Y3RFeHBxAH4ACUwAA3RhZ3EAfgAVeHEAfgAYcQB+AIhzcgAgc3BlYy5jdmxhc3QuQ1ZMRXhwJEFycmF5RGVyZWZFeHDkJNvgbAhgBgIAA0wABWFycmF5cQB+AAlMAAVpbmRleHEAfgAJTAADdGFncQB+ABV4cQB+ABhzcQB+ALl0AAFtc3EAfgAcdAAMdGVzdENvbnRyYWN0cQB+AMBzcQB+ACAAcHNxAH4AJHNxAH4AKAAAABYAAAAHcQB+ACpzcQB+ACgAAAAKAAAAB3EAfgCvcHEAfgBQc3EAfgAgAHBzcQB+ACRzcQB+ACgAAAAYAAAAB3EAfgAqc3EAfgAoAAAACgAAAAdxAH4Ar3BzcgAlc3BlYy5jdmxhc3QuQ1ZMRXhwJENvbnN0YW50JE51bWJlckxpdABdlv4jnjYFAgADTAABbnQAFkxqYXZhL21hdGgvQmlnSW50ZWdlcjtMAAlwcmludEhpbnRxAH4AE0wAA3RhZ3EAfgAVeHIAG3NwZWMuY3ZsYXN0LkNWTEV4cCRDb25zdGFudLtVtKlnp5+bAgAAeHEAfgAYc3IAFGphdmEubWF0aC5CaWdJbnRlZ2VyjPyfH6k7+x0DAAZJAAhiaXRDb3VudEkACWJpdExlbmd0aEkAE2ZpcnN0Tm9uemVyb0J5dGVOdW1JAAxsb3dlc3RTZXRCaXRJAAZzaWdudW1bAAltYWduaXR1ZGV0AAJbQnhxAH4AM////////////////v////4AAAAAdXIAAltCrPMX+AYIVOACAAB4cAAAAAB4dAACMTBzcQB+ACAAcHNxAH4AJHNxAH4AKAAAABoAAAAHcQB+ACpzcQB+ACgAAAAZAAAAB3EAfgCvcHNxAH4AIABwc3EAfgAkc3EAfgAoAAAAGwAAAAdxAH4AKnNxAH4AKAAAAAoAAAAHcQB+AK9wc3EAfgAgAHBzcQB+ACRzcQB+ACgAAAAeAAAAB3EAfgAqc3EAfgAoAAAACgAAAAdxAH4Ar3B4c3IAKnNwZWMuY3ZsYXN0LkNWTENtZCRTaW1wbGUkQXNzdW1lQ21kJEFzc3VtZZguNQhltAhKAgAFWgAQaW52YXJpYW50UHJlQ29uZEwAC2Rlc2NyaXB0aW9ucQB+ABNMAANleHBxAH4ACUwABXJhbmdlcQB+AAtMAAVzY29wZXEAfgAMeHIAI3NwZWMuY3ZsYXN0LkNWTENtZCRTaW1wbGUkQXNzdW1lQ21kb17awtyOC4QCAAB4cQB+AKkAcHNyACFzcGVjLmN2bGFzdC5DVkxFeHAkUmVsb3BFeHAkRXFFeHBIDlG3n1bUygIAA0wAAWxxAH4ACUwAAXJxAH4ACUwAA3RhZ3EAfgAVeHIAG3NwZWMuY3ZsYXN0LkNWTEV4cCRSZWxvcEV4cNT+zURY77uiAgAAeHEAfgAYc3EAfgC5cQB+AIhzcQB+ALtzcQB+ALlxAH4AvnNxAH4AHHEAfgDAcQB+AMBzcQB+ACAAcHNxAH4AJHNxAH4AKAAAABgAAAAIcQB+ACpzcQB+ACgAAAAMAAAACHEAfgCvcHEAfgBQc3EAfgAgAHBzcQB+ACRzcQB+ACgAAAAaAAAACHEAfgAqc3EAfgAoAAAADAAAAAhxAH4Ar3BzcQB+AMlxAH4Az3EAfgDSc3EAfgAgAHBzcQB+ACRzcQB+ACgAAAAcAAAACHEAfgAqc3EAfgAoAAAAGwAAAAhxAH4Ar3BzcQB+ACAAcHNxAH4AJHNxAH4AKAAAAB0AAAAIcQB+ACpzcQB+ACgAAAAMAAAACHEAfgCvcHNxAH4AIABwc3EAfgAkc3EAfgAoAAAAIAAAAAhxAH4AKnNxAH4AKAAAAAwAAAAIcQB+AK9wc3IAL3NwZWMuY3ZsYXN0LkNWTEV4cCRSZWxvcEV4cCRBcml0aFJlbG9wRXhwJEd0RXhwiloskl81tasCAANMAAFscQB+AAlMAAFycQB+AAlMAAN0YWdxAH4AFXhyAClzcGVjLmN2bGFzdC5DVkxFeHAkUmVsb3BFeHAkQXJpdGhSZWxvcEV4cI7opCkt6stnAgAAeHEAfgDjc3EAfgAccQB+AB9xAH4AH3NxAH4AIABwc3EAfgAkc3EAfgAoAAAAJgAAAAhxAH4AKnNxAH4AKAAAACUAAAAIcQB+AK9wcQB+AFBzcQB+AMlzcQB+AM3///////////////7////+AAAAAXVxAH4A0AAAAAEDeHEAfgDSc3EAfgAgAHBzcQB+ACRzcQB+ACgAAAAqAAAACHEAfgAqc3EAfgAoAAAAKQAAAAhxAH4Ar3BzcQB+ACABcHNxAH4AJHNxAH4AKAAAACoAAAAIcQB+ACpzcQB+ACgAAAAlAAAACHEAfgCvcHNxAH4AIABwc3EAfgAkc3EAfgAoAAAAKwAAAAhxAH4AKnNxAH4AKAAAAAwAAAAIcQB+AK9wc3EAfgAkc3EAfgAoAAAALAAAAAhxAH4AKnNxAH4AKAAAAAQAAAAIcQB+AK94cQB+AF5zcQB+AKFxAH4AXnNxAH4AGgAAAAJ3BAAAAAJzcgAvc3BlYy5jdmxhc3QuQ1ZMVHlwZSRQdXJlQ1ZMVHlwZSRQcmltaXRpdmUkVUludEu5C5qOKRJGKQIAAkkACGJpdFdpZHRoSQABa3hyAClzcGVjLmN2bGFzdC5DVkxUeXBlJFB1cmVDVkxUeXBlJFByaW1pdGl2ZQqb2/80fsI7AgAAeHIAH3NwZWMuY3ZsYXN0LkNWTFR5cGUkUHVyZUNWTFR5cGX9BrQWU7YosQIAAHhxAH4AmQAAAQAAAAEAc3IAJnNwZWMuY3ZsYXN0LkNWTFR5cGUkUHVyZUNWTFR5cGUkU3RydWN0NUmhFGkTOYMCAAJMAAZmaWVsZHNxAH4ACkwABG5hbWVxAH4AE3hxAH4BHHNxAH4AGgAAAAd3BAAAAAdzcgAyc3BlYy5jdmxhc3QuQ1ZMVHlwZSRQdXJlQ1ZMVHlwZSRTdHJ1Y3QkU3RydWN0RW50cnkzHxoz/bbqDQIAAkwAB2N2bFR5cGVxAH4ApUwACWZpZWxkTmFtZXEAfgATeHBzcQB+ARoAAAEAAAABAHEAfgAfc3EAfgEhc3IAO3NwZWMuY3ZsYXN0LkNWTFR5cGUkUHVyZUNWTFR5cGUkUHJpbWl0aXZlJEFjY291bnRJZGVudGlmaWVyIEUKRPwCm3ECAAB4cQB+ARtxAH4AfnNxAH4BIXNxAH4BGgAAAAgAAAAIcQB+AIJzcQB+ASFzcQB+ARoAAAAIAAAACHEAfgCFc3EAfgEhc3IALnNwZWMuY3ZsYXN0LkNWTFR5cGUkUHVyZUNWTFR5cGUkUHJpbWl0aXZlJEJvb2zbq8Fo2DCyzwIAAHhxAH4BG3EAfgCIc3EAfgEhc3EAfgEaAAABAAAAAQBxAH4AjHNxAH4BIXEAfgEtcQB+AI94cQB+AJB4c3EAfgAaAAAAAncEAAAAAnNyABRzcGVjLmN2bGFzdC5DVkxQYXJhbZUgQywsLU7ZAgAETAACaWRxAH4AE0wACm9yaWdpbmFsSWRxAH4AE0wABXJhbmdlcQB+AAtMAAR0eXBlcQB+AKV4cHEAfgAfcQB+AB9zcQB+ACRzcQB+ACgAAAAaAAAABnEAfgAqc3EAfgAoAAAAFAAAAAZxAH4BHXNxAH4BMnEAfgBTcQB+AFNzcQB+ACRzcQB+ACgAAAAxAAAABnEAfgAqc3EAfgAoAAAAHAAAAAZxAH4BH3hzcQB+ACRzcQB+ACgAAAABAAAACXEAfgAqc3EAfgAoAAAAAAAAAAZzcgAkc3BlYy5jdmxhc3QuQ1ZMVHlwZSRQdXJlQ1ZMVHlwZSRWb2lki6Bk1Y34dWcCAAB4cQB+ARxxAH4Ar3QADENWTCBmdW5jdGlvbgAAAAN4c3EAfgAaAAAAAXcEAAAAAXNxAH4AuXEAfgCIc3EAfgC7c3EAfgC5cQB+AL5zcQB+ABxxAH4AwHEAfgDAcQB+AMFxAH4AUHEAfgDFcQB+AMxxAH4A13EAfgDbeHNxAH4A3wBwc3EAfgDic3EAfgC5cQB+AIhzcQB+ALtzcQB+ALlxAH4AvnNxAH4AHHEAfgDAcQB+AMBxAH4A6XEAfgBQcQB+AO1xAH4A8XEAfgD2cQB+APpzcQB+AP5zcQB+ABxxAH4AH3EAfgAfcQB+AQJxAH4AUHEAfgEGcQB+AQ1xAH4BEXEAfgEVcQB+AK94cQB+AF5zcQB+AKFxAH4AXnNxAH4AGgAAAAJ3BAAAAAJxAH4BHXEAfgEfeHNxAH4AGgAAAAJ3BAAAAAJxAH4BM3EAfgE3eHEAfgE7cQB+AT9xAH4Ar3EAfgFAcQB+AGBxAH4ALnEAfgE/cHNxAH4AGgAAAAJ3BAAAAAJxAH4AZ3EAfgBweHEAfgCRcQB+AC5xAH4AlXBzcgAWc3BlYy5DVkwkRXh0ZXJuYWxFeGFjdOcwmTuU10E4AgACTAAKc2lnaGFzaEludHQAEExldm0vU2lnaGFzaEludDtMAAlzaWduYXR1cmV0AC9Mc3BlYy9jdmxhc3QvUXVhbGlmaWVkTWV0aG9kUGFyYW1ldGVyU2lnbmF0dXJlO3hwc3IADmV2bS5TaWdoYXNoSW50PbtqepD4ptUCAAFMAAFucQB+AMp4cHNxAH4Azf///////////////v////4AAAABdXEAfgDQAAAABIxDpEF4c3IAN3NwZWMuY3ZsYXN0LlF1YWxpZmllZE1ldGhvZFNpZ25hdHVyZSRRdWFsaWZpZWRNZXRob2RTaWcYfUy0bR1s9QIAA0wABnBhcmFtc3EAfgAKTAATcXVhbGlmaWVkTWV0aG9kTmFtZXQAKExzcGVjL2N2bGFzdC9Db250cmFjdEZ1bmN0aW9uSWRlbnRpZmllcjtMAANyZXNxAH4ACnhwcQB+AGNzcgAdc3BlYy5jdmxhc3QuUXVhbGlmaWVkRnVuY3Rpb27lKUzy5DlRgwIAAkwABGhvc3R0AB5Mc3BlYy9jdmxhc3QvU29saWRpdHlDb250cmFjdDtMAAhtZXRob2RJZHEAfgATeHBzcgAcc3BlYy5jdmxhc3QuU29saWRpdHlDb250cmFjdCNpfXcagT2iAgABTAAEbmFtZXEAfgATeHB0AAxUZXN0Q29udHJhY3R0AAd3b3JrT25TcQB+ADw="}
		LabelCmd "Inline CVL/Ghost Function 'workOnSCVL(x,s)'"
		JumpCmd 3_0_0_1_0_0
	}
	Block 3_0_0_1_0_0 Succ [4_0_0_0_0_0] {
		AnnotationCmd:125 JSON{"key":{"name":"tac.decompiler.call-end","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.StartBranchSnippet","branchIndex":3,"branchSource":{"range":{"specFile":"TestContract.sol","start":{"line":16,"charByteOffset":8},"end":{"line":16,"charByteOffset":29}},"content":"this.workOnS(x, m[0])"}}}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.EndBranchSnippet","branchIndex":3}}
		AnnotationCmd:125 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":237,"bytecodeCount":7,"sources":[{"source":0,"begin":282,"end":303},{"source":0,"begin":235,"end":310}]}}
		AnnotationCmd:159 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"f4132f73f6fc0b565e6354058894661c6afe16981ce8b67d4c700ae0547e6bb6","pc":85,"bytecodeCount":2,"sources":[{"source":0,"begin":235,"end":310}]}}
		AssignExpCmd:159 lastHasThrown!!103:41 false
		AssignExpCmd:159 lastReverted:7 false
		AnnotationCmd:159 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:105 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.HaltSnippet.Return","range":{"specFile":"TestContract.sol","start":{"line":15,"charByteOffset":4},"end":{"line":17,"charByteOffset":5}}}}
		LabelCmd:105 "End procedure TestContract-workOnSExt(uint256)"
		AnnotationCmd:105 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":{"callee":{"contractId":"ce4604a0000000000000000000000001","sigHash":{"n":"2f0949c5"},"attr":{"#class":"scene.MethodAttribute.Common"}},"calleeId":1}}
	}
	Block 4_0_0_0_0_0 Succ [] {
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule"}},{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.NonTACKeywordEntry","name":"lastStorage"}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AnnotationCmd:105 JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":20}
		AnnotationCmd:160 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Assert","range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":18,"charByteOffset":4},"end":{"line":18,"charByteOffset":32}},"exp":{"#class":"spec.cvlast.CVLExp.FieldSelectExp","structExp":{"#class":"spec.cvlast.CVLExp.ArrayDerefExp","array":{"#class":"spec.cvlast.CVLExp.FieldSelectExp","structExp":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"testContract","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":1}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.CodeContract","name":{"name":"TestContract"}},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":18,"charByteOffset":11},"end":{"line":18,"charByteOffset":23}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.CVLExp$VariableExp$ContractInstanceId","instanceId":"ce4604a0000000000000000000000001"}},"twoStateIndex":"NEITHER"},"fieldName":"m","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":1}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.VM","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMMappingDescriptor","keyType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"valueType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.EVMStructDescriptor","canonicalId":"TestContract.sol|TestContract.Simple","location":null,"fields":[{"fieldName":"x","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"fieldName":"y","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}},{"fieldName":"z1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8}},{"fieldName":"z2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8}},{"fieldName":"b1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}},{"fieldName":"x2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"fieldName":"b2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}}],"name":"TestContract.Simple"},"location":null},"context":{"#class":"spec.cvlast.typedescriptors.FromVMContext.StateValue"}},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":18,"charByteOffset":11},"end":{"line":18,"charByteOffset":25}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.StorageAccessMarker"}}},"index":{"#class":"spec.cvlast.CVLExp.Constant.NumberLit","n":"0","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":1}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral","n":"0"},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":18,"charByteOffset":26},"end":{"line":18,"charByteOffset":27}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":1}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.VM","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMStructDescriptor","canonicalId":"TestContract.sol|TestContract.Simple","location":null,"fields":[{"fieldName":"x","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"fieldName":"y","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.address"}},{"fieldName":"z1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8}},{"fieldName":"z2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":8}},{"fieldName":"b1","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}},{"fieldName":"x2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"fieldName":"b2","fieldType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"}}],"name":"TestContract.Simple"},"context":{"#class":"spec.cvlast.typedescriptors.FromVMContext.StateValue"}},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":18,"charByteOffset":11},"end":{"line":18,"charByteOffset":28}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.StorageAccessMarker"}}},"fieldName":"b1","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":1}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.VM","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$bool"},"context":{"#class":"spec.cvlast.typedescriptors.FromVMContext.StateValue"}},"range":{"#class":"utils.Range.Range","specFile":"test.spec","start":{"line":18,"charByteOffset":11},"end":{"line":18,"charByteOffset":31}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.StorageAccessMarker"}}},"description":null,"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":1}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssignExpCmd:161 I104 0x0
		AssertCmd:162 true "sanity bounds check on cvl to vm encoding (unsigned int elements of a user array) of %1$s failed"
		AssignExpCmd:163 R105:21 Apply(hash_3_keccak:bif Apply(skey_basic:bif 0x40) Apply(skey_basic:bif 0x0) Apply(skey_basic:bif 0x0))
		AssignExpCmd:163 R106:21 Apply(skey_add:bif R105:21 0x1)
		AssignExpCmd:164 R107:21 AnnotationExp(Select(CANON53!!93:153 R106:165 ) JSON{"key":{"name":"tac.storage.access-paths","type":"analysis.storage.StorageAnalysisResult$AccessPaths","erasureStrategy":"Canonical"},"value":{"paths":[{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.StructAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.MapAccess","base":{"#class":"analysis.storage.StorageAnalysis.AnalysisPath.Root","slot":"0"},"key":{"#class":"vc.data.TACSymbol.Const","value":"0"},"baseSlot":{"#class":"vc.data.TACSymbol.Const","value":"0"},"hashResult":{"#class":"vc.data.TACSymbol.Const","value":"0"}},"offset":{"#class":"analysis.storage.StorageAnalysis.Offset.Bytes","numBytes":"36"}}]}})
		AssignExpCmd:163 B109 LNot(Eq(R107:21 0x0 ) )
		AnnotationCmd:163 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.DirectStorageLoad","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"B109","tag":{"#class":"tac.Tag.Bool"},"callIndex":0},"displayPath":{"#class":"analysis.storage.DisplayPath.FieldAccess","field":"b1","base":{"#class":"analysis.storage.DisplayPath.MapAccess","key":{"#class":"vc.data.TACSymbol.Const","value":"0"},"keyTyp":{"#class":"tac.TACStorageType.IntegralType","typeLabel":"uint256","numBytes":"20","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"lowerBound":null,"upperBound":null},"base":{"#class":"analysis.storage.DisplayPath.Root","name":"m"}}},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.bool"},"contractInstance":"ce4604a0000000000000000000000001","range":{"specFile":"test.spec","start":{"line":18,"charByteOffset":11},"end":{"line":18,"charByteOffset":31}}}}
		AssertCmd:166 B109 "testContract.m[0].b1"
	}
}
Axioms {
}
Metas {
  "0": [
    {
      "key": {
        "name": "tac.is.memory",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "tacM",
        "maybeTACKeywordOrdinal": 1
      }
    },
    {
      "key": {
        "name": "tac.memory.partition",
        "type": "analysis.pta.abi.UnindexedPartition",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "id": 0
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
        "name": "tacReturndata",
        "maybeTACKeywordOrdinal": 19
      }
    },
    {
      "key": {
        "name": "tac.is.returndata",
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
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "tacM0x40",
        "maybeTACKeywordOrdinal": 39
      }
    },
    {
      "key": {
        "name": "tac.is.reserved.memory.slot.var",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "40"
    }
  ],
  "3": [
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
  "4": [
    {
      "key": {
        "name": "tac.immutable.array",
        "type": "vc.data.ImmutableBound",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "sym": {
          "#class": "vc.data.TACSymbol.Var.Full",
          "namePrefix": "tacCalldatasize",
          "tag": {
            "#class": "tac.Tag.Bit256"
          },
          "callIndex": 1,
          "meta": [
            {
              "key": {
                "name": "Tac.symbol.keyword",
                "type": "vc.data.TACSymbol$Var$KeywordEntry",
                "erasureStrategy": "Canonical"
              },
              "value": {
                "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                "name": "tacCalldatasize",
                "maybeTACKeywordOrdinal": 12
              }
            }
          ]
        }
      }
    },
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "tacCalldatabuf",
        "maybeTACKeywordOrdinal": 15
      }
    },
    {
      "key": {
        "name": "tac.wordmap-key",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "4"
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Split",
        "idx": "4"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.calldata.offset",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "4"
    },
    {
      "key": {
        "name": "tac.is.calldata",
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
        "name": "tac.is.memory",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "tacM",
        "maybeTACKeywordOrdinal": 1
      }
    },
    {
      "key": {
        "name": "tac.memory.partition",
        "type": "analysis.pta.abi.UnindexedPartition",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "id": 2
      }
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
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "tacAddress",
        "maybeTACKeywordOrdinal": 22
      }
    },
    {
      "key": {
        "name": "tac.env.known-bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 160
    }
  ],
  "7": [
    {
      "key": {
        "name": "tac.last.reverted",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Rule"
      }
    },
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.NonTACKeywordEntry",
        "name": "lastReverted"
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
      "value": "lastReverted"
    }
  ],
  "8": [
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
  "9": [
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
  "10": [
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
            "offset": "0"
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
        "#class": "vc.data.ScalarizationSort.UnscalarizedBuffer"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
        "bitwidth": 256
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
        "offset": "0"
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
  "11": [
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
        "start": 0
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 160
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.address"
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
  "12": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "tacCalldatasize",
        "maybeTACKeywordOrdinal": 12
      }
    }
  ],
  "13": [
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Rule"
      }
    },
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.NonTACKeywordEntry",
        "name": "calledContract"
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
      "value": "calledContract"
    }
  ],
  "14": [
    {
      "key": {
        "name": "tac.is.memory",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "tacM",
        "maybeTACKeywordOrdinal": 1
      }
    },
    {
      "key": {
        "name": "tac.memory.partition",
        "type": "analysis.pta.abi.UnindexedPartition",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "id": 3
      }
    }
  ],
  "15": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "tacBalance",
        "maybeTACKeywordOrdinal": 23
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
    }
  ],
  "16": [
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
        "start": 160
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
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
        "bitwidth": 8
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
  "17": [
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
        "start": 168
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
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
        "bitwidth": 8
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
  "18": [
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
  "19": [
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
            "offset": "2"
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
        "#class": "vc.data.ScalarizationSort.UnscalarizedBuffer"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.slot.type",
        "type": "spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK",
        "bitwidth": 256
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
        "offset": "2"
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
  "20": [
    {
      "key": {
        "name": "tac.immutable.array",
        "type": "vc.data.ImmutableBound",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "sym": {
          "#class": "vc.data.TACSymbol.Var.Full",
          "namePrefix": "tacCalldatasize",
          "tag": {
            "#class": "tac.Tag.Bit256"
          },
          "callIndex": 1,
          "meta": [
            {
              "key": {
                "name": "Tac.symbol.keyword",
                "type": "vc.data.TACSymbol$Var$KeywordEntry",
                "erasureStrategy": "Canonical"
              },
              "value": {
                "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                "name": "tacCalldatasize",
                "maybeTACKeywordOrdinal": 12
              }
            }
          ]
        }
      }
    },
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "tacCalldatabuf",
        "maybeTACKeywordOrdinal": 15
      }
    },
    {
      "key": {
        "name": "tac.is.calldata",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "21": [
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
  "22": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1002
    }
  ],
  "23": [
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
  "24": [
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
  "25": [
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
  "26": [
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
  "27": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1021
    }
  ],
  "28": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1018
    }
  ],
  "29": [
    {
      "key": {
        "name": "tac.decomp-inscalar.sort",
        "type": "tac.DecomposedInputScalarSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "tac.DecomposedInputScalarSort.Simple",
        "byteOffset": "4"
      }
    }
  ],
  "30": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1009
    }
  ],
  "31": [
    {
      "key": {
        "name": "tac.decomp-inscalar.sort",
        "type": "tac.DecomposedInputScalarSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "tac.DecomposedInputScalarSort.Simple",
        "byteOffset": "24"
      }
    }
  ],
  "32": [
    {
      "key": {
        "name": "tac.decomp-inscalar.sort",
        "type": "tac.DecomposedInputScalarSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "tac.DecomposedInputScalarSort.Simple",
        "byteOffset": "44"
      }
    }
  ],
  "33": [
    {
      "key": {
        "name": "tac.decomp-inscalar.sort",
        "type": "tac.DecomposedInputScalarSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "tac.DecomposedInputScalarSort.Simple",
        "byteOffset": "64"
      }
    }
  ],
  "34": [
    {
      "key": {
        "name": "tac.decomp-inscalar.sort",
        "type": "tac.DecomposedInputScalarSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "tac.DecomposedInputScalarSort.Simple",
        "byteOffset": "84"
      }
    }
  ],
  "35": [
    {
      "key": {
        "name": "tac.decomp-inscalar.sort",
        "type": "tac.DecomposedInputScalarSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "tac.DecomposedInputScalarSort.Simple",
        "byteOffset": "a4"
      }
    }
  ],
  "36": [
    {
      "key": {
        "name": "tac.decomp-inscalar.sort",
        "type": "tac.DecomposedInputScalarSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "tac.DecomposedInputScalarSort.Simple",
        "byteOffset": "c4"
      }
    }
  ],
  "37": [
    {
      "key": {
        "name": "tac.decomp-inscalar.sort",
        "type": "tac.DecomposedInputScalarSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "tac.DecomposedInputScalarSort.Simple",
        "byteOffset": "e4"
      }
    }
  ],
  "38": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1017
    }
  ],
  "39": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1016
    }
  ],
  "40": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1012
    }
  ],
  "41": [
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Rule"
      }
    },
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.NonTACKeywordEntry",
        "name": "lastHasThrown"
      }
    },
    {
      "key": {
        "name": "tac.last.has.thrown",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
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
      "value": "lastHasThrown"
    }
  ],
  "42": [
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
  "43": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.FieldAccess",
            "field": "x",
            "base": {
              "#class": "analysis.storage.DisplayPath.MapAccess",
              "key": {
                "#class": "vc.data.TACSymbol.Const",
                "value": "0"
              },
              "keyTyp": {
                "#class": "tac.TACStorageType.IntegralType",
                "typeLabel": "uint256",
                "numBytes": "20",
                "descriptor": {
                  "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                  "bitwidth": 256
                },
                "lowerBound": null,
                "upperBound": null
              },
              "base": {
                "#class": "analysis.storage.DisplayPath.Root",
                "name": "m"
              }
            }
          }
        ]
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
                "#class": "vc.data.TACSymbol.Const",
                "value": "0"
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "CANON48",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 1,
                "meta": [
                  {
                    "key": {
                      "name": "tac.is-temp-var",
                      "type": "tac.MetaMap$Companion$NothingValue",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                    }
                  }
                ]
              },
              "hashResult": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "CANON45",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 1,
                "meta": [
                  {
                    "key": {
                      "name": "tac.is-temp-var",
                      "type": "tac.MetaMap$Companion$NothingValue",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                    }
                  }
                ]
              }
            },
            "offset": {
              "#class": "analysis.storage.StorageAnalysis.Offset.Words",
              "numWords": "0"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1009
    }
  ],
  "44": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.FieldAccess",
            "field": "y",
            "base": {
              "#class": "analysis.storage.DisplayPath.MapAccess",
              "key": {
                "#class": "vc.data.TACSymbol.Const",
                "value": "0"
              },
              "keyTyp": {
                "#class": "tac.TACStorageType.IntegralType",
                "typeLabel": "uint256",
                "numBytes": "20",
                "descriptor": {
                  "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                  "bitwidth": 256
                },
                "lowerBound": null,
                "upperBound": null
              },
              "base": {
                "#class": "analysis.storage.DisplayPath.Root",
                "name": "m"
              }
            }
          }
        ]
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
                "#class": "vc.data.TACSymbol.Const",
                "value": "0"
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "CANON48",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 1,
                "meta": [
                  {
                    "key": {
                      "name": "tac.is-temp-var",
                      "type": "tac.MetaMap$Companion$NothingValue",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                    }
                  }
                ]
              },
              "hashResult": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "CANON45",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 1,
                "meta": [
                  {
                    "key": {
                      "name": "tac.is-temp-var",
                      "type": "tac.MetaMap$Companion$NothingValue",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                    }
                  }
                ]
              }
            },
            "offset": {
              "#class": "analysis.storage.StorageAnalysis.Offset.Bytes",
              "numBytes": "20"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1009
    }
  ],
  "45": [
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
            "offset": "3"
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
        "offset": "3"
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
  "46": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "env",
          "fields": [
            {
              "fieldName": "msg",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "msg",
                "fields": [
                  {
                    "fieldName": "sender",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "value",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "tx",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "tx",
                "fields": [
                  {
                    "fieldName": "origin",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "block",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "block",
                "fields": [
                  {
                    "fieldName": "basefee",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "blobbasefee",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "coinbase",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "difficulty",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "gaslimit",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "number",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "timestamp",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "msg",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "msg",
              "fields": [
                {
                  "fieldName": "sender",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "value",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                }
              ]
            }
          },
          {
            "fieldName": "value",
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
            "line": 14,
            "charByteOffset": 4
          },
          "end": {
            "line": 14,
            "charByteOffset": 10
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
      "value": "e.msg.value"
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
          "name": "env",
          "fields": [
            {
              "fieldName": "msg",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "msg",
                "fields": [
                  {
                    "fieldName": "sender",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "value",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "tx",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "tx",
                "fields": [
                  {
                    "fieldName": "origin",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "block",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "block",
                "fields": [
                  {
                    "fieldName": "basefee",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "blobbasefee",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "coinbase",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "difficulty",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "gaslimit",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "number",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "timestamp",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "tx",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "tx",
              "fields": [
                {
                  "fieldName": "origin",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                }
              ]
            }
          },
          {
            "fieldName": "origin",
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
            "line": 14,
            "charByteOffset": 4
          },
          "end": {
            "line": 14,
            "charByteOffset": 10
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
      "value": "e.tx.origin"
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
          "name": "env",
          "fields": [
            {
              "fieldName": "msg",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "msg",
                "fields": [
                  {
                    "fieldName": "sender",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "value",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "tx",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "tx",
                "fields": [
                  {
                    "fieldName": "origin",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "block",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "block",
                "fields": [
                  {
                    "fieldName": "basefee",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "blobbasefee",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "coinbase",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "difficulty",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "gaslimit",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "number",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "timestamp",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "block",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "block",
              "fields": [
                {
                  "fieldName": "basefee",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "blobbasefee",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "coinbase",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "difficulty",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "gaslimit",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "number",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "timestamp",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                }
              ]
            }
          },
          {
            "fieldName": "basefee",
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
            "line": 14,
            "charByteOffset": 4
          },
          "end": {
            "line": 14,
            "charByteOffset": 10
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
      "value": "e.block.basefee"
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
          "name": "env",
          "fields": [
            {
              "fieldName": "msg",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "msg",
                "fields": [
                  {
                    "fieldName": "sender",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "value",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "tx",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "tx",
                "fields": [
                  {
                    "fieldName": "origin",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "block",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "block",
                "fields": [
                  {
                    "fieldName": "basefee",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "blobbasefee",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "coinbase",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "difficulty",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "gaslimit",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "number",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "timestamp",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "block",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "block",
              "fields": [
                {
                  "fieldName": "basefee",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "blobbasefee",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "coinbase",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "difficulty",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "gaslimit",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "number",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "timestamp",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                }
              ]
            }
          },
          {
            "fieldName": "blobbasefee",
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
            "line": 14,
            "charByteOffset": 4
          },
          "end": {
            "line": 14,
            "charByteOffset": 10
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
      "value": "e.block.blobbasefee"
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
          "name": "env",
          "fields": [
            {
              "fieldName": "msg",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "msg",
                "fields": [
                  {
                    "fieldName": "sender",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "value",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "tx",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "tx",
                "fields": [
                  {
                    "fieldName": "origin",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "block",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "block",
                "fields": [
                  {
                    "fieldName": "basefee",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "blobbasefee",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "coinbase",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "difficulty",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "gaslimit",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "number",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "timestamp",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "block",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "block",
              "fields": [
                {
                  "fieldName": "basefee",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "blobbasefee",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "coinbase",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "difficulty",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "gaslimit",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "number",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "timestamp",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                }
              ]
            }
          },
          {
            "fieldName": "coinbase",
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
            "line": 14,
            "charByteOffset": 4
          },
          "end": {
            "line": 14,
            "charByteOffset": 10
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
      "value": "e.block.coinbase"
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
          "name": "env",
          "fields": [
            {
              "fieldName": "msg",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "msg",
                "fields": [
                  {
                    "fieldName": "sender",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "value",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "tx",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "tx",
                "fields": [
                  {
                    "fieldName": "origin",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "block",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "block",
                "fields": [
                  {
                    "fieldName": "basefee",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "blobbasefee",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "coinbase",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "difficulty",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "gaslimit",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "number",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "timestamp",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "block",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "block",
              "fields": [
                {
                  "fieldName": "basefee",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "blobbasefee",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "coinbase",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "difficulty",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "gaslimit",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "number",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "timestamp",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                }
              ]
            }
          },
          {
            "fieldName": "difficulty",
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
            "line": 14,
            "charByteOffset": 4
          },
          "end": {
            "line": 14,
            "charByteOffset": 10
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
      "value": "e.block.difficulty"
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
          "name": "env",
          "fields": [
            {
              "fieldName": "msg",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "msg",
                "fields": [
                  {
                    "fieldName": "sender",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "value",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "tx",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "tx",
                "fields": [
                  {
                    "fieldName": "origin",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "block",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "block",
                "fields": [
                  {
                    "fieldName": "basefee",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "blobbasefee",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "coinbase",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "difficulty",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "gaslimit",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "number",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "timestamp",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "block",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "block",
              "fields": [
                {
                  "fieldName": "basefee",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "blobbasefee",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "coinbase",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "difficulty",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "gaslimit",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "number",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "timestamp",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                }
              ]
            }
          },
          {
            "fieldName": "gaslimit",
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
            "line": 14,
            "charByteOffset": 4
          },
          "end": {
            "line": 14,
            "charByteOffset": 10
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
      "value": "e.block.gaslimit"
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
          "name": "env",
          "fields": [
            {
              "fieldName": "msg",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "msg",
                "fields": [
                  {
                    "fieldName": "sender",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "value",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "tx",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "tx",
                "fields": [
                  {
                    "fieldName": "origin",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "block",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "block",
                "fields": [
                  {
                    "fieldName": "basefee",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "blobbasefee",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "coinbase",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "difficulty",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "gaslimit",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "number",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "timestamp",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "block",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "block",
              "fields": [
                {
                  "fieldName": "basefee",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "blobbasefee",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "coinbase",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "difficulty",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "gaslimit",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "number",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "timestamp",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                }
              ]
            }
          },
          {
            "fieldName": "number",
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
            "line": 14,
            "charByteOffset": 4
          },
          "end": {
            "line": 14,
            "charByteOffset": 10
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
      "value": "e.block.number"
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
          "name": "env",
          "fields": [
            {
              "fieldName": "msg",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "msg",
                "fields": [
                  {
                    "fieldName": "sender",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "value",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "tx",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "tx",
                "fields": [
                  {
                    "fieldName": "origin",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "block",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "block",
                "fields": [
                  {
                    "fieldName": "basefee",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "blobbasefee",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "coinbase",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "difficulty",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "gaslimit",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "number",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "timestamp",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "block",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "block",
              "fields": [
                {
                  "fieldName": "basefee",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "blobbasefee",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "coinbase",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "difficulty",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "gaslimit",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "number",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                },
                {
                  "fieldName": "timestamp",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                }
              ]
            }
          },
          {
            "fieldName": "timestamp",
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
            "line": 14,
            "charByteOffset": 4
          },
          "end": {
            "line": 14,
            "charByteOffset": 10
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
      "value": "e.block.timestamp"
    }
  ],
  "55": [
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
            "line": 6,
            "charByteOffset": 20
          },
          "end": {
            "line": 6,
            "charByteOffset": 26
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
  "56": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
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
        },
        "fields": [
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
            "line": 6,
            "charByteOffset": 28
          },
          "end": {
            "line": 6,
            "charByteOffset": 49
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
      "value": "s.x"
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
        },
        "fields": [
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
            "line": 6,
            "charByteOffset": 28
          },
          "end": {
            "line": 6,
            "charByteOffset": 49
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
      "value": "s.y"
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
        },
        "fields": [
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
            "line": 6,
            "charByteOffset": 28
          },
          "end": {
            "line": 6,
            "charByteOffset": 49
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
      "value": "s.z1"
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
        },
        "fields": [
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
            "line": 6,
            "charByteOffset": 28
          },
          "end": {
            "line": 6,
            "charByteOffset": 49
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
      "value": "s.z2"
    }
  ],
  "60": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
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
        },
        "fields": [
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
            "line": 6,
            "charByteOffset": 28
          },
          "end": {
            "line": 6,
            "charByteOffset": 49
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
      "value": "s.b1"
    }
  ],
  "61": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
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
        },
        "fields": [
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
            "line": 6,
            "charByteOffset": 28
          },
          "end": {
            "line": 6,
            "charByteOffset": 49
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
      "value": "s.x2"
    }
  ],
  "62": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
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
        },
        "fields": [
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
            "line": 6,
            "charByteOffset": 28
          },
          "end": {
            "line": 6,
            "charByteOffset": 49
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
      "value": "s.b2"
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
                "namePrefix": "CANON74",
                "tag": {
                  "#class": "tac.Tag.Int"
                },
                "callIndex": 0
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
                "namePrefix": "CANON80",
                "tag": {
                  "#class": "tac.Tag.Int"
                },
                "callIndex": 0
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
  "65": [
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    }
  ],
  "66": [
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
                "namePrefix": "CANON89",
                "tag": {
                  "#class": "tac.Tag.Int"
                },
                "callIndex": 0
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
  "67": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.FieldAccess",
            "field": "x2",
            "base": {
              "#class": "analysis.storage.DisplayPath.MapAccess",
              "key": {
                "#class": "vc.data.TACSymbol.Const",
                "value": "0"
              },
              "keyTyp": {
                "#class": "tac.TACStorageType.IntegralType",
                "typeLabel": "uint256",
                "numBytes": "20",
                "descriptor": {
                  "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                  "bitwidth": 256
                },
                "lowerBound": null,
                "upperBound": null
              },
              "base": {
                "#class": "analysis.storage.DisplayPath.Root",
                "name": "m"
              }
            }
          }
        ]
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
                "#class": "vc.data.TACSymbol.Const",
                "value": "0"
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "CANON48",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 1,
                "meta": [
                  {
                    "key": {
                      "name": "tac.is-temp-var",
                      "type": "tac.MetaMap$Companion$NothingValue",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                    }
                  }
                ]
              },
              "hashResult": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "CANON45",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 1,
                "meta": [
                  {
                    "key": {
                      "name": "tac.is-temp-var",
                      "type": "tac.MetaMap$Companion$NothingValue",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                    }
                  }
                ]
              }
            },
            "offset": {
              "#class": "analysis.storage.StorageAnalysis.Offset.Words",
              "numWords": "2"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1009
    }
  ],
  "68": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.FieldAccess",
            "field": "b2",
            "base": {
              "#class": "analysis.storage.DisplayPath.MapAccess",
              "key": {
                "#class": "vc.data.TACSymbol.Const",
                "value": "0"
              },
              "keyTyp": {
                "#class": "tac.TACStorageType.IntegralType",
                "typeLabel": "uint256",
                "numBytes": "20",
                "descriptor": {
                  "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                  "bitwidth": 256
                },
                "lowerBound": null,
                "upperBound": null
              },
              "base": {
                "#class": "analysis.storage.DisplayPath.Root",
                "name": "m"
              }
            }
          }
        ]
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
                "#class": "vc.data.TACSymbol.Const",
                "value": "0"
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "CANON48",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 1,
                "meta": [
                  {
                    "key": {
                      "name": "tac.is-temp-var",
                      "type": "tac.MetaMap$Companion$NothingValue",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                    }
                  }
                ]
              },
              "hashResult": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "CANON45",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 1,
                "meta": [
                  {
                    "key": {
                      "name": "tac.is-temp-var",
                      "type": "tac.MetaMap$Companion$NothingValue",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                    }
                  }
                ]
              }
            },
            "offset": {
              "#class": "analysis.storage.StorageAnalysis.Offset.Bytes",
              "numBytes": "60"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1009
    }
  ],
  "69": [
    {
      "key": {
        "name": "cvl.def.site",
        "type": "spec.CVLDefinitionSite",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "spec.CVLDefinitionSite.Rule"
      }
    },
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.NonTACKeywordEntry",
        "name": "executingContract"
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
      "value": "executingContract"
    }
  ],
  "70": [
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
  "71": [
    {
      "key": {
        "name": "cvl.struct.path",
        "type": "spec.cvlast.CVLStructPathNode",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "rootStructType": {
          "name": "env",
          "fields": [
            {
              "fieldName": "msg",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "msg",
                "fields": [
                  {
                    "fieldName": "sender",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "value",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "tx",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "tx",
                "fields": [
                  {
                    "fieldName": "origin",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  }
                ]
              }
            },
            {
              "fieldName": "block",
              "cvlType": {
                "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
                "name": "block",
                "fields": [
                  {
                    "fieldName": "basefee",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "blobbasefee",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "coinbase",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                    }
                  },
                  {
                    "fieldName": "difficulty",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "gaslimit",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "number",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  },
                  {
                    "fieldName": "timestamp",
                    "cvlType": {
                      "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                      "k": 256
                    }
                  }
                ]
              }
            }
          ]
        },
        "fields": [
          {
            "fieldName": "msg",
            "cvlType": {
              "#class": "spec.cvlast.CVLType.PureCVLType.Struct",
              "name": "msg",
              "fields": [
                {
                  "fieldName": "sender",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"
                  }
                },
                {
                  "fieldName": "value",
                  "cvlType": {
                    "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
                    "k": 256
                  }
                }
              ]
            }
          },
          {
            "fieldName": "sender",
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
            "line": 14,
            "charByteOffset": 4
          },
          "end": {
            "line": 14,
            "charByteOffset": 10
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
      "value": "e.msg.sender"
    }
  ],
  "72": [
    {
      "key": {
        "name": "tac.is.memory",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "tacM",
        "maybeTACKeywordOrdinal": 1
      }
    },
    {
      "key": {
        "name": "tacsimplesimple.havocme",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "tac.memory.partition",
        "type": "analysis.pta.abi.UnindexedPartition",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "id": 0
      }
    }
  ],
  "73": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "tacSighash",
        "maybeTACKeywordOrdinal": 6
      }
    }
  ],
  "74": [
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
            "line": 11,
            "charByteOffset": 18
          },
          "end": {
            "line": 11,
            "charByteOffset": 24
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
  "75": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 0
    }
  ],
  "76": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1
    }
  ],
  "77": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 2
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
  "79": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 3
    }
  ],
  "80": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 4
    }
  ],
  "81": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 5
    }
  ],
  "82": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 6
    }
  ],
  "83": [
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
  "84": [
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
  "85": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 7
    }
  ],
  "86": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 8
    }
  ],
  "87": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 9
    }
  ],
  "88": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 10
    }
  ],
  "89": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 11
    }
  ],
  "90": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 12
    }
  ],
  "91": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 13
    }
  ],
  "92": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 14
    }
  ],
  "93": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 15
    }
  ],
  "94": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 16
    }
  ],
  "95": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 17
    }
  ],
  "96": [
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
          "line": 12,
          "charByteOffset": 4
        },
        "end": {
          "line": 12,
          "charByteOffset": 18
        }
      }
    }
  ],
  "97": [
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
                  "scopeId": 1
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
                "line": 12,
                "charByteOffset": 12
              },
              "end": {
                "line": 12,
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
          "line": 12,
          "charByteOffset": 4
        },
        "end": {
          "line": 12,
          "charByteOffset": 18
        }
      }
    }
  ],
  "98": [
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
                  "scopeId": 1
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
                "line": 12,
                "charByteOffset": 16
              },
              "end": {
                "line": 12,
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
          "line": 12,
          "charByteOffset": 4
        },
        "end": {
          "line": 12,
          "charByteOffset": 18
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
                    "scopeId": 1
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
                  "line": 12,
                  "charByteOffset": 12
                },
                "end": {
                  "line": 12,
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
                    "scopeId": 1
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
                  "line": 12,
                  "charByteOffset": 16
                },
                "end": {
                  "line": 12,
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
                  "scopeId": 1
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
                "line": 12,
                "charByteOffset": 12
              },
              "end": {
                "line": 12,
                "charByteOffset": 17
              }
            }
          }
        },
        "o1": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "I25",
            "tag": {
              "#class": "tac.Tag.Int"
            },
            "callIndex": 0
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
                    "scopeId": 1
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
                  "line": 12,
                  "charByteOffset": 12
                },
                "end": {
                  "line": 12,
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
                    "scopeId": 1
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
                  "line": 12,
                  "charByteOffset": 16
                },
                "end": {
                  "line": 12,
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
          "line": 12,
          "charByteOffset": 4
        },
        "end": {
          "line": 12,
          "charByteOffset": 18
        }
      }
    }
  ],
  "100": [
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
          "line": 12,
          "charByteOffset": 4
        },
        "end": {
          "line": 12,
          "charByteOffset": 18
        }
      }
    }
  ],
  "101": [
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
          "line": 14,
          "charByteOffset": 4
        },
        "end": {
          "line": 14,
          "charByteOffset": 10
        }
      }
    }
  ],
  "102": [
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
          "line": 14,
          "charByteOffset": 4
        },
        "end": {
          "line": 14,
          "charByteOffset": 10
        }
      }
    }
  ],
  "103": [
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
          "line": 15,
          "charByteOffset": 4
        },
        "end": {
          "line": 15,
          "charByteOffset": 21
        }
      }
    }
  ],
  "104": [
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
                  "scopeId": 1
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
                "line": 15,
                "charByteOffset": 18
              },
              "end": {
                "line": 15,
                "charByteOffset": 19
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
          "line": 15,
          "charByteOffset": 4
        },
        "end": {
          "line": 15,
          "charByteOffset": 21
        }
      }
    }
  ],
  "105": [
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
          "line": 15,
          "charByteOffset": 4
        },
        "end": {
          "line": 15,
          "charByteOffset": 21
        }
      }
    }
  ],
  "106": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "I29",
        "tag": {
          "#class": "tac.Tag.Int"
        },
        "callIndex": 0
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
          "line": 15,
          "charByteOffset": 4
        },
        "end": {
          "line": 15,
          "charByteOffset": 21
        }
      }
    }
  ],
  "107": [
    {
      "key": {
        "name": "tac.immutable.array",
        "type": "vc.data.ImmutableBound",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "sym": {
          "#class": "vc.data.TACSymbol.Var.Full",
          "namePrefix": "tacCalldatasize",
          "tag": {
            "#class": "tac.Tag.Bit256"
          },
          "callIndex": 0,
          "meta": [
            {
              "key": {
                "name": "Tac.symbol.keyword",
                "type": "vc.data.TACSymbol$Var$KeywordEntry",
                "erasureStrategy": "Canonical"
              },
              "value": {
                "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                "name": "tacCalldatasize",
                "maybeTACKeywordOrdinal": 12
              }
            }
          ]
        }
      }
    },
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "tacCalldatabuf",
        "maybeTACKeywordOrdinal": 15
      }
    },
    {
      "key": {
        "name": "tac.wordmap-key",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "4"
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Split",
        "idx": "4"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.calldata.offset",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "4"
    },
    {
      "key": {
        "name": "tac.is.calldata",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "108": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON24",
        "tag": {
          "#class": "tac.Tag.Int"
        },
        "callIndex": 0,
        "meta": [
          {
            "key": {
              "name": "tac.is-temp-var",
              "type": "tac.MetaMap$Companion$NothingValue",
              "erasureStrategy": "Canonical"
            },
            "value": {
            }
          }
        ]
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
          "line": 15,
          "charByteOffset": 4
        },
        "end": {
          "line": 15,
          "charByteOffset": 21
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
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON25",
        "tag": {
          "#class": "tac.Tag.Int"
        },
        "callIndex": 0,
        "meta": [
          {
            "key": {
              "name": "tac.is-temp-var",
              "type": "tac.MetaMap$Companion$NothingValue",
              "erasureStrategy": "Canonical"
            },
            "value": {
            }
          }
        ]
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
          "line": 15,
          "charByteOffset": 4
        },
        "end": {
          "line": 15,
          "charByteOffset": 21
        }
      }
    }
  ],
  "110": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON26",
        "tag": {
          "#class": "tac.Tag.Int"
        },
        "callIndex": 0,
        "meta": [
          {
            "key": {
              "name": "tac.is-temp-var",
              "type": "tac.MetaMap$Companion$NothingValue",
              "erasureStrategy": "Canonical"
            },
            "value": {
            }
          }
        ]
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
          "line": 15,
          "charByteOffset": 4
        },
        "end": {
          "line": 15,
          "charByteOffset": 21
        }
      }
    }
  ],
  "111": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON27",
        "tag": {
          "#class": "tac.Tag.Int"
        },
        "callIndex": 0,
        "meta": [
          {
            "key": {
              "name": "tac.is-temp-var",
              "type": "tac.MetaMap$Companion$NothingValue",
              "erasureStrategy": "Canonical"
            },
            "value": {
            }
          }
        ]
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
          "line": 15,
          "charByteOffset": 4
        },
        "end": {
          "line": 15,
          "charByteOffset": 21
        }
      }
    }
  ],
  "112": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON28",
        "tag": {
          "#class": "tac.Tag.Int"
        },
        "callIndex": 0,
        "meta": [
          {
            "key": {
              "name": "tac.is-temp-var",
              "type": "tac.MetaMap$Companion$NothingValue",
              "erasureStrategy": "Canonical"
            },
            "value": {
            }
          }
        ]
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
          "line": 15,
          "charByteOffset": 4
        },
        "end": {
          "line": 15,
          "charByteOffset": 21
        }
      }
    }
  ],
  "113": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON29",
        "tag": {
          "#class": "tac.Tag.Int"
        },
        "callIndex": 0,
        "meta": [
          {
            "key": {
              "name": "tac.is-temp-var",
              "type": "tac.MetaMap$Companion$NothingValue",
              "erasureStrategy": "Canonical"
            },
            "value": {
            }
          }
        ]
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
          "line": 15,
          "charByteOffset": 4
        },
        "end": {
          "line": 15,
          "charByteOffset": 21
        }
      }
    }
  ],
  "114": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON30",
        "tag": {
          "#class": "tac.Tag.Int"
        },
        "callIndex": 0,
        "meta": [
          {
            "key": {
              "name": "tac.is-temp-var",
              "type": "tac.MetaMap$Companion$NothingValue",
              "erasureStrategy": "Canonical"
            },
            "value": {
            }
          }
        ]
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
          "line": 15,
          "charByteOffset": 4
        },
        "end": {
          "line": 15,
          "charByteOffset": 21
        }
      }
    }
  ],
  "115": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON31",
        "tag": {
          "#class": "tac.Tag.Int"
        },
        "callIndex": 0,
        "meta": [
          {
            "key": {
              "name": "tac.is-temp-var",
              "type": "tac.MetaMap$Companion$NothingValue",
              "erasureStrategy": "Canonical"
            },
            "value": {
            }
          }
        ]
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
          "line": 15,
          "charByteOffset": 4
        },
        "end": {
          "line": 15,
          "charByteOffset": 21
        }
      }
    }
  ],
  "116": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON32",
        "tag": {
          "#class": "tac.Tag.Int"
        },
        "callIndex": 0,
        "meta": [
          {
            "key": {
              "name": "tac.is-temp-var",
              "type": "tac.MetaMap$Companion$NothingValue",
              "erasureStrategy": "Canonical"
            },
            "value": {
            }
          }
        ]
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
          "line": 15,
          "charByteOffset": 4
        },
        "end": {
          "line": 15,
          "charByteOffset": 21
        }
      }
    }
  ],
  "117": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON33",
        "tag": {
          "#class": "tac.Tag.Int"
        },
        "callIndex": 0,
        "meta": [
          {
            "key": {
              "name": "tac.is-temp-var",
              "type": "tac.MetaMap$Companion$NothingValue",
              "erasureStrategy": "Canonical"
            },
            "value": {
            }
          }
        ]
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
          "line": 15,
          "charByteOffset": 4
        },
        "end": {
          "line": 15,
          "charByteOffset": 21
        }
      }
    }
  ],
  "118": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON34",
        "tag": {
          "#class": "tac.Tag.Int"
        },
        "callIndex": 0,
        "meta": [
          {
            "key": {
              "name": "tac.is-temp-var",
              "type": "tac.MetaMap$Companion$NothingValue",
              "erasureStrategy": "Canonical"
            },
            "value": {
            }
          }
        ]
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
          "line": 15,
          "charByteOffset": 4
        },
        "end": {
          "line": 15,
          "charByteOffset": 21
        }
      }
    }
  ],
  "119": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON35",
        "tag": {
          "#class": "tac.Tag.Int"
        },
        "callIndex": 0,
        "meta": [
          {
            "key": {
              "name": "tac.is-temp-var",
              "type": "tac.MetaMap$Companion$NothingValue",
              "erasureStrategy": "Canonical"
            },
            "value": {
            }
          }
        ]
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
          "line": 15,
          "charByteOffset": 4
        },
        "end": {
          "line": 15,
          "charByteOffset": 21
        }
      }
    }
  ],
  "120": [
    {
      "key": {
        "name": "tac.transfers.balance",
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
          "line": 15,
          "charByteOffset": 4
        },
        "end": {
          "line": 15,
          "charByteOffset": 21
        }
      }
    }
  ],
  "121": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "tacAddress",
        "maybeTACKeywordOrdinal": 22
      }
    },
    {
      "key": {
        "name": "tac.env.known-bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 160
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
  "122": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 25,
        "len": 841,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000001",
        "sourceContext": {
          "indexToFilePath": {
            "0": "TestContract.sol"
          },
          "sourceDir": ".post_autofinders.0"
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
          "line": 15,
          "charByteOffset": 4
        },
        "end": {
          "line": 15,
          "charByteOffset": 21
        }
      }
    }
  ],
  "123": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 235,
        "len": 75,
        "jumpType": "ENTER",
        "address": "ce4604a0000000000000000000000001",
        "sourceContext": {
          "indexToFilePath": {
            "0": "TestContract.sol"
          },
          "sourceDir": ".post_autofinders.0"
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
          "line": 15,
          "charByteOffset": 4
        },
        "end": {
          "line": 15,
          "charByteOffset": 21
        }
      }
    }
  ],
  "124": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 298,
        "len": 4,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000001",
        "sourceContext": {
          "indexToFilePath": {
            "0": "TestContract.sol"
          },
          "sourceDir": ".post_autofinders.0"
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
          "line": 15,
          "charByteOffset": 4
        },
        "end": {
          "line": 15,
          "charByteOffset": 21
        }
      }
    }
  ],
  "125": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 282,
        "len": 21,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000001",
        "sourceContext": {
          "indexToFilePath": {
            "0": "TestContract.sol"
          },
          "sourceDir": ".post_autofinders.0"
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
          "line": 15,
          "charByteOffset": 4
        },
        "end": {
          "line": 15,
          "charByteOffset": 21
        }
      }
    }
  ],
  "126": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 282,
        "len": 21,
        "jumpType": "ENTER",
        "address": "ce4604a0000000000000000000000001",
        "sourceContext": {
          "indexToFilePath": {
            "0": "TestContract.sol"
          },
          "sourceDir": ".post_autofinders.0"
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
          "line": 15,
          "charByteOffset": 4
        },
        "end": {
          "line": 15,
          "charByteOffset": 21
        }
      }
    }
  ],
  "127": [
    {
      "key": {
        "name": "tac.immutable.array",
        "type": "vc.data.ImmutableBound",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "sym": {
          "#class": "vc.data.TACSymbol.Var.Full",
          "namePrefix": "tacCalldatasize!!30",
          "tag": {
            "#class": "tac.Tag.Bit256"
          },
          "callIndex": 0,
          "meta": [
            {
              "key": {
                "name": "Tac.symbol.keyword",
                "type": "vc.data.TACSymbol$Var$KeywordEntry",
                "erasureStrategy": "Canonical"
              },
              "value": {
                "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                "name": "tacCalldatasize",
                "maybeTACKeywordOrdinal": 12
              }
            }
          ]
        }
      }
    },
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "tacCalldatabuf",
        "maybeTACKeywordOrdinal": 15
      }
    },
    {
      "key": {
        "name": "tac.wordmap-key",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "4"
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Split",
        "idx": "4"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.calldata.offset",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "4"
    },
    {
      "key": {
        "name": "tac.is.calldata",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "128": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 282,
        "len": 21,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000001",
        "sourceContext": {
          "indexToFilePath": {
            "0": "TestContract.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "tac.storage.node",
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
            "offset": "0"
          }
        ]
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
          "line": 15,
          "charByteOffset": 4
        },
        "end": {
          "line": 15,
          "charByteOffset": 21
        }
      }
    },
    {
      "key": {
        "name": "tac.call-graph.address-read",
        "type": "analysis.icfg.CallGraphBuilder$ContractStorageRead",
        "erasureStrategy": "Canonical"
      },
      "value": "rO0ABXNyADJhbmFseXNpcy5pY2ZnLkNhbGxHcmFwaEJ1aWxkZXIkQ29udHJhY3RTdG9yYWdlUmVhZJo5HPv1EkgqAgABSQACaWR4cAAAAAA="
    },
    {
      "key": {
        "name": "tac.storage.access",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "tac.storage.printer",
        "type": "instrumentation.StoragePathAnnotation$StoragePathPrinter",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "129": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.FieldAccess",
            "field": "x",
            "base": {
              "#class": "analysis.storage.DisplayPath.MapAccess",
              "key": {
                "#class": "vc.data.TACSymbol.Const",
                "value": "0"
              },
              "keyTyp": {
                "#class": "tac.TACStorageType.IntegralType",
                "typeLabel": "uint256",
                "numBytes": "20",
                "descriptor": {
                  "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                  "bitwidth": 256
                },
                "lowerBound": null,
                "upperBound": null
              },
              "base": {
                "#class": "analysis.storage.DisplayPath.Root",
                "name": "m"
              }
            }
          }
        ]
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
                "#class": "vc.data.TACSymbol.Const",
                "value": "0"
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R8",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "tac.is-temp-var",
                      "type": "tac.MetaMap$Companion$NothingValue",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                    }
                  }
                ]
              },
              "hashResult": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R44",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "vc.data.TACSymbol$Var$KeywordEntry",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                      "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                      "name": "L",
                      "maybeTACKeywordOrdinal": 45
                    }
                  },
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
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1018
                  }
                ]
              }
            },
            "offset": {
              "#class": "analysis.storage.StorageAnalysis.Offset.Words",
              "numWords": "0"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1009
    }
  ],
  "130": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 282,
        "len": 21,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000001",
        "sourceContext": {
          "indexToFilePath": {
            "0": "TestContract.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "tac.storage.node",
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
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "test.spec",
        "start": {
          "line": 15,
          "charByteOffset": 4
        },
        "end": {
          "line": 15,
          "charByteOffset": 21
        }
      }
    },
    {
      "key": {
        "name": "tac.call-graph.address-read",
        "type": "analysis.icfg.CallGraphBuilder$ContractStorageRead",
        "erasureStrategy": "Canonical"
      },
      "value": "rO0ABXNyADJhbmFseXNpcy5pY2ZnLkNhbGxHcmFwaEJ1aWxkZXIkQ29udHJhY3RTdG9yYWdlUmVhZJo5HPv1EkgqAgABSQACaWR4cAAAAAE="
    },
    {
      "key": {
        "name": "tac.storage.access",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "tac.storage.printer",
        "type": "instrumentation.StoragePathAnnotation$StoragePathPrinter",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "131": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.FieldAccess",
            "field": "y",
            "base": {
              "#class": "analysis.storage.DisplayPath.MapAccess",
              "key": {
                "#class": "vc.data.TACSymbol.Const",
                "value": "0"
              },
              "keyTyp": {
                "#class": "tac.TACStorageType.IntegralType",
                "typeLabel": "uint256",
                "numBytes": "20",
                "descriptor": {
                  "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                  "bitwidth": 256
                },
                "lowerBound": null,
                "upperBound": null
              },
              "base": {
                "#class": "analysis.storage.DisplayPath.Root",
                "name": "m"
              }
            }
          }
        ]
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
                "#class": "vc.data.TACSymbol.Const",
                "value": "0"
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R8",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "tac.is-temp-var",
                      "type": "tac.MetaMap$Companion$NothingValue",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                    }
                  }
                ]
              },
              "hashResult": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R44",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "vc.data.TACSymbol$Var$KeywordEntry",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                      "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                      "name": "L",
                      "maybeTACKeywordOrdinal": 45
                    }
                  },
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
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1018
                  }
                ]
              }
            },
            "offset": {
              "#class": "analysis.storage.StorageAnalysis.Offset.Bytes",
              "numBytes": "20"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1009
    }
  ],
  "132": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.FieldAccess",
            "field": "z1",
            "base": {
              "#class": "analysis.storage.DisplayPath.MapAccess",
              "key": {
                "#class": "vc.data.TACSymbol.Const",
                "value": "0"
              },
              "keyTyp": {
                "#class": "tac.TACStorageType.IntegralType",
                "typeLabel": "uint256",
                "numBytes": "20",
                "descriptor": {
                  "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                  "bitwidth": 256
                },
                "lowerBound": null,
                "upperBound": null
              },
              "base": {
                "#class": "analysis.storage.DisplayPath.Root",
                "name": "m"
              }
            }
          }
        ]
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
                "#class": "vc.data.TACSymbol.Const",
                "value": "0"
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R8",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "tac.is-temp-var",
                      "type": "tac.MetaMap$Companion$NothingValue",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                    }
                  }
                ]
              },
              "hashResult": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R44",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "vc.data.TACSymbol$Var$KeywordEntry",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                      "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                      "name": "L",
                      "maybeTACKeywordOrdinal": 45
                    }
                  },
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
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1018
                  }
                ]
              }
            },
            "offset": {
              "#class": "analysis.storage.StorageAnalysis.Offset.Bytes",
              "numBytes": "34"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1009
    }
  ],
  "133": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.FieldAccess",
            "field": "z2",
            "base": {
              "#class": "analysis.storage.DisplayPath.MapAccess",
              "key": {
                "#class": "vc.data.TACSymbol.Const",
                "value": "0"
              },
              "keyTyp": {
                "#class": "tac.TACStorageType.IntegralType",
                "typeLabel": "uint256",
                "numBytes": "20",
                "descriptor": {
                  "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                  "bitwidth": 256
                },
                "lowerBound": null,
                "upperBound": null
              },
              "base": {
                "#class": "analysis.storage.DisplayPath.Root",
                "name": "m"
              }
            }
          }
        ]
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
                "#class": "vc.data.TACSymbol.Const",
                "value": "0"
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R8",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "tac.is-temp-var",
                      "type": "tac.MetaMap$Companion$NothingValue",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                    }
                  }
                ]
              },
              "hashResult": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R44",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "vc.data.TACSymbol$Var$KeywordEntry",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                      "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                      "name": "L",
                      "maybeTACKeywordOrdinal": 45
                    }
                  },
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
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1018
                  }
                ]
              }
            },
            "offset": {
              "#class": "analysis.storage.StorageAnalysis.Offset.Bytes",
              "numBytes": "35"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1009
    }
  ],
  "134": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.FieldAccess",
            "field": "b1",
            "base": {
              "#class": "analysis.storage.DisplayPath.MapAccess",
              "key": {
                "#class": "vc.data.TACSymbol.Const",
                "value": "0"
              },
              "keyTyp": {
                "#class": "tac.TACStorageType.IntegralType",
                "typeLabel": "uint256",
                "numBytes": "20",
                "descriptor": {
                  "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                  "bitwidth": 256
                },
                "lowerBound": null,
                "upperBound": null
              },
              "base": {
                "#class": "analysis.storage.DisplayPath.Root",
                "name": "m"
              }
            }
          }
        ]
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
                "#class": "vc.data.TACSymbol.Const",
                "value": "0"
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R8",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "tac.is-temp-var",
                      "type": "tac.MetaMap$Companion$NothingValue",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                    }
                  }
                ]
              },
              "hashResult": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R44",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "vc.data.TACSymbol$Var$KeywordEntry",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                      "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                      "name": "L",
                      "maybeTACKeywordOrdinal": 45
                    }
                  },
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
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1018
                  }
                ]
              }
            },
            "offset": {
              "#class": "analysis.storage.StorageAnalysis.Offset.Bytes",
              "numBytes": "36"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1009
    }
  ],
  "135": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 282,
        "len": 21,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000001",
        "sourceContext": {
          "indexToFilePath": {
            "0": "TestContract.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "tac.storage.node",
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
            "offset": "2"
          }
        ]
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
          "line": 15,
          "charByteOffset": 4
        },
        "end": {
          "line": 15,
          "charByteOffset": 21
        }
      }
    },
    {
      "key": {
        "name": "tac.call-graph.address-read",
        "type": "analysis.icfg.CallGraphBuilder$ContractStorageRead",
        "erasureStrategy": "Canonical"
      },
      "value": "rO0ABXNyADJhbmFseXNpcy5pY2ZnLkNhbGxHcmFwaEJ1aWxkZXIkQ29udHJhY3RTdG9yYWdlUmVhZJo5HPv1EkgqAgABSQACaWR4cAAAAAI="
    },
    {
      "key": {
        "name": "tac.storage.access",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "tac.storage.printer",
        "type": "instrumentation.StoragePathAnnotation$StoragePathPrinter",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "136": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.FieldAccess",
            "field": "x2",
            "base": {
              "#class": "analysis.storage.DisplayPath.MapAccess",
              "key": {
                "#class": "vc.data.TACSymbol.Const",
                "value": "0"
              },
              "keyTyp": {
                "#class": "tac.TACStorageType.IntegralType",
                "typeLabel": "uint256",
                "numBytes": "20",
                "descriptor": {
                  "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                  "bitwidth": 256
                },
                "lowerBound": null,
                "upperBound": null
              },
              "base": {
                "#class": "analysis.storage.DisplayPath.Root",
                "name": "m"
              }
            }
          }
        ]
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
                "#class": "vc.data.TACSymbol.Const",
                "value": "0"
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R8",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "tac.is-temp-var",
                      "type": "tac.MetaMap$Companion$NothingValue",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                    }
                  }
                ]
              },
              "hashResult": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R44",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "vc.data.TACSymbol$Var$KeywordEntry",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                      "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                      "name": "L",
                      "maybeTACKeywordOrdinal": 45
                    }
                  },
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
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1018
                  }
                ]
              }
            },
            "offset": {
              "#class": "analysis.storage.StorageAnalysis.Offset.Words",
              "numWords": "2"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1009
    }
  ],
  "137": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 282,
        "len": 21,
        "jumpType": "REGULAR",
        "address": "ce4604a0000000000000000000000001",
        "sourceContext": {
          "indexToFilePath": {
            "0": "TestContract.sol"
          },
          "sourceDir": ".post_autofinders.0"
        }
      }
    },
    {
      "key": {
        "name": "tac.storage.node",
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
            "offset": "3"
          }
        ]
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
          "line": 15,
          "charByteOffset": 4
        },
        "end": {
          "line": 15,
          "charByteOffset": 21
        }
      }
    },
    {
      "key": {
        "name": "tac.storage.access",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    },
    {
      "key": {
        "name": "tac.storage.printer",
        "type": "instrumentation.StoragePathAnnotation$StoragePathPrinter",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "138": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
      }
    },
    {
      "key": {
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.FieldAccess",
            "field": "b2",
            "base": {
              "#class": "analysis.storage.DisplayPath.MapAccess",
              "key": {
                "#class": "vc.data.TACSymbol.Const",
                "value": "0"
              },
              "keyTyp": {
                "#class": "tac.TACStorageType.IntegralType",
                "typeLabel": "uint256",
                "numBytes": "20",
                "descriptor": {
                  "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                  "bitwidth": 256
                },
                "lowerBound": null,
                "upperBound": null
              },
              "base": {
                "#class": "analysis.storage.DisplayPath.Root",
                "name": "m"
              }
            }
          }
        ]
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
                "#class": "vc.data.TACSymbol.Const",
                "value": "0"
              },
              "baseSlot": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R8",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "tac.is-temp-var",
                      "type": "tac.MetaMap$Companion$NothingValue",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                    }
                  }
                ]
              },
              "hashResult": {
                "#class": "vc.data.TACSymbol.Var.Full",
                "namePrefix": "R44",
                "tag": {
                  "#class": "tac.Tag.Bit256"
                },
                "callIndex": 0,
                "meta": [
                  {
                    "key": {
                      "name": "Tac.symbol.keyword",
                      "type": "vc.data.TACSymbol$Var$KeywordEntry",
                      "erasureStrategy": "Canonical"
                    },
                    "value": {
                      "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                      "name": "L",
                      "maybeTACKeywordOrdinal": 45
                    }
                  },
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
                      "name": "tac.stack.height",
                      "type": "java.lang.Integer",
                      "erasureStrategy": "Canonical"
                    },
                    "value": 1018
                  }
                ]
              }
            },
            "offset": {
              "#class": "analysis.storage.StorageAnalysis.Offset.Bytes",
              "numBytes": "60"
            }
          }
        ]
      }
    },
    {
      "key": {
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1009
    }
  ],
  "139": [
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "L",
        "maybeTACKeywordOrdinal": 45
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
        "name": "tac.stack.height",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1021
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
  "140": [
    {
      "key": {
        "name": "tac.immutable.array",
        "type": "vc.data.ImmutableBound",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "sym": {
          "#class": "vc.data.TACSymbol.Var.Full",
          "namePrefix": "tacCalldatasize!!2",
          "tag": {
            "#class": "tac.Tag.Bit256"
          },
          "callIndex": 0,
          "meta": [
            {
              "key": {
                "name": "Tac.symbol.keyword",
                "type": "vc.data.TACSymbol$Var$KeywordEntry",
                "erasureStrategy": "Canonical"
              },
              "value": {
                "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
                "name": "tacCalldatasize",
                "maybeTACKeywordOrdinal": 12
              }
            }
          ]
        }
      }
    },
    {
      "key": {
        "name": "Tac.symbol.keyword",
        "type": "vc.data.TACSymbol$Var$KeywordEntry",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry",
        "name": "tacCalldatabuf",
        "maybeTACKeywordOrdinal": 15
      }
    },
    {
      "key": {
        "name": "tac.wordmap-key",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "4"
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Split",
        "idx": "4"
      }
    },
    {
      "key": {
        "name": "tac.storage.bit-width",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 256
    },
    {
      "key": {
        "name": "tac.calldata.offset",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
      },
      "value": "4"
    },
    {
      "key": {
        "name": "tac.is.calldata",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "141": [
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
          "line": 7,
          "charByteOffset": 4
        },
        "end": {
          "line": 7,
          "charByteOffset": 31
        }
      }
    }
  ],
  "142": [
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
                  "scopeId": 3
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
                "line": 7,
                "charByteOffset": 25
              },
              "end": {
                "line": 7,
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
          "line": 7,
          "charByteOffset": 4
        },
        "end": {
          "line": 7,
          "charByteOffset": 31
        }
      }
    }
  ],
  "143": [
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
          "line": 7,
          "charByteOffset": 4
        },
        "end": {
          "line": 7,
          "charByteOffset": 31
        }
      }
    }
  ],
  "144": [
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
          "line": 7,
          "charByteOffset": 4
        },
        "end": {
          "line": 7,
          "charByteOffset": 31
        }
      }
    }
  ],
  "145": [
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
          "line": 7,
          "charByteOffset": 4
        },
        "end": {
          "line": 7,
          "charByteOffset": 31
        }
      }
    }
  ],
  "146": [
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
                "namePrefix": "I88",
                "tag": {
                  "#class": "tac.Tag.Int"
                },
                "callIndex": 0
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
  "147": [
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
                  "scopeId": 3
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
              "comment": "autogenerated bool expression at test.spec:8:5"
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
          "line": 7,
          "charByteOffset": 4
        },
        "end": {
          "line": 7,
          "charByteOffset": 31
        }
      }
    }
  ],
  "148": [
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
          "line": 8,
          "charByteOffset": 4
        },
        "end": {
          "line": 8,
          "charByteOffset": 44
        }
      }
    }
  ],
  "149": [
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
                  "scopeId": 3
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
                "charByteOffset": 27
              },
              "end": {
                "line": 8,
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
          "line": 8,
          "charByteOffset": 4
        },
        "end": {
          "line": 8,
          "charByteOffset": 44
        }
      }
    }
  ],
  "150": [
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
          "charByteOffset": 44
        }
      }
    }
  ],
  "151": [
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
          "charByteOffset": 44
        }
      }
    }
  ],
  "152": [
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
          "charByteOffset": 44
        }
      }
    }
  ],
  "153": [
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
  "154": [
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
                "namePrefix": "I95",
                "tag": {
                  "#class": "tac.Tag.Int"
                },
                "callIndex": 0
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
  "155": [
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
                  "scopeId": 3
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
                "line": 8,
                "charByteOffset": 37
              },
              "end": {
                "line": 8,
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
          "line": 8,
          "charByteOffset": 4
        },
        "end": {
          "line": 8,
          "charByteOffset": 44
        }
      }
    }
  ],
  "156": [
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
                  "scopeId": 3
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
                "line": 8,
                "charByteOffset": 41
              },
              "end": {
                "line": 8,
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
          "line": 8,
          "charByteOffset": 4
        },
        "end": {
          "line": 8,
          "charByteOffset": 44
        }
      }
    }
  ],
  "157": [
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
                    "scopeId": 3
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
                  "line": 8,
                  "charByteOffset": 37
                },
                "end": {
                  "line": 8,
                  "charByteOffset": 38
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
                    "scopeId": 3
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
                  "line": 8,
                  "charByteOffset": 41
                },
                "end": {
                  "line": 8,
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
                  "scopeId": 3
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
                "line": 8,
                "charByteOffset": 37
              },
              "end": {
                "line": 8,
                "charByteOffset": 42
              }
            },
            "hasParens": true
          }
        },
        "o1": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "I100",
            "tag": {
              "#class": "tac.Tag.Int"
            },
            "callIndex": 0
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
                    "scopeId": 3
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
                  "line": 8,
                  "charByteOffset": 37
                },
                "end": {
                  "line": 8,
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
                    "scopeId": 3
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
                  "line": 8,
                  "charByteOffset": 41
                },
                "end": {
                  "line": 8,
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
          "line": 8,
          "charByteOffset": 4
        },
        "end": {
          "line": 8,
          "charByteOffset": 44
        }
      }
    }
  ],
  "158": [
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
                          "scopeId": 3
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
                        "line": 8,
                        "charByteOffset": 12
                      },
                      "end": {
                        "line": 8,
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
                        "scopeId": 3
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
                      "line": 8,
                      "charByteOffset": 12
                    },
                    "end": {
                      "line": 8,
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
                        "scopeId": 3
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
                      "charByteOffset": 27
                    },
                    "end": {
                      "line": 8,
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
                      "scopeId": 3
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
                    "line": 8,
                    "charByteOffset": 12
                  },
                  "end": {
                    "line": 8,
                    "charByteOffset": 29
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
                    "scopeId": 3
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
                  "line": 8,
                  "charByteOffset": 12
                },
                "end": {
                  "line": 8,
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
                      "scopeId": 3
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
                    "line": 8,
                    "charByteOffset": 37
                  },
                  "end": {
                    "line": 8,
                    "charByteOffset": 38
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
                      "scopeId": 3
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
                    "line": 8,
                    "charByteOffset": 41
                  },
                  "end": {
                    "line": 8,
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
                    "scopeId": 3
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
                  "line": 8,
                  "charByteOffset": 37
                },
                "end": {
                  "line": 8,
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
                  "scopeId": 3
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
                "line": 8,
                "charByteOffset": 12
              },
              "end": {
                "line": 8,
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
                          "scopeId": 3
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
                        "line": 8,
                        "charByteOffset": 12
                      },
                      "end": {
                        "line": 8,
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
                        "scopeId": 3
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
                      "line": 8,
                      "charByteOffset": 12
                    },
                    "end": {
                      "line": 8,
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
                        "scopeId": 3
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
                      "charByteOffset": 27
                    },
                    "end": {
                      "line": 8,
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
                      "scopeId": 3
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
                    "line": 8,
                    "charByteOffset": 12
                  },
                  "end": {
                    "line": 8,
                    "charByteOffset": 29
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
                    "scopeId": 3
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
                  "line": 8,
                  "charByteOffset": 12
                },
                "end": {
                  "line": 8,
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
                      "scopeId": 3
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
                    "line": 8,
                    "charByteOffset": 37
                  },
                  "end": {
                    "line": 8,
                    "charByteOffset": 38
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
                      "scopeId": 3
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
                    "line": 8,
                    "charByteOffset": 41
                  },
                  "end": {
                    "line": 8,
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
                    "scopeId": 3
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
                  "line": 8,
                  "charByteOffset": 37
                },
                "end": {
                  "line": 8,
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
          "line": 8,
          "charByteOffset": 4
        },
        "end": {
          "line": 8,
          "charByteOffset": 44
        }
      }
    }
  ],
  "159": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 235,
        "len": 75,
        "jumpType": "EXIT",
        "address": "ce4604a0000000000000000000000001",
        "sourceContext": {
          "indexToFilePath": {
            "0": "TestContract.sol"
          },
          "sourceDir": ".post_autofinders.0"
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
          "line": 15,
          "charByteOffset": 4
        },
        "end": {
          "line": 15,
          "charByteOffset": 21
        }
      }
    }
  ],
  "160": [
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
          "line": 18,
          "charByteOffset": 4
        },
        "end": {
          "line": 18,
          "charByteOffset": 32
        }
      }
    }
  ],
  "161": [
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
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 1
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
                "line": 18,
                "charByteOffset": 26
              },
              "end": {
                "line": 18,
                "charByteOffset": 27
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
          "line": 18,
          "charByteOffset": 4
        },
        "end": {
          "line": 18,
          "charByteOffset": 32
        }
      }
    }
  ],
  "162": [
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
          "line": 18,
          "charByteOffset": 4
        },
        "end": {
          "line": 18,
          "charByteOffset": 32
        }
      }
    }
  ],
  "163": [
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
          "line": 18,
          "charByteOffset": 4
        },
        "end": {
          "line": 18,
          "charByteOffset": 32
        }
      }
    }
  ],
  "164": [
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
          "line": 18,
          "charByteOffset": 4
        },
        "end": {
          "line": 18,
          "charByteOffset": 32
        }
      }
    }
  ],
  "165": [
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
                "namePrefix": "I104",
                "tag": {
                  "#class": "tac.Tag.Int"
                },
                "callIndex": 0
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
  "166": [
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
          "line": 18,
          "charByteOffset": 4
        },
        "end": {
          "line": 18,
          "charByteOffset": 32
        }
      }
    }
  ]
}