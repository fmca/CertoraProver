TACSymbolTable {
	UserDefined {
		UninterpSort skey
	}
	BuiltinFunctions {
		to_skey:JSON{"#class":"vc.data.TACBuiltInFunction.Hash.ToSkey"}
		skey_basic:JSON{"#class":"vc.data.TACBuiltInFunction.Hash.Basic"}
		safe_math_narrow_bv256:JSON{"#class":"vc.data.TACBuiltInFunction.SafeMathNarrow","returnSort":{"bits":256}}
	}
	UninterpretedFunctions {
		CANON111:JSON{"name":"CANON111","paramSorts":[{"#class":"tac.Tag.Int"}],"returnSort":{"#class":"tac.Tag.Int"},"attribute":"Ghost","cvlResultType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"cvlParamTypes":[{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}],"declarationName":"CANON111"}
		CANON84:JSON{"name":"CANON84","paramSorts":[{"#class":"tac.Tag.Int"}],"returnSort":{"#class":"tac.Tag.Int"},"attribute":"Ghost","cvlResultType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"cvlParamTypes":[{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}],"declarationName":"CANON84"}
		CANON92:JSON{"name":"CANON92","paramSorts":[],"returnSort":{"#class":"tac.Tag.Int"},"attribute":"Ghost","cvlResultType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"cvlParamTypes":[],"declarationName":"CANON92"}
	}
	tacM0x40@2:bv256:0
	tacM0x40@5:bv256:0
	tacM0x40@7:bv256:0
	tacCodesizeCANON0:bv256:1
	tacCalldatabufCANON0@2:bv256:2
	tacCalldatabufCANON0@5:bv256:2
	tacCalldatabufCANON1@2:bv256:3
	CANON85!!77:int:4
	CANON85!!89:int:4
	tacM0x40!!0:bv256:0
	tacM0x40!!1:bv256:0
	tacM0x40!!2:bv256:0
	tacAddress!!31:bv256:5
	tacAddress!!59:bv256:5
	tacAddress!!80:bv256:5
	lastReverted:bool:6
	tacExtcodesize!!4:wordmap:7
	CANON88!!8:bv256:8
	tacCalldatasize@2:bv256:9
	tacCalldatasize@5:bv256:9
	tacCalldatasize@7:bv256:9
	calledContract:int:10
	tacExtcodesize:wordmap:7
	CANON100:bool:11
	CANON101:int
	CANON102:int
	CANON103:bool:11
	CANON104:int
	CANON105:int
	CANON106:bool
	CANON107:int
	CANON108:bool:12
	CANON109:bool:11
	CANON111:ghostmap(int->int)
	tacCalldatasize!!28:bv256:9
	tacCalldatasize!!56:bv256:9
	tacCalldatasize!!78:bv256:9
	tacBalance:wordmap:13
	calledContract!!42:int:10
	calledContract!!69:int:10
	tacBalance!!36:wordmap:13
	tacBalance!!40:wordmap:13
	tacBalance!!64:wordmap:13
	tacBalance!!5:wordmap:13
	tacCalldatabuf@2:bytemap:14
	tacCalldatabuf@5:bytemap:15
	tacCalldatabuf@7:bytemap:16
	CANON59!!55:int:17
	CANON59!!76:int:17
	R3:bv256:1
	R6:bv256:18
	R9:bv256:19
	B18:bool:20
	B19:bool:20
	B22:bool
	B83:bool:12
	B84:bool
	B92:bool
	I20:int
	I21:int
	I23:int
	I24:int
	I25:int
	I26:int
	I35:int:20
	I38:int:20
	I45:int
	I46:int
	I47:int
	I48:int
	I53:int
	I54:int
	I63:int:20
	I66:int:20
	I72:int
	I85:int
	I90:int
	I91:int
	I93:int
	I94:int
	I95:int
	I96:int
	I97:int
	I98:int
	R10:bv256:21
	R11:bv256:22
	R12:bv256:23
	R17:bv256:20
	R29:bv256:20
	R32:bv256:20
	R33:bv256:20
	R34:bv256:20
	R37:bv256:20
	R39:bv256:20
	R41:bv256:20
	R49:bv256:24
	R57:bv256:20
	R60:bv256:20
	R61:bv256:20
	R62:bv256:20
	R65:bv256:20
	R67:bv256:20
	R68:bv256:20
	R73:bv256:24
	R79:bv256:20
	R81:bv256:20
	R82:bv256:18
	R86:bv256:24
	B101:bool:12
	I100:int
	CANON!!16:int:25
	CANON!!44:int:25
	CANON!!71:int:25
	CANON28!7:ghostmap(bv256*bv256*bv256->bv256):26
	tacAddress@2:bv256:5
	tacAddress@5:bv256:5
	tacAddress@7:bv256:5
	LCANON0@2:bv256:24
	LCANON1@5:bv256:24
	LCANON2@7:bv256:18
	LCANON3@7:bv256:24
	CANON10:int:27
	CANON11:int:28
	CANON12:int:29
	CANON13:int:30
	CANON14:int:31
	CANON15:int:32
	CANON16:int:33
	CANON17:int:34
	CANON18:int
	CANON19:int
	CANON20:bool
	CANON21:int
	CANON22:int:35
	CANON23:int
	CANON24:int
	CANON25:int
	CANON26:int:36
	CANON28:ghostmap(bv256*bv256*bv256->bv256):26
	CANON29:bv256:20
	CANON42:bv256:20
	CANON43:bv256:20
	CANON44:bv256:20
	CANON45:bv256:20
	CANON46:int:20
	CANON47:bv256:20
	CANON48:int:20
	CANON49:bv256:20
	CANON50@2:bv256:20
	CANON50@5:bv256:20
	CANON50@7:bv256:20
	CANON51:int:37
	CANON52:int:38
	CANON53:int
	CANON54:int
	CANON55:int
	CANON56:int
	CANON57:int
	CANON58:int
	CANON59:int:17
	CANON61:bv256:20
	CANON74:bv256:20
	CANON75:bv256:20
	CANON76:bv256:20
	CANON77:bv256:20
	CANON78:int:20
	CANON79:bv256:20
	CANON80:int:20
	CANON81:bv256:20
	CANON82:int:39
	CANON83:int:40
	CANON84:ghostmap(int->int):41
	CANON85:int:4
	CANON87:bv256:20
	CANON88:bv256:8
	CANON89:bool:12
	CANON90:bool
	CANON92:int:42
	CANON93:int:43
	CANON94:bool:11
	CANON95:int
	CANON96:int
	CANON97:bool
	CANON98:int
	CANON99:int
	tacContractAtCANON1:bv256:19
	tacContractAtCANON2:bv256:21
	tacContractAtCANON3:bv256:22
	executingContract:int:44
	lastHasThrown:bool:45
	lastReverted!!51:bool:6
	lastReverted!!75:bool:6
	lastReverted!!88:bool:6
	CANON1:bv256:20
	CANON2:bool:20
	CANON3:bool:20
	CANON4:int:46
	CANON5:int:47
	CANON6:int:48
	CANON7:int:49
	CANON8:int:50
	CANON9:int:51
	tacContractAtCANON:bv256:23
	executingContract!!43:int:44
	executingContract!!70:int:44
	CANON26!!27:int:36
	CANON26!!52:int:36
	lastHasThrown!!30:bool:45
	lastHasThrown!!50:bool:45
	lastHasThrown!!58:bool:45
	lastHasThrown!!74:bool:45
	lastHasThrown!!87:bool:45
	tacSighash!!13:bv256:52
	tacSighash!!14:bv256:52
	tacSighash!!15:bv256:52
	tacSighash@2:bv256:52
	tacSighash@5:bv256:52
	tacSighash@7:bv256:52
	CANON:int:25
	CANON106!!99:bool:11
}
Program {
	Block 0_0_0_0_0_0 Succ [1_0_0_1_0_1] {
		AssignHavocCmd tacM0x40!!0:0
		AssumeExpCmd Le(tacM0x40!!0:0 0x80 )
		AssignHavocCmd tacM0x40!!1:0
		AssumeExpCmd Le(tacM0x40!!1:0 0x80 )
		AssignHavocCmd tacM0x40!!2:0
		AssumeExpCmd Le(tacM0x40!!2:0 0x80 )
		AssignHavocCmd R3:1
		AssumeExpCmd Ge(R3:1 0x1 )
		AssignHavocCmd tacExtcodesize!!4:7
		AssignHavocCmd tacBalance!!5:13
		AssignHavocCmd R6:18
		AssignHavocCmd CANON10:27
		AssumeExpCmd LAnd(Ge(CANON10:27 0x0(int) ) Le(CANON10:27 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff(int) ) )
		AssignHavocCmd CANON11:28
		AssumeExpCmd LAnd(Ge(CANON11:28 0x0(int) ) Le(CANON11:28 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff(int) ) )
		AssignHavocCmd CANON12:29
		AssumeExpCmd LAnd(Ge(CANON12:29 0x0(int) ) Le(CANON12:29 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff(int) ) )
		AssignHavocCmd CANON13:30
		AssumeExpCmd LAnd(Ge(CANON13:30 0x0(int) ) Le(CANON13:30 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff(int) ) )
		AssignHavocCmd CANON15:32
		AssumeExpCmd Eq(CANON15:32 0x14(int) )
		AssignHavocCmd CANON28!7:26
		AssignHavocCmd CANON84:41
		AssignHavocCmd CANON88!!8:8
		AssumeExpCmd Ge(CANON88!!8:8 0x2 )
		AssignHavocCmd CANON92:42
		AssumeExpCmd LAnd(Ge(CANON92:42 0x2(int) ) Le(CANON92:42 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff(int) ) )
		AssignHavocCmd R9:19
		AssumeExpCmd Eq(R9:19 0x1 )
		AssignHavocCmd R10:21
		AssumeExpCmd Eq(R10:21 0x2 )
		AssignHavocCmd R11:22
		AssumeExpCmd Eq(R11:22 0x4 )
		AssignHavocCmd CANON4:46
		AssumeExpCmd LAnd(Ge(CANON4:46 0x0(int) ) Le(CANON4:46 0xffffffffffffffffffffffffffffffffffffffff(int) ) )
		AssignHavocCmd CANON5:47
		AssumeExpCmd Eq(CANON5:47 0x0(int) )
		AssignHavocCmd CANON6:48
		AssumeExpCmd LAnd(Ge(CANON6:48 0x0(int) ) Le(CANON6:48 0xffffffffffffffffffffffffffffffffffffffff(int) ) )
		AssignHavocCmd CANON7:49
		AssumeExpCmd LAnd(Ge(CANON7:49 0x0(int) ) Le(CANON7:49 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff(int) ) )
		AssignHavocCmd CANON8:50
		AssumeExpCmd LAnd(Ge(CANON8:50 0x0(int) ) Le(CANON8:50 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff(int) ) )
		AssignHavocCmd CANON9:51
		AssumeExpCmd LAnd(Ge(CANON9:51 0x0(int) ) Le(CANON9:51 0xffffffffffffffffffffffffffffffffffffffff(int) ) )
		AssignHavocCmd R12:23
		AssumeExpCmd LAnd(Ge(R12:23 0x1 ) Le(R12:23 0xffffffffffffffffffffffffffffffffffffffff ) )
		AssignHavocCmd tacSighash!!13:52
		AssumeExpCmd Eq(tacSighash!!13:52 0x771602f7 )
		AssignHavocCmd tacSighash!!14:52
		AssumeExpCmd Eq(tacSighash!!14:52 0xeee97206 )
		AssignHavocCmd tacSighash!!15:52
		AssumeExpCmd Eq(tacSighash!!15:52 0x31b6bd06 )
		AnnotationCmd JSON{"key":{"name":"tac.state.extension","type":"analysis.icfg.Inliner$ExtendedStateVars","erasureStrategy":"Canonical"},"value":"rO0ABXNyACdhbmFseXNpcy5pY2ZnLklubGluZXIkRXh0ZW5kZWRTdGF0ZVZhcnOvh/MjxNFkQAIAAUwAFmluc3RhbmNlVG9FeHRlbmRlZFZhcnN0AA9MamF2YS91dGlsL01hcDt4cHNyACFkYXRhc3RydWN0dXJlcy5MaW5rZWRBcnJheUhhc2hNYXAAAAAAAAAAAQMAAkYACmxvYWRGYWN0b3JMAAloYXNoVGFibGV0AC5MZGF0YXN0cnVjdHVyZXMvYXJyYXloYXNodGFibGUvQXJyYXlIYXNoVGFibGU7eHB3CAAAAAFAAAAAc3IAFGphdmEubWF0aC5CaWdJbnRlZ2VyjPyfH6k7+x0DAAZJAAhiaXRDb3VudEkACWJpdExlbmd0aEkAE2ZpcnN0Tm9uemVyb0J5dGVOdW1JAAxsb3dlc3RTZXRCaXRJAAZzaWdudW1bAAltYWduaXR1ZGV0AAJbQnhyABBqYXZhLmxhbmcuTnVtYmVyhqyVHQuU4IsCAAB4cP///////////////v////4AAAABdXIAAltCrPMX+AYIVOACAAB4cAAAABDORgSgAAAAAAAAAAAAAAABeHNxAH4AA3cIAAAAAEAAAAB4eA=="}
		AnnotationCmd:53 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"rule parameters setup"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":0}
		AnnotationCmd:54 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"Setup"}}
		AnnotationCmd:55 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"multi contract setup"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":2}
		AnnotationCmd:56 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"contract address vars initialized"}}
		AssignExpCmd CANON!!16:25 R12:57
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":3}
		AnnotationCmd:58 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"setup read tracking instrumentation"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":4}
		AnnotationCmd:59 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"last storage initialize"}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule"}},{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.NonTACKeywordEntry","name":"lastStorage"}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":5}
		AnnotationCmd:60 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assuming contracts in scene with non-empty bytecode have EXTCODESIZE larger than zero"}}
		AssignExpCmd R17:20 Select(tacExtcodesize!!4:7 Apply(to_skey:bif R12:57) )
		AssumeExpCmd Ge(R17:20 0x1 )
		AssumeExpCmd Eq(R17:61 R3:62 )
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":6}
		AnnotationCmd:63 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assuming address(0).code has no code deployed"}}
		AssignExpCmd B19:20 Eq(Select(tacExtcodesize!!4:7 Apply(skey_basic:bif 0x0) ) 0x0 )
		AssumeCmd B19:20 "expToAssumeCmd"
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":7}
		AnnotationCmd:64 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about contracts' addresses"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":8}
		AnnotationCmd:65 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about static addresses"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":9}
		AnnotationCmd:66 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"establish addresses of precompiled contracts"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":10}
		AnnotationCmd:67 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"assumptions about uniqueness of contracts' addresses"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":11}
		AnnotationCmd:68 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"static links"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":12}
		AnnotationCmd:69 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"record starting nonces"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":13}
		AnnotationCmd:70 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"cloned contracts have no balances"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":14}
		AnnotationCmd:71 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"Linked immutable setup"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":15}
		AnnotationCmd:72 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"Constrain immutables"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":16}
		AnnotationCmd:73 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Message","s":"establish equivalence of extension and base contract immutables"}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":17}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1}
		AnnotationCmd:74 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Declaration","range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":32,"charByteOffset":4},"end":{"line":32,"charByteOffset":10}},"cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"id":"e","scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AnnotationCmd JSON{"key":{"name":"cvl.trace.declaration","type":"spec.CVLCompiler$Companion$TraceMeta$VariableDeclaration","erasureStrategy":"Erased"},"value":{"v":{"#class":"spec.CVLCompiler.Companion.TraceMeta.ValueIdentity.CVLVar","id":"e186"},"t":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"type":{"#class":"spec.CVLCompiler.Companion.TraceMeta.DeclarationType.Variable"},"fields":[[{"#class":"tac.DataField.StructField","field":"block"},{"#class":"tac.DataField.StructField","field":"coinbase"}],{"namePrefix":"CANON9","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"fields":[{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":32,"charByteOffset":4},"end":{"line":32,"charByteOffset":10}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"e.block.coinbase"}]},[{"#class":"tac.DataField.StructField","field":"block"},{"#class":"tac.DataField.StructField","field":"basefee"}],{"namePrefix":"CANON7","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"fields":[{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":32,"charByteOffset":4},"end":{"line":32,"charByteOffset":10}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"e.block.basefee"}]},[{"#class":"tac.DataField.StructField","field":"block"},{"#class":"tac.DataField.StructField","field":"timestamp"}],{"namePrefix":"CANON13","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"fields":[{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":32,"charByteOffset":4},"end":{"line":32,"charByteOffset":10}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"e.block.timestamp"}]},[{"#class":"tac.DataField.StructField","field":"block"},{"#class":"tac.DataField.StructField","field":"blobbasefee"}],{"namePrefix":"CANON8","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"fields":[{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":32,"charByteOffset":4},"end":{"line":32,"charByteOffset":10}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"e.block.blobbasefee"}]},[{"#class":"tac.DataField.StructField","field":"tx"},{"#class":"tac.DataField.StructField","field":"origin"}],{"namePrefix":"CANON6","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"fields":[{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":32,"charByteOffset":4},"end":{"line":32,"charByteOffset":10}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"e.tx.origin"}]},[{"#class":"tac.DataField.StructField","field":"msg"},{"#class":"tac.DataField.StructField","field":"sender"}],{"namePrefix":"CANON4","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":32,"charByteOffset":4},"end":{"line":32,"charByteOffset":10}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"e.msg.sender"}]},[{"#class":"tac.DataField.StructField","field":"msg"},{"#class":"tac.DataField.StructField","field":"value"}],{"namePrefix":"CANON5","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":32,"charByteOffset":4},"end":{"line":32,"charByteOffset":10}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"e.msg.value"}]},[{"#class":"tac.DataField.StructField","field":"block"},{"#class":"tac.DataField.StructField","field":"difficulty"}],{"namePrefix":"CANON10","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"fields":[{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":32,"charByteOffset":4},"end":{"line":32,"charByteOffset":10}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"e.block.difficulty"}]},[{"#class":"tac.DataField.StructField","field":"block"},{"#class":"tac.DataField.StructField","field":"gaslimit"}],{"namePrefix":"CANON11","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"fields":[{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":32,"charByteOffset":4},"end":{"line":32,"charByteOffset":10}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"e.block.gaslimit"}]},[{"#class":"tac.DataField.StructField","field":"block"},{"#class":"tac.DataField.StructField","field":"number"}],{"namePrefix":"CANON12","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.struct.path","type":"spec.cvlast.CVLStructPathNode","erasureStrategy":"CallTrace"},"value":{"rootStructType":{"name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"fields":[{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":32,"charByteOffset":4},"end":{"line":32,"charByteOffset":10}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"e.block.number"}]}]}}
		AnnotationCmd:75 JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":18}
		AnnotationCmd:76 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Definition","range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":33,"charByteOffset":4},"end":{"line":33,"charByteOffset":20}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"idL":[{"#class":"spec.cvlast.CVLLhs.Id","range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":33,"charByteOffset":4},"end":{"line":33,"charByteOffset":15}},"id":"num","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":33,"charByteOffset":4},"end":{"line":33,"charByteOffset":15}}}}],"exp":{"#class":"spec.cvlast.CVLExp.Constant.NumberLit","n":"5","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral","n":"5"},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":33,"charByteOffset":18},"end":{"line":33,"charByteOffset":19}}}},"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssignExpCmd:77 CANON14:31 0x5
		AnnotationCmd:78 JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":19}
		AnnotationCmd:79 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Declaration","range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":34,"charByteOffset":4},"end":{"line":34,"charByteOffset":14}},"cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"id":"t","scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AnnotationCmd JSON{"key":{"name":"cvl.trace.declaration","type":"spec.CVLCompiler$Companion$TraceMeta$VariableDeclaration","erasureStrategy":"Erased"},"value":{"v":{"#class":"spec.CVLCompiler.Companion.TraceMeta.ValueIdentity.TACVar","t":{"namePrefix":"CANON15","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule","range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":34,"charByteOffset":4},"end":{"line":34,"charByteOffset":14}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"t"}]}},"t":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"type":{"#class":"spec.CVLCompiler.Companion.TraceMeta.DeclarationType.Variable"},"fields":null}}
		AnnotationCmd:80 JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":20}
		AnnotationCmd:81 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Definition","range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":35,"charByteOffset":4},"end":{"line":35,"charByteOffset":24}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"idL":[{"#class":"spec.cvlast.CVLLhs.Id","range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":35,"charByteOffset":4},"end":{"line":35,"charByteOffset":14}},"id":"r1","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":35,"charByteOffset":4},"end":{"line":35,"charByteOffset":14}}}}],"exp":{"#class":"spec.cvlast.CVLExp.ApplyExp.CVLFunction","id":"func","args":[],"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":35,"charByteOffset":17},"end":{"line":35,"charByteOffset":23}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.CVLFunction","range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":24,"charByteOffset":0},"end":{"line":29,"charByteOffset":1}},"declarationId":"func","params":[],"rets":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"block":[{"cmd_type":"spec.cvlast.CVLCmd.Simple.Definition","range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":25,"charByteOffset":4},"end":{"line":25,"charByteOffset":21}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"idL":[{"#class":"spec.cvlast.CVLLhs.Id","range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":25,"charByteOffset":4},"end":{"line":25,"charByteOffset":15}},"id":"num","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":4}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":null,"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":25,"charByteOffset":4},"end":{"line":25,"charByteOffset":15}}}}],"exp":{"#class":"spec.cvlast.CVLExp.Constant.NumberLit","n":"a","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":4}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":null,"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":25,"charByteOffset":18},"end":{"line":25,"charByteOffset":20}}}},"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":4}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}},{"cmd_type":"spec.cvlast.CVLCmd.Simple.Definition","range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":26,"charByteOffset":4},"end":{"line":26,"charByteOffset":21}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"idL":[{"#class":"spec.cvlast.CVLLhs.Id","range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":26,"charByteOffset":4},"end":{"line":26,"charByteOffset":15}},"id":"ret","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":4}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":null,"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":26,"charByteOffset":4},"end":{"line":26,"charByteOffset":15}}}}],"exp":{"#class":"spec.cvlast.CVLExp.Constant.NumberLit","n":"14","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":4}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":null,"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":26,"charByteOffset":18},"end":{"line":26,"charByteOffset":20}}}},"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":4}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}},{"cmd_type":"spec.cvlast.CVLCmd.Simple.AssumeCmd.Assume","range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":27,"charByteOffset":4},"end":{"line":27,"charByteOffset":22}},"exp":{"#class":"spec.cvlast.CVLExp.RelopExp.ArithRelopExp.GtExp","l":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"ret","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":4}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":null,"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":27,"charByteOffset":12},"end":{"line":27,"charByteOffset":15}}},"twoStateIndex":"NEITHER"},"r":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"num","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":4}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":null,"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":27,"charByteOffset":18},"end":{"line":27,"charByteOffset":21}}},"twoStateIndex":"NEITHER"},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":4}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":null,"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":27,"charByteOffset":12},"end":{"line":27,"charByteOffset":21}}}},"description":null,"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":4}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}},{"cmd_type":"spec.cvlast.CVLCmd.Simple.Return","range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":28,"charByteOffset":4},"end":{"line":28,"charByteOffset":15}},"exps":[{"#class":"spec.cvlast.CVLExp.VariableExp","id":"ret","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":4}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":null,"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":28,"charByteOffset":11},"end":{"line":28,"charByteOffset":14}}},"twoStateIndex":"NEITHER"}],"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":4}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}],"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":4}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}},"noRevert":true},"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
	}
	Block 1_0_0_1_0_1 Succ [2_0_0_0_0_0] {
		AnnotationCmd:82 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.CVLSnippetCmd.CVLFunctionStart","callIndex":1,"name":"func","range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":35,"charByteOffset":17},"end":{"line":35,"charByteOffset":23}},"isNoRevert":true}}
		AnnotationCmd:83 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Definition","range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":25,"charByteOffset":4},"end":{"line":25,"charByteOffset":21}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"idL":[{"#class":"spec.cvlast.CVLLhs.Id","range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":25,"charByteOffset":4},"end":{"line":25,"charByteOffset":15}},"id":"num","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":4}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":25,"charByteOffset":4},"end":{"line":25,"charByteOffset":15}}}}],"exp":{"#class":"spec.cvlast.CVLExp.Constant.NumberLit","n":"a","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":4}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral","n":"a"},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":25,"charByteOffset":18},"end":{"line":25,"charByteOffset":20}}}},"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":4}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssignExpCmd:84 CANON16:33 0xa
		AnnotationCmd:85 JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":22}
		AnnotationCmd:86 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Definition","range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":26,"charByteOffset":4},"end":{"line":26,"charByteOffset":21}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"idL":[{"#class":"spec.cvlast.CVLLhs.Id","range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":26,"charByteOffset":4},"end":{"line":26,"charByteOffset":15}},"id":"ret","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":4}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":26,"charByteOffset":4},"end":{"line":26,"charByteOffset":15}}}}],"exp":{"#class":"spec.cvlast.CVLExp.Constant.NumberLit","n":"14","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":4}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral","n":"14"},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":26,"charByteOffset":18},"end":{"line":26,"charByteOffset":20}}}},"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":4}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssignExpCmd:87 CANON17:34 0x14
		AnnotationCmd:88 JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":23}
		AnnotationCmd:89 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.AssumeCmd.Assume","range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":27,"charByteOffset":4},"end":{"line":27,"charByteOffset":22}},"exp":{"#class":"spec.cvlast.CVLExp.RelopExp.ArithRelopExp.GtExp","l":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"ret","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":4}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":27,"charByteOffset":12},"end":{"line":27,"charByteOffset":15}}},"twoStateIndex":"NEITHER"},"r":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"num","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":4}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":27,"charByteOffset":18},"end":{"line":27,"charByteOffset":21}}},"twoStateIndex":"NEITHER"},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":4}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":27,"charByteOffset":12},"end":{"line":27,"charByteOffset":21}}}},"description":null,"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":4}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssignExpCmd:90 I20 0x14(int)
		AssignExpCmd:91 I21 0xa(int)
		AssignExpCmd:92 B22 true
		AnnotationCmd:93 JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":24}
		AssignExpCmd:94 I23 0x14(int)
		AnnotationCmd:95 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Return","stmt":{"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":28,"charByteOffset":4},"end":{"line":28,"charByteOffset":15}},"exps":[{"#class":"spec.cvlast.CVLExp.VariableExp","id":"ret","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":4}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":28,"charByteOffset":11},"end":{"line":28,"charByteOffset":14}}},"twoStateIndex":"NEITHER"}],"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":4}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.CVLSnippetCmd.CVLRet.PrimitiveRet","callIndex":1,"index":0,"sym":{"namePrefix":"I23","tag":{"#class":"tac.Tag.Int"},"callIndex":0},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"label":{"stmt":{"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":28,"charByteOffset":4},"end":{"line":28,"charByteOffset":15}},"exps":[{"#class":"spec.cvlast.CVLExp.VariableExp","id":"ret","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":4}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":28,"charByteOffset":11},"end":{"line":28,"charByteOffset":14}}},"twoStateIndex":"NEITHER"}],"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":4}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}}
		AssignExpCmd:82 CANON22:35 0x14(int)
		AnnotationCmd:82 JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":25}
		AnnotationCmd:82 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.CVLSnippetCmd.CVLFunctionEnd","callIndex":1,"name":"func"}}
		AnnotationCmd:82 JSON{"key":{"name":"revert.confluence","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd:82 "join point of revert handling"
	}
	Block 2_0_0_0_0_0 Succ [3_0_0_2_0_0] {
		AnnotationCmd:82 JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":21}
		AnnotationCmd:96 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Definition","range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":36,"charByteOffset":4},"end":{"line":36,"charByteOffset":30}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"idL":[{"#class":"spec.cvlast.CVLLhs.Id","range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":36,"charByteOffset":4},"end":{"line":36,"charByteOffset":14}},"id":"r2","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":36,"charByteOffset":4},"end":{"line":36,"charByteOffset":14}}}}],"exp":{"#class":"spec.cvlast.CVLExp.ApplyExp.ContractFunction.Concrete","methodIdWithCallContext":{"#class":"spec.cvlast.ConcreteMethod","signature":{"#class":"spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig","wrapped":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"TestContract"},"methodId":"add"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"a","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}},{"#class":"spec.cvlast.VMParam.Named","name":"b","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}]},"sighashInt":{"n":"771602f7"}}},"args":[{"#class":"spec.cvlast.CVLExp.VariableExp","id":"e","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":36,"charByteOffset":21},"end":{"line":36,"charByteOffset":22}}},"twoStateIndex":"NEITHER"},{"#class":"spec.cvlast.CVLExp.Constant.NumberLit","n":"4","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral","n":"4"},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":36,"charByteOffset":24},"end":{"line":36,"charByteOffset":25}}}},{"#class":"spec.cvlast.CVLExp.Constant.NumberLit","n":"5","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral","n":"5"},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":36,"charByteOffset":27},"end":{"line":36,"charByteOffset":28}}}}],"noRevert":true,"storage":{"id":"lastStorage","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"},"range":{"#class":"utils.Range.Empty","comment":"empty storage type"}},"twoStateIndex":"NEITHER"},"isWhole":false,"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.VM","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"context":{"#class":"spec.cvlast.typedescriptors.FromVMContext.ReturnValue"}},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":36,"charByteOffset":17},"end":{"line":36,"charByteOffset":29}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.CallResolution$DirectPassing","target":{"methodSignature":{"#class":"spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig","wrapped":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"TestContract"},"methodId":"add"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"a","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}},{"#class":"spec.cvlast.VMParam.Named","name":"b","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}]},"sighashInt":{"n":"771602f7"}},"definitelyNonPayable":true,"annotation":{"visibility":"EXTERNAL","envFree":false,"library":false,"virtual":false},"stateMutability":"nonpayable","evmExternalMethodInfo":{"sigHash":"771602f7","name":"add","argTypes":[{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}],"resultTypes":[{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}],"stateMutability":"nonpayable","isConstant":false,"paramNames":["a","b"],"isLibrary":false,"contractName":"TestContract","contractInstanceId":"ce4604a0000000000000000000000001","sourceSegment":{"range":{"specFile":"TestContract.sol","start":{"line":5,"charByteOffset":4},"end":{"line":7,"charByteOffset":5}},"content":"function add(uint256 a, uint256 b) public returns (uint256) {\n        return a + b;\n    }"}}},"hasEnv":true}}},"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AnnotationCmd JSON{"key":{"name":"cvl.trace.data.movement","type":"spec.CVLCompiler$Companion$TraceMeta$CVLMovement","erasureStrategy":"Erased"},"value":{"dst":{"id":"certoraArg202203"},"src":{"id":"e186"}}}
		AssignExpCmd:97 I25 0x4
		AssignExpCmd:98 I26 0x5
	}
	Block 3_0_0_2_0_0 Succ [4_0_0_3_0_2] {
		AssignHavocCmd:99 CANON26!!27:36
		AnnotationCmd:99 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":{"callee":{"contractId":"ce4604a0000000000000000000000001","sigHash":{"n":"771602f7"},"attr":{"#class":"scene.MethodAttribute.Common"}},"summary":null,"convention":{"#class":"analysis.icfg.Inliner.CallConventionType.FromCVL"},"calleeId":2}}
		AssignHavocCmd:99 tacCalldatasize!!28:9
		AssumeExpCmd Eq(tacCalldatasize!!28:9 0x44 )
		AssignExpCmd:99 tacCalldatabuf@2:14 MapDefinition(CANON27.598:bv256 -> Ite(Lt(CANON27.598 tacCalldatasize!!28:9 ) Select(Select(Select(CANON28!7:26 CANON27.598 ) tacCalldatasize!!28:9 ) 0x771602f7 ) 0x0 ) bytemap)
		AssignExpCmd:99 R29:20 Select(Select(Select(CANON28!7:26 0x0 ) 0x44 ) 0x771602f7 )
		AssumeExpCmd LAnd(Ge(R29:20 0x771602f700000000000000000000000000000000000000000000000000000000 ) Le(R29:20 0x771602f7ffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) )
		AnnotationCmd:99 JSON{"key":{"name":"cvl.arg-serialization.start","type":"spec.CVLInvocationCompiler$StartSerializationMarker","erasureStrategy":"Canonical"},"value":{"id":0,"callId":2}}
		LabelCmd:99 "1: Read primitive from certoraArg204205:int..."
		AssertCmd:100 true "sanity bounds check on cvl to vm encoding (unsigned int elements of a user array) of %1$s failed"
		AssertCmd:100 true "sanity bounds check on cvl to vm encoding (unsigned int elements of a user array) of %1$s failed"
		AssignExpCmd:99 tacCalldatabufCANON0@2:2 0x4
		LabelCmd:99 "...done 1"
		AnnotationCmd JSON{"key":{"name":"cvl.trace.external","type":"spec.CVLCompiler$Companion$TraceMeta$ExternalArg","erasureStrategy":"Erased"},"value":{"s":{"#class":"spec.CVLCompiler.Companion.TraceMeta.ValueIdentity.TACVar","t":{"namePrefix":"I25","tag":{"#class":"tac.Tag.Int"},"callIndex":0}},"rootOffset":"0","callId":2,"targetType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"sourceType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral","n":"4"},"fields":null}}
		LabelCmd:99 "2: Read primitive from certoraArg206207:int..."
		AssertCmd:101 true "sanity bounds check on cvl to vm encoding (unsigned int elements of a user array) of %1$s failed"
		AssertCmd:101 true "sanity bounds check on cvl to vm encoding (unsigned int elements of a user array) of %1$s failed"
		AssignExpCmd:99 tacCalldatabufCANON1@2:3 0x5
		LabelCmd:99 "...done 2"
		AnnotationCmd JSON{"key":{"name":"cvl.trace.external","type":"spec.CVLCompiler$Companion$TraceMeta$ExternalArg","erasureStrategy":"Erased"},"value":{"s":{"#class":"spec.CVLCompiler.Companion.TraceMeta.ValueIdentity.TACVar","t":{"namePrefix":"I26","tag":{"#class":"tac.Tag.Int"},"callIndex":0}},"rootOffset":"20","callId":2,"targetType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"sourceType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral","n":"5"},"fields":null}}
		AnnotationCmd:99 JSON{"key":{"name":"cvl.arg-serialization.end","type":"spec.CVLInvocationCompiler$EndSerializationMarker","erasureStrategy":"Canonical"},"value":{"id":0,"callId":2}}
		AssignExpCmd:99 lastHasThrown!!30:45 false
		AssertCmd:102 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:103 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:104 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:105 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:106 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:107 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:108 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:109 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:110 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:111 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:112 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:113 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssignExpCmd:99 R32:20 Apply(safe_math_narrow_bv256:bif CANON4:46)
		AssignExpCmd:99 R34:20 Select(tacBalance!!5:13 Apply(to_skey:bif R32:20) )
		AssignExpCmd:114 tacBalance!!36:13 Store(tacBalance!!5:13 Apply(to_skey:bif R32:20) R34:20 )
		AssignExpCmd:99 R37:20 Select(tacBalance!!36:13 Apply(to_skey:bif R12:57) )
		AssignExpCmd:114 R39:20 Apply(safe_math_narrow_bv256:bif R37:20)
		AssignExpCmd:114 tacBalance!!40:13 Store(tacBalance!!36:13 Apply(to_skey:bif R12:57) R39:20 )
		AnnotationCmd:99 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.TransferSnippet","srcAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R34","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R34","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R32","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}},"trgAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R37","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R39","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R12","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.NonTACKeywordEntry","name":"tacContractAt"}},{"key":{"name":"tac.contract.sym.addr.name","type":"java.lang.String","erasureStrategy":"Erased"},"value":"TestContract"},{"key":{"name":"tac.contract.sym.addr","type":"java.math.BigInteger","erasureStrategy":"Erased"},"value":"ce4604a0000000000000000000000001"}]}},"transferredAmount":{"#class":"vc.data.TACSymbol.Const","value":"0"}}}
		LabelCmd:99 "Start procedure TestContract-add(uint256,uint256)"
		AnnotationCmd:99 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:99 R41:20 Select(tacExtcodesize!!4:7 Apply(to_skey:bif R12:115) )
		AssumeExpCmd Ge(R41:20 0x1 )
		AnnotationCmd:99 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.RawStorageAccess.WithLocSym","isLoad":true,"loc":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R12","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"tacAddress","maybeTACKeywordOrdinal":22}},{"key":{"name":"tac.env.known-bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.contract.sym.addr.name","type":"java.lang.String","erasureStrategy":"Erased"},"value":"TestContract"},{"key":{"name":"tac.contract.sym.addr","type":"java.math.BigInteger","erasureStrategy":"Erased"},"value":"ce4604a0000000000000000000000001"}]},"contractInstance":"ce4604a0000000000000000000000001","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R41","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"storageType":null,"range":null}}
		AnnotationCmd:99 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":{"unresolvedFunctions":[]}}
		AnnotationCmd:99 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AnnotationCmd:99 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":0,"bytecodeCount":8,"sources":[{"source":0,"begin":25,"end":2021}]}}
		LabelCmd "→ Assuming FP is strictly monotonic increasing"
		LabelCmd "←"
		AnnotationCmd:99 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.StartBranchSnippet","branchIndex":0,"branchSource":{"range":{"specFile":"TestContract.sol","start":{"line":2,"charByteOffset":0},"end":{"line":24,"charByteOffset":1}},"content":"contract TestContract {...}"}}}
		AnnotationCmd:99 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.EndBranchSnippet","branchIndex":0}}
		AnnotationCmd:116 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":16,"bytecodeCount":7,"sources":[{"source":0,"begin":25,"end":2021}]}}
		AnnotationCmd:116 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":26,"bytecodeCount":9,"sources":[{"source":0,"begin":25,"end":2021}]}}
		AnnotationCmd:116 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":43,"bytecodeCount":5,"sources":[{"source":0,"begin":25,"end":2021}]}}
		AnnotationCmd:116 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":54,"bytecodeCount":5,"sources":[{"source":0,"begin":25,"end":2021}]}}
		AnnotationCmd:116 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":150,"bytecodeCount":14,"sources":[{"source":0,"begin":75,"end":500}]}}
		AnnotationCmd:117 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":1105,"bytecodeCount":11,"sources":[{"source":1,"begin":420,"end":827},{"source":1,"begin":488,"end":494},{"source":1,"begin":496,"end":502},{"source":1,"begin":545,"end":547},{"source":1,"begin":533,"end":542},{"source":1,"begin":524,"end":531},{"source":1,"begin":520,"end":543},{"source":1,"begin":516,"end":548},{"source":1,"begin":513,"end":515}]}}
		AnnotationCmd:99 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.StartBranchSnippet","branchIndex":1,"branchSource":{"range":{"specFile":"TestContract.sol","start":{"line":5,"charByteOffset":4},"end":{"line":7,"charByteOffset":5}},"content":"compiler-generate condition in function add(uint256 a, uint256 b) public returns (uint256) "}}}
		AnnotationCmd:99 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.EndBranchSnippet","branchIndex":1}}
		AnnotationCmd:99 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":1124,"bytecodeCount":9,"sources":[{"source":1,"begin":513,"end":515},{"source":1,"begin":604,"end":605},{"source":1,"begin":629,"end":682},{"source":1,"begin":674,"end":681},{"source":1,"begin":665,"end":671},{"source":1,"begin":654,"end":663},{"source":1,"begin":650,"end":672}]}}
		AnnotationCmd:99 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":1043,"bytecodeCount":10,"sources":[{"source":1,"begin":7,"end":146},{"source":1,"begin":53,"end":58},{"source":1,"begin":91,"end":97},{"source":1,"begin":78,"end":98},{"source":1,"begin":69,"end":98},{"source":1,"begin":107,"end":140},{"source":1,"begin":134,"end":139}]}}
		AnnotationCmd:99 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":1440,"bytecodeCount":5,"sources":[{"source":1,"begin":2119,"end":2241},{"source":1,"begin":2192,"end":2216},{"source":1,"begin":2210,"end":2215}]}}
		AnnotationCmd:99 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":1383,"bytecodeCount":9,"sources":[{"source":1,"begin":1850,"end":1927},{"source":1,"begin":1887,"end":1894},{"source":1,"begin":1916,"end":1921},{"source":1,"begin":1905,"end":1921},{"source":1,"begin":1895,"end":1927}]}}
		AnnotationCmd:99 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":1449,"bytecodeCount":5,"sources":[{"source":1,"begin":2192,"end":2216},{"source":1,"begin":2185,"end":2190},{"source":1,"begin":2182,"end":2217},{"source":1,"begin":2172,"end":2174}]}}
		AnnotationCmd:99 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":1460,"bytecodeCount":3,"sources":[{"source":1,"begin":2172,"end":2174},{"source":1,"begin":2162,"end":2241}]}}
		AnnotationCmd:99 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":1058,"bytecodeCount":6,"sources":[{"source":1,"begin":107,"end":140},{"source":1,"begin":59,"end":146}]}}
		AnnotationCmd:99 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":1138,"bytecodeCount":12,"sources":[{"source":1,"begin":629,"end":682},{"source":1,"begin":619,"end":682},{"source":1,"begin":575,"end":692},{"source":1,"begin":731,"end":733},{"source":1,"begin":757,"end":810},{"source":1,"begin":802,"end":809},{"source":1,"begin":793,"end":799},{"source":1,"begin":782,"end":791},{"source":1,"begin":778,"end":800}]}}
		AnnotationCmd:99 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":1043,"bytecodeCount":10,"sources":[{"source":1,"begin":7,"end":146},{"source":1,"begin":53,"end":58},{"source":1,"begin":91,"end":97},{"source":1,"begin":78,"end":98},{"source":1,"begin":69,"end":98},{"source":1,"begin":107,"end":140},{"source":1,"begin":134,"end":139}]}}
		AnnotationCmd:99 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":1440,"bytecodeCount":5,"sources":[{"source":1,"begin":2119,"end":2241},{"source":1,"begin":2192,"end":2216},{"source":1,"begin":2210,"end":2215}]}}
		AnnotationCmd:99 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":1383,"bytecodeCount":9,"sources":[{"source":1,"begin":1850,"end":1927},{"source":1,"begin":1887,"end":1894},{"source":1,"begin":1916,"end":1921},{"source":1,"begin":1905,"end":1921},{"source":1,"begin":1895,"end":1927}]}}
		AnnotationCmd:99 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":1449,"bytecodeCount":5,"sources":[{"source":1,"begin":2192,"end":2216},{"source":1,"begin":2185,"end":2190},{"source":1,"begin":2182,"end":2217},{"source":1,"begin":2172,"end":2174}]}}
		AnnotationCmd:99 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":1460,"bytecodeCount":3,"sources":[{"source":1,"begin":2172,"end":2174},{"source":1,"begin":2162,"end":2241}]}}
		AnnotationCmd:99 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":1058,"bytecodeCount":6,"sources":[{"source":1,"begin":107,"end":140},{"source":1,"begin":59,"end":146}]}}
		AnnotationCmd:99 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":1155,"bytecodeCount":10,"sources":[{"source":1,"begin":757,"end":810},{"source":1,"begin":747,"end":810},{"source":1,"begin":702,"end":820},{"source":1,"begin":503,"end":827}]}}
		AnnotationCmd:99 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":171,"bytecodeCount":3,"sources":[{"source":0,"begin":75,"end":500}]}}
		JumpCmd 4_0_0_3_0_2
	}
	Block 4_0_0_3_0_2 Succ [5_0_0_2_0_0] {
		AnnotationCmd JSON{"key":{"name":"call.trace.internal.summary.start","type":"analysis.icfg.SummaryStack$SummaryStart$Internal","erasureStrategy":"CallTrace"},"value":"rO0ABXNyADBhbmFseXNpcy5pY2ZnLlN1bW1hcnlTdGFjayRTdW1tYXJ5U3RhcnQkSW50ZXJuYWwlfWFJE7iemQIABkwADmFwcGxpZWRTdW1tYXJ5dAAsTGFuYWx5c2lzL2ljZmcvU3VtbWFyaXphdGlvbiRBcHBsaWVkU3VtbWFyeTtMABdjYWxsUmVzb2x1dGlvblRhYmxlSW5mb3QANkxyZXBvcnQvY2FsbHJlc29sdXRpb24vQ2FsbFJlc29sdXRpb25UYWJsZVN1bW1hcnlJbmZvO0wAC2NhbGxTaXRlU3JjdAAVTHZjL2RhdGEvVEFDTWV0YUluZm87TAAPbWV0aG9kU2lnbmF0dXJldAAmTHNwZWMvY3ZsYXN0L1F1YWxpZmllZE1ldGhvZFNpZ25hdHVyZTtMAARyZXRzdAAQTGphdmEvdXRpbC9MaXN0O0wAB3N1cHBvcnR0AA9MamF2YS91dGlsL1NldDt4cgAnYW5hbHlzaXMuaWNmZy5TdW1tYXJ5U3RhY2skU3VtbWFyeVN0YXJ0zo/b071HRz0CAAB4cHNyADdhbmFseXNpcy5pY2ZnLlN1bW1hcml6YXRpb24kQXBwbGllZFN1bW1hcnkkTWV0aG9kc0Jsb2NrxBlpQb2eQrwCAAJMAAxzcGVjQ2FsbFN1bW10AC5Mc3BlYy9jdmxhc3QvU3BlY0NhbGxTdW1tYXJ5JEV4cHJlc3NpYmxlSW5DVkw7TAAQc3VtbWFyaXplZE1ldGhvZHQAG0xzcGVjL0NWTCRTdW1tYXJ5U2lnbmF0dXJlO3hwc3IAH3NwZWMuY3ZsYXN0LlNwZWNDYWxsU3VtbWFyeSRFeHCItcAI/3pVHwIAB0wAA2V4cHQAFExzcGVjL2N2bGFzdC9DVkxFeHA7TAAMZXhwZWN0ZWRUeXBlcQB+AAVMAAlmdW5QYXJhbXNxAH4ABUwABXJhbmdldAANTHV0aWxzL1JhbmdlO0wABXNjb3BldAAWTHNwZWMvY3ZsYXN0L0NWTFNjb3BlO0wAEXN1bW1hcml6YXRpb25Nb2RldAAvTHNwZWMvY3ZsYXN0L1NwZWNDYWxsU3VtbWFyeSRTdW1tYXJpemF0aW9uTW9kZTtMAAp3aXRoQ2xhdXNldAAsTHNwZWMvY3ZsYXN0L1NwZWNDYWxsU3VtbWFyeSRFeHAkV2l0aENsYXVzZTt4cgAsc3BlYy5jdmxhc3QuU3BlY0NhbGxTdW1tYXJ5JEV4cHJlc3NpYmxlSW5DVkw5jBEFxNlONwIAAHhyABtzcGVjLmN2bGFzdC5TcGVjQ2FsbFN1bW1hcnmf4QieXcWlAQIAAHhwc3IAJ3NwZWMuY3ZsYXN0LkNWTEV4cCRBcHBseUV4cCRDVkxGdW5jdGlvbghf8sf20DA6AgAFWgAIbm9SZXZlcnRMAARhcmdzcQB+AAVMAAJpZHQAEkxqYXZhL2xhbmcvU3RyaW5nO0wAF21ldGhvZElkV2l0aENhbGxDb250ZXh0dAAdTHNwZWMvY3ZsYXN0L1NwZWNEZWNsYXJhdGlvbjtMAAN0YWd0ABdMc3BlYy9jdmxhc3QvQ1ZMRXhwVGFnO3hyABtzcGVjLmN2bGFzdC5DVkxFeHAkQXBwbHlFeHAF3JlNR+1SuwIAAHhyACFzcGVjLmN2bGFzdC5DVkxFeHAkQXBwbGljYXRpb25FeHAEe7zFegP5fQIAAHhyABJzcGVjLmN2bGFzdC5DVkxFeHAB+J/cNeGTiAIAAHhwAXNyABNqYXZhLnV0aWwuQXJyYXlMaXN0eIHSHZnHYZ0DAAFJAARzaXpleHAAAAACdwQAAAACc3IAHnNwZWMuY3ZsYXN0LkNWTEV4cCRWYXJpYWJsZUV4cJ0ULkp52IKNAgAETAACaWRxAH4AF0wADG9yaWdpbmFsTmFtZXEAfgAXTAADdGFncQB+ABlMAA10d29TdGF0ZUluZGV4dAAbTHNwZWMvY3ZsYXN0L1R3b1N0YXRlSW5kZXg7eHEAfgAcdAABYXEAfgAjc3IAFXNwZWMuY3ZsYXN0LkNWTEV4cFRhZ9WLKphaC/tTAgAFWgAJaGFzUGFyZW5zTAAKYW5ub3RhdGlvbnQAIkxzcGVjL2N2bGFzdC9FeHByZXNzaW9uQW5ub3RhdGlvbjtMAAVyYW5nZXEAfgAPTAAFc2NvcGVxAH4AEEwABHR5cGV0ABVMc3BlYy9jdmxhc3QvQ1ZMVHlwZTt4cABwc3IAEXV0aWxzLlJhbmdlJFJhbmdlelevcoxEsQYCAANMAANlbmR0ABZMdXRpbHMvU291cmNlUG9zaXRpb247TAAIc3BlY0ZpbGVxAH4AF0wABXN0YXJ0cQB+ACl4cgALdXRpbHMuUmFuZ2XoA/TylWV/VwIAAHhwc3IAFHV0aWxzLlNvdXJjZVBvc2l0aW9ulfTn1OqZxI0CAAJJAA5jaGFyQnl0ZU9mZnNldEkABGxpbmV4cAAAAFsAAAABdAAKQmFzaWMuc3BlY3NxAH4ALAAAAFoAAAABc3IAFHNwZWMuY3ZsYXN0LkNWTFNjb3BlIslgWNQdXVQCAANMABZoYXNoQ29kZUNhY2hlJGRlbGVnYXRldAANTGtvdGxpbi9MYXp5O0wACmlubmVyU2NvcGVxAH4AEEwACnNjb3BlU3RhY2txAH4ABXhwc3IAGmtvdGxpbi5Jbml0aWFsaXplZExhenlJbXBse8d/8SAqgY0CAAFMAAV2YWx1ZXQAEkxqYXZhL2xhbmcvT2JqZWN0O3hwc3IAEWphdmEubGFuZy5JbnRlZ2VyEuKgpPeBhzgCAAFJAAV2YWx1ZXhyABBqYXZhLmxhbmcuTnVtYmVyhqyVHQuU4IsCAAB4cMzxqF9zcQB+ADBzcQB+ADNzcQB+ADZOZ41hc3EAfgAwc3EAfgAzc3EAfgA2AAAAH3BzcgAca290bGluLmNvbGxlY3Rpb25zLkVtcHR5TGlzdJlvx9Cn4GAyAgAAeHBzcgAjamF2YS51dGlsLkNvbGxlY3Rpb25zJFNpbmdsZXRvbkxpc3Qq7ykQPKeblwIAAUwAB2VsZW1lbnRxAH4ANHhwc3IAJnNwZWMuY3ZsYXN0LkNWTFNjb3BlJEl0ZW0kQXN0U2NvcGVJdGVth5un9wbVoZMCAAB4cgAZc3BlYy5jdmxhc3QuQ1ZMU2NvcGUkSXRlbS8Dr/+eN1ZFAgAAeHBzcQB+AB4AAAACdwQAAAACcQB+AEVzcgArc3BlYy5jdmxhc3QuQ1ZMU2NvcGUkSXRlbSRFeHByZXNzaW9uU3VtbWFyeQ8zGp1aX6loAgABSQAHc2NvcGVJZHhyAClzcGVjLmN2bGFzdC5DVkxTY29wZSRJdGVtJEFTVEVsZW1lbnRTY29wZVKrjxFR5CKWAgABTAAHZWxlbWVudHQAGkxzcGVjL2N2bGFzdC9DcmVhdGVzU2NvcGU7eHEAfgBEc3EAfgANc3IAJXNwZWMuY3ZsYXN0LkNWTEV4cCRVbnJlc29sdmVkQXBwbHlFeHA1PheCG7l9yAIACFoADGludm9rZUlzU2FmZVoADWludm9rZUlzV2hvbGVMAARhcmdzcQB+AAVMAARiYXNlcQB+AA5MAA1pbnZva2VTdG9yYWdldAAgTHNwZWMvY3ZsYXN0L0NWTEV4cCRWYXJpYWJsZUV4cDtMAAhtZXRob2RJZHEAfgAXTAADdGFncQB+ABlMAA10d29TdGF0ZUluZGV4cQB+ACF4cQB+ABsBAHNxAH4AHgAAAAJ3BAAAAAJzcQB+ACBxAH4AI3EAfgAjc3EAfgAkAHBxAH4AK3EAfgAycH5yABlzcGVjLmN2bGFzdC5Ud29TdGF0ZUluZGV4AAAAAAAAAAASAAB4cgAOamF2YS5sYW5nLkVudW0AAAAAAAAAABIAAHhwdAAHTkVJVEhFUnNxAH4AIHQAAWJxAH4AV3NxAH4AJABwc3EAfgAoc3EAfgAsAAAAXgAAAAFxAH4ALnNxAH4ALAAAAF0AAAABcQB+ADJwcQB+AFR4cHNxAH4AIHQAC2xhc3RTdG9yYWdlcQB+AF1zcQB+ACQAcHNyABF1dGlscy5SYW5nZSRFbXB0ecSDHpJeeJXXAgABTAAHY29tbWVudHEAfgAXeHEAfgAqdAASZW1wdHkgc3RvcmFnZSB0eXBlcQB+ADJwcQB+AFR0AAdjdmxfYWRkc3EAfgAkAHBzcQB+AChzcQB+ACwAAABfAAAAAXEAfgAuc3EAfgAsAAAAUgAAAAFxAH4AMnBxAH4AVHBzcQB+AB4AAAACdwQAAAACc3IAGXNwZWMuY3ZsYXN0LlZNUGFyYW0kTmFtZWQAXezwjrrQjQIABEwABG5hbWVxAH4AF0wADG9yaWdpbmFsTmFtZXEAfgAXTAAFcmFuZ2VxAH4AD0wABnZtVHlwZXQALkxzcGVjL2N2bGFzdC90eXBlZGVzY3JpcHRvcnMvVk1UeXBlRGVzY3JpcHRvcjt4cgATc3BlYy5jdmxhc3QuVk1QYXJhbaA5qID7MF6/AgAAeHBxAH4AI3EAfgAjc3EAfgAoc3EAfgAsAAAAJwAAAAFxAH4ALnNxAH4ALAAAAB4AAAABc3IAM3NwZWMuY3ZsYXN0LnR5cGVkZXNjcmlwdG9ycy5FVk1UeXBlRGVzY3JpcHRvciRVSW50S6h6LEsweg4lAgABSQAIYml0d2lkdGh4cgBEc3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yJEVWTUlzb21vcnBoaWNWYWx1ZVR5cGWW45V3at3xfwIAAHhyADpzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkRVZNVmFsdWVUeXBlEOTS9aivN+ECAAB4cgAtc3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yXlYd3MaOPugCAAB4cAAAAQBzcQB+AGhxAH4AV3EAfgBXc3EAfgAoc3EAfgAsAAAAMgAAAAFxAH4ALnNxAH4ALAAAACkAAAABc3EAfgBvAAABAHhzcQB+AChzcQB+ACwAAABfAAAAAXEAfgAuc3EAfgAsAAAAUgAAAAFxAH4AMn5yAC1zcGVjLmN2bGFzdC5TcGVjQ2FsbFN1bW1hcnkkU3VtbWFyaXphdGlvbk1vZGUAAAAAAAAAABIAAHhxAH4AU3QAA0FMTHAAAAAAeHNyABZzcGVjLmN2bGFzdC5DVkxUeXBlJFZNo6s7LR18330CAAJMAAdjb250ZXh0dAArTHNwZWMvY3ZsYXN0L3R5cGVkZXNjcmlwdG9ycy9Gcm9tVk1Db250ZXh0O0wACmRlc2NyaXB0b3JxAH4AaXhyABNzcGVjLmN2bGFzdC5DVkxUeXBldDETlbfBZVACAAB4cHNyAENzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRnJvbVZNQ29udGV4dCRJbnRlcm5hbFN1bW1hcnlBcmdCaW5kaW5nnsXkzwE/iScCAAB4cgApc3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkZyb21WTUNvbnRleHTF2vGG93fwZQIAAHhwcQB+AHNxAH4AVHNxAH4AIHEAfgBXcQB+AFdzcQB+ACQAcHEAfgBZcQB+ADJzcQB+AH9xAH4AhXEAfgB4cQB+AFR4cQB+AGJzcgAbc3BlYy5jdmxhc3QuU3BlY0RlY2xhcmF0aW9ujRb0DzyoobcCAAFMAAhtZXRob2RJZHEAfgAXeHBxAH4AYnNxAH4AJABzcgAXc3BlYy5jdmxhc3QuQ1ZMRnVuY3Rpb24uWdWoiYfIYQIACUwABWJsb2NrcQB+AAVMAA1kZWNsYXJhdGlvbklkcQB+ABdMABJmdW5jdGlvbklkZW50aWZpZXJxAH4AGEwACnBhcmFtVHlwZXNxAH4ABUwABnBhcmFtc3EAfgAFTAAFcmFuZ2VxAH4AD0wABHJldHN0ACFMc3BlYy9jdmxhc3QvQ1ZMVHlwZSRQdXJlQ1ZMVHlwZTtMAAVzY29wZXEAfgAQTAAPdHlwZURlc2NyaXB0aW9ucQB+ABd4cHNxAH4AHgAAAAF3BAAAAAFzcgAgc3BlYy5jdmxhc3QuQ1ZMQ21kJFNpbXBsZSRSZXR1cm5noLos6RDbuAIABEwAB2NtZE5hbWVxAH4AF0wABGV4cHNxAH4ABUwABXJhbmdlcQB+AA9MAAVzY29wZXEAfgAQeHIAGXNwZWMuY3ZsYXN0LkNWTENtZCRTaW1wbGWA/5FLCuaTSAIAAHhyABJzcGVjLmN2bGFzdC5DVkxDbWR9T7T2R5OokgIAAHhwdAAGcmV0dXJuc3EAfgAeAAAAAXcEAAAAAXNyABtzcGVjLmN2bGFzdC5DVkxFeHAkQ2FzdEV4cHIWyHePH2zcnwIABUwAA2FyZ3EAfgAOTAAIY2FzdFR5cGV0AA9Mc3BlYy9DYXN0VHlwZTtMAAxpbkNWTEJsb2NrSWR0ABNMamF2YS9sYW5nL0ludGVnZXI7TAADdGFncQB+ABlMAAp0b0Nhc3RUeXBlcQB+AI14cQB+ABxzcgAjc3BlYy5jdmxhc3QuQ1ZMRXhwJEJpbmFyeUV4cCRBZGRFeHDJHdelRwemfQIAA0wAAWxxAH4ADkwAAXJxAH4ADkwAA3RhZ3EAfgAZeHIAHHNwZWMuY3ZsYXN0LkNWTEV4cCRCaW5hcnlFeHCSEZ+AH8oBJgIAAHhxAH4AHHNxAH4AIHEAfgAjcQB+ACNzcQB+ACQAcHNxAH4AKHNxAH4ALAAAABwAAAAMcQB+AC5zcQB+ACwAAAAbAAAADHNxAH4AMHNxAH4AM3NxAH4ANszxqLxxAH4AOXNxAH4AHgAAAAJ3BAAAAAJxAH4ARXNyAC5zcGVjLmN2bGFzdC5DVkxTY29wZSRJdGVtJENWTEZ1bmN0aW9uU2NvcGVJdGVte1vIQGGDSjkCAAFJAAdzY29wZUlkeHEAfgBIc3EAfgCMc3EAfgAeAAAAAXcEAAAAAXNxAH4AkHEAfgCUc3EAfgAeAAAAAXcEAAAAAXNxAH4AlnNxAH4AmnNxAH4AIHEAfgAjcQB+ACNxAH4AnnEAfgBUc3EAfgAgcQB+AFdxAH4AV3NxAH4AJABwc3EAfgAoc3EAfgAsAAAAIAAAAAxxAH4ALnNxAH4ALAAAAB8AAAAMcQB+AKJwcQB+AFRzcQB+ACQAcHNxAH4AKHNxAH4ALAAAACAAAAAMcQB+AC5zcQB+ACwAAAAbAAAADHEAfgCicH5yAA1zcGVjLkNhc3RUeXBlAAAAAAAAAAASAAB4cQB+AFN0AAdSRVFVSVJFcHNxAH4AJABwc3EAfgAoc3EAfgAsAAAAIAAAAAxxAH4ALnNxAH4ALAAAAAsAAAAMcQB+AKJwc3IAL3NwZWMuY3ZsYXN0LkNWTFR5cGUkUHVyZUNWTFR5cGUkUHJpbWl0aXZlJFVJbnRLuQuajikSRikCAAJJAAhiaXRXaWR0aEkAAWt4cgApc3BlYy5jdmxhc3QuQ1ZMVHlwZSRQdXJlQ1ZMVHlwZSRQcmltaXRpdmUKm9v/NH7COwIAAHhyAB9zcGVjLmN2bGFzdC5DVkxUeXBlJFB1cmVDVkxUeXBl/Qa0FlO2KLECAAB4cQB+AIEAAAEAAAABAHhzcQB+AChzcQB+ACwAAAAiAAAADHEAfgAuc3EAfgAsAAAABAAAAAxxAH4AonhxAH4AYnNxAH4AiXEAfgBic3EAfgAeAAAAAncEAAAAAnNxAH4AvwAAAQAAAAEAc3EAfgC/AAABAAAAAQB4c3EAfgAeAAAAAncEAAAAAnNyABRzcGVjLmN2bGFzdC5DVkxQYXJhbZUgQywsLU7ZAgAETAACaWRxAH4AF0wACm9yaWdpbmFsSWRxAH4AF0wABXJhbmdlcQB+AA9MAAR0eXBlcQB+AI14cHEAfgAjcQB+ACNzcQB+AChzcQB+ACwAAAAaAAAAC3EAfgAuc3EAfgAsAAAAEQAAAAtxAH4AyHNxAH4Ay3EAfgBXcQB+AFdzcQB+AChzcQB+ACwAAAAlAAAAC3EAfgAuc3EAfgAsAAAAHAAAAAtxAH4AyXhzcQB+AChzcQB+ACwAAAABAAAADXEAfgAuc3EAfgAsAAAAAAAAAAtzcQB+AL8AAAEAAAABAHEAfgCidAAMQ1ZMIGZ1bmN0aW9uAAAAA3hwcQB+AFRzcQB+ACBxAH4AV3EAfgBXcQB+ALBxAH4AVHEAfgC0cQB+ALlwcQB+ALtxAH4AwnhxAH4Aw3EAfgCieHEAfgBic3EAfgCJcQB+AGJzcQB+AB4AAAACdwQAAAACcQB+AMhxAH4AyXhzcQB+AB4AAAACdwQAAAACcQB+AMxxAH4A0HhxAH4A1HEAfgDXcQB+AKJxAH4A2HEAfgBkcQB+ADJxAH4A13BzcQB+AB4AAAACdwQAAAACcQB+AGtxAH4AdHhxAH4AeXEAfgAycQB+AH1wc3IAFnNwZWMuQ1ZMJEludGVybmFsRXhhY3SF/Egh8I7sYAIAAUwACXNpZ25hdHVyZXQAL0xzcGVjL2N2bGFzdC9RdWFsaWZpZWRNZXRob2RQYXJhbWV0ZXJTaWduYXR1cmU7eHBzcgA3c3BlYy5jdmxhc3QuUXVhbGlmaWVkTWV0aG9kU2lnbmF0dXJlJFF1YWxpZmllZE1ldGhvZFNpZxh9TLRtHWz1AgADTAAGcGFyYW1zcQB+AAVMABNxdWFsaWZpZWRNZXRob2ROYW1ldAAoTHNwZWMvY3ZsYXN0L0NvbnRyYWN0RnVuY3Rpb25JZGVudGlmaWVyO0wAA3Jlc3EAfgAFeHBxAH4AZ3NyAB1zcGVjLmN2bGFzdC5RdWFsaWZpZWRGdW5jdGlvbuUpTPLkOVGDAgACTAAEaG9zdHQAHkxzcGVjL2N2bGFzdC9Tb2xpZGl0eUNvbnRyYWN0O0wACG1ldGhvZElkcQB+ABd4cHNyABxzcGVjLmN2bGFzdC5Tb2xpZGl0eUNvbnRyYWN0I2l9dxqBPaICAAFMAARuYW1lcQB+ABd4cHQADFRlc3RDb250cmFjdHQAA2FkZHNxAH4AHgAAAAF3BAAAAAFzcgAbc3BlYy5jdmxhc3QuVk1QYXJhbSRVbm5hbWVkQM3mz745puMCAAJMAAVyYW5nZXEAfgAPTAAGdm1UeXBlcQB+AGl4cQB+AGpzcQB+AChzcQB+ACwAAABNAAAAAXEAfgAuc3EAfgAsAAAARgAAAAFzcQB+AG8AAAEAeHNyAEByZXBvcnQuY2FsbHJlc29sdXRpb24uQ2FsbFJlc29sdXRpb25UYWJsZVN1bW1hcnlJbmZvJERlZmF1bHRJbmZv3XK/8JXJObUCAAFMABFhcHBsaWNhdGlvblJlYXNvbnQAKExhbmFseXNpcy9pY2ZnL1N1bW1hcnlBcHBsaWNhdGlvblJlYXNvbjt4cgA0cmVwb3J0LmNhbGxyZXNvbHV0aW9uLkNhbGxSZXNvbHV0aW9uVGFibGVTdW1tYXJ5SW5mbxq20EbaZsyGAgABTAANaW5mbyRkZWxlZ2F0ZXEAfgAxeHBzcQB+ADNzcgAhZGF0YXN0cnVjdHVyZXMuTGlua2VkQXJyYXlIYXNoTWFwAAAAAAAAAAEDAAJGAApsb2FkRmFjdG9yTAAJaGFzaFRhYmxldAAuTGRhdGFzdHJ1Y3R1cmVzL2FycmF5aGFzaHRhYmxlL0FycmF5SGFzaFRhYmxlO3hwdwgAAAABQAAAAHQAGnN1bW1hcnkgYXBwbGljYXRpb24gcmVhc29udAA/ZGVjbGFyZWQgYXQgQmFzaWMuc3BlYzoyOjgzIHRvIGFwcGx5IHRvIGFsbCBjYWxscyB0byB0aGUgY2FsbGVleHNyAC9hbmFseXNpcy5pY2ZnLlN1bW1hcnlBcHBsaWNhdGlvblJlYXNvbiRTcGVjJEFsbDVbfdlUEwDtAgACTAADbG9jcQB+AA9MAA9tZXRob2RTaWduYXR1cmVxAH4AF3hyACthbmFseXNpcy5pY2ZnLlN1bW1hcnlBcHBsaWNhdGlvblJlYXNvbiRTcGVjnk8P0pteLB0CAAB4cgAmYW5hbHlzaXMuaWNmZy5TdW1tYXJ5QXBwbGljYXRpb25SZWFzb25CnD+iq+g4mgIAAHhwcQB+AHl0ABVhZGQodWludDI1NiwgdWludDI1NilzcgATdmMuZGF0YS5UQUNNZXRhSW5mb0W7USKtClXbAgAGSQAFYmVnaW5JAANsZW5JAAZzb3VyY2VMAAdhZGRyZXNzdAAWTGphdmEvbWF0aC9CaWdJbnRlZ2VyO0wACGp1bXBUeXBldAATTGNvbXBpbGVyL0p1bXBUeXBlO0wADXNvdXJjZUNvbnRleHR0ABhMY29tcGlsZXIvU291cmNlQ29udGV4dDt4cAAAAEsAAAGpAAAAAHNyABRqYXZhLm1hdGguQmlnSW50ZWdlcoz8nx+pO/sdAwAGSQAIYml0Q291bnRJAAliaXRMZW5ndGhJABNmaXJzdE5vbnplcm9CeXRlTnVtSQAMbG93ZXN0U2V0Qml0SQAGc2lnbnVtWwAJbWFnbml0dWRldAACW0J4cQB+ADf///////////////7////+AAAAAXVyAAJbQqzzF/gGCFTgAgAAeHAAAAAQzkYEoAAAAAAAAAAAAAAAAXh+cgARY29tcGlsZXIuSnVtcFR5cGUAAAAAAAAAABIAAHhxAH4AU3QABUVOVEVSc3IAFmNvbXBpbGVyLlNvdXJjZUNvbnRleHSDeLXeEWLWywIAAkwAD2luZGV4VG9GaWxlUGF0aHQAD0xqYXZhL3V0aWwvTWFwO0wACXNvdXJjZURpcnEAfgAXeHBzcQB+APd3CAAAAAFAAAAAc3EAfgA2AAAAAHQAEFRlc3RDb250cmFjdC5zb2x4dAATLnBvc3RfYXV0b2ZpbmRlcnMuMHNxAH4A4XNxAH4AHgAAAAJ3BAAAAAJzcQB+AGhxAH4AI3EAfgAjc3EAfgBfdAAAc3EAfgBvAAABAHNxAH4AaHEAfgBXcQB+AFdzcQB+AF9xAH4BGXNxAH4AbwAAAQB4c3EAfgDkc3EAfgDncQB+AOlxAH4A6nNxAH4AHgAAAAF3BAAAAAFzcQB+AOxzcQB+AF9xAH4BGXNxAH4AbwAAAQB4c3EAfgAeAAAAAXcEAAAAAXNyABthbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmNSZXTkicRVatvZJgIAA0kABm9mZnNldEwACGxvY2F0aW9udAAnTGFuYWx5c2lzL2lwL0ludGVybmFsRnVuY1ZhbHVlTG9jYXRpb247TAABc3QAF0x2Yy9kYXRhL1RBQ1N5bWJvbCRWYXI7eHAAAAAAc3IALGFuYWx5c2lzLmlwLkludGVybmFsRnVuY1ZhbHVlTG9jYXRpb24kU2NhbGFy6tL+3ru/KPUCAAB4cgAlYW5hbHlzaXMuaXAuSW50ZXJuYWxGdW5jVmFsdWVMb2NhdGlvbmyMCp1I2e37AgAAeHBzcgAadmMuZGF0YS5UQUNTeW1ib2wkVmFyJEZ1bGzTyzRM0mPeYgIABEkACWNhbGxJbmRleEwABG1ldGF0AB5MY29tL2NlcnRvcmEvY29sbGVjdC9UcmVhcE1hcDtMAApuYW1lUHJlZml4cQB+ABdMAAN0YWd0AAlMdGFjL1RhZzt4cgAVdmMuZGF0YS5UQUNTeW1ib2wkVmFy/Ehr1L4wRhECAAB4cgARdmMuZGF0YS5UQUNTeW1ib2wSkyLY56xy1AIAAHhwAAAAAnNyACBjb20uY2VydG9yYS5jb2xsZWN0Lkhhc2hUcmVhcE1hcM4n+3qupXKcAgADTAADa2V5cQB+ADRMAARuZXh0dAArTGNvbS9jZXJ0b3JhL2NvbGxlY3QvS2V5VmFsdWVQYWlyTGlzdCRNb3JlO0wABXZhbHVlcQB+ADR4cgAkY29tLmNlcnRvcmEuY29sbGVjdC5BYnN0cmFjdFRyZWFwTWFwLW7dR2hNBhkCAAB4cgAZY29tLmNlcnRvcmEuY29sbGVjdC5UcmVhcP/ew+O23D8jAgACTAAEbGVmdHQAG0xjb20vY2VydG9yYS9jb2xsZWN0L1RyZWFwO0wABXJpZ2h0cQB+ATZ4cHNxAH4BMnBwc3IAC3RhYy5NZXRhS2V5avYXikOyot0CAANMAA9lcmFzdXJlU3RyYXRlZ3l0AB1MdGFjL01ldGFLZXkkRXJhc3VyZVN0cmF0ZWd5O0wABG5hbWVxAH4AF0wAA3R5cHQAEUxqYXZhL2xhbmcvQ2xhc3M7eHB+cgAbdGFjLk1ldGFLZXkkRXJhc3VyZVN0cmF0ZWd5AAAAAAAAAAASAAB4cQB+AFN0AAlDYW5vbmljYWx0ABJUYWMuc3ltYm9sLmtleXdvcmR2cgAidmMuZGF0YS5UQUNTeW1ib2wkVmFyJEtleXdvcmRFbnRyeU7jwOQ0dtx2AgAAeHBwc3IAMnZjLmRhdGEuVEFDU3ltYm9sJFZhciRLZXl3b3JkRW50cnkkVEFDS2V5d29yZEVudHJ5uJkWjywELK0CAAJJABZtYXliZVRBQ0tleXdvcmRPcmRpbmFsTAAEbmFtZXEAfgAXeHEAfgFBAAAALXQAAUxwc3EAfgE5cQB+AT50ABB0YWMuc3RhY2suaGVpZ2h0dnEAfgA2cHNxAH4ANgAAA/90AANSNDVzcgAOdGFjLlRhZyRCaXQyNTYMJPutC/yioAIAAHhyAAx0YWMuVGFnJEJpdHONlhh3aSMLmAIABkkACGJpdHdpZHRoTAAJbWF4U2lnbmVkcQB+AQJMAAttYXhVbnNpZ25lZHEAfgECTAALbWluU2lnbmVkMnNxAH4BAkwADW1pblNpZ25lZE1hdGhxAH4BAkwAB21vZHVsdXNxAH4BAnhyAAd0YWMuVGFneiXiZp1BxfUCAAB4cAAAAQBzcQB+AQb///////////////7////+AAAAAXVxAH4BCQAAACB//////////////////////////////////////////3hzcQB+AQb///////////////7////+AAAAAXVxAH4BCQAAACD//////////////////////////////////////////3hzcQB+AQb///////////////7////+AAAAAXVxAH4BCQAAACCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHhzcQB+AQb///////////////7////+/////3VxAH4BCQAAACCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHhzcQB+AQb///////////////7////+AAAAAXVxAH4BCQAAACEBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB4eHNyABtrb3RsaW4uY29sbGVjdGlvbnMuRW1wdHlTZXQvRrAVdtfi9AIAAHhw"}
		AssignExpCmd calledContract!!42:10 R12:57
		AssignExpCmd executingContract!!43:44 R12:57
		AssignExpCmd CANON!!44:25 R12:57
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.CVLSnippetCmd.CVLFunctionStart","callIndex":4,"name":"cvl_add","range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":1,"charByteOffset":82},"end":{"line":1,"charByteOffset":95}},"isNoRevert":true}}
		LabelCmd "9: Move primitive value for variable a498499:int..."
		LabelCmd "...done 9"
		AssignExpCmd CANON51:37 0x4(int)
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.CVLSnippetCmd.CVLArg.PrimitiveArg","callIndex":4,"index":0,"sym":{"namePrefix":"CANON51","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Function","range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":11,"charByteOffset":17},"end":{"line":11,"charByteOffset":26}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"a"}]},"param":{"Named_type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"id":"a","range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":11,"charByteOffset":17},"end":{"line":11,"charByteOffset":26}}}}}
		LabelCmd "10: Move primitive value for variable b500501:int..."
		LabelCmd "...done 10"
		AssignExpCmd CANON52:38 0x5(int)
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.CVLSnippetCmd.CVLArg.PrimitiveArg","callIndex":4,"index":1,"sym":{"namePrefix":"CANON52","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Function","range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":11,"charByteOffset":28},"end":{"line":11,"charByteOffset":37}}}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"b"}]},"param":{"Named_type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"id":"b","range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":11,"charByteOffset":28},"end":{"line":11,"charByteOffset":37}}}}}
		AssignExpCmd:118 I45 0x4(int)
		AssignExpCmd:119 I46 0x5(int)
		AssignExpCmd:120 I47 0x9(int)
		AssignExpCmd:121 I48 0x9(int)
		AnnotationCmd:122 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Return","stmt":{"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":12,"charByteOffset":4},"end":{"line":12,"charByteOffset":34}},"exps":[{"#class":"spec.cvlast.CVLExp.CastExpr","toCastType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"arg":{"#class":"spec.cvlast.CVLExp.BinaryExp.AddExp","l":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"a","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":3}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":12,"charByteOffset":27},"end":{"line":12,"charByteOffset":28}}},"twoStateIndex":"NEITHER"},"r":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"b","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":3}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":12,"charByteOffset":31},"end":{"line":12,"charByteOffset":32}}},"twoStateIndex":"NEITHER"},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":3}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":12,"charByteOffset":27},"end":{"line":12,"charByteOffset":32}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":3}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":12,"charByteOffset":11},"end":{"line":12,"charByteOffset":32}}},"castType":"REQUIRE","inCVLBlockId":1}],"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":3}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.CVLSnippetCmd.CVLRet.PrimitiveRet","callIndex":4,"index":0,"sym":{"namePrefix":"I48","tag":{"#class":"tac.Tag.Int"},"callIndex":0},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"label":{"stmt":{"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":12,"charByteOffset":4},"end":{"line":12,"charByteOffset":34}},"exps":[{"#class":"spec.cvlast.CVLExp.CastExpr","toCastType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"arg":{"#class":"spec.cvlast.CVLExp.BinaryExp.AddExp","l":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"a","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":3}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":12,"charByteOffset":27},"end":{"line":12,"charByteOffset":28}}},"twoStateIndex":"NEITHER"},"r":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"b","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":3}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":12,"charByteOffset":31},"end":{"line":12,"charByteOffset":32}}},"twoStateIndex":"NEITHER"},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":3}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":12,"charByteOffset":27},"end":{"line":12,"charByteOffset":32}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":3}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":12,"charByteOffset":11},"end":{"line":12,"charByteOffset":32}}},"castType":"REQUIRE","inCVLBlockId":1}],"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.CVLFunctionScopeItem","scopeId":3}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}}
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":27}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.CVLSnippetCmd.CVLFunctionEnd","callIndex":4,"name":"cvl_add"}}
		AnnotationCmd JSON{"key":{"name":"revert.confluence","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		LabelCmd "join point of revert handling"
		LabelCmd "8: Read primitive from tmp494495:int..."
		AssertCmd:123 true "sanity bounds check on cvl to vm encoding (unsigned int elements of a user array) of %1$s failed"
		AssignExpCmd R49:24 0x9
		LabelCmd "...done 8"
		AnnotationCmd JSON{"key":{"name":"call.trace.internal.summary.end","type":"analysis.icfg.SummaryStack$SummaryEnd$Internal","erasureStrategy":"Canonical"},"value":"rO0ABXNyAC5hbmFseXNpcy5pY2ZnLlN1bW1hcnlTdGFjayRTdW1tYXJ5RW5kJEludGVybmFs/bQ7d/THvhkCAANMAA9tZXRob2RTaWduYXR1cmV0ACZMc3BlYy9jdmxhc3QvUXVhbGlmaWVkTWV0aG9kU2lnbmF0dXJlO0wABHJldHN0ABBMamF2YS91dGlsL0xpc3Q7TAAHc3VwcG9ydHQAD0xqYXZhL3V0aWwvU2V0O3hyACVhbmFseXNpcy5pY2ZnLlN1bW1hcnlTdGFjayRTdW1tYXJ5RW5kFZQmA8fWa+kCAAB4cHNyADdzcGVjLmN2bGFzdC5RdWFsaWZpZWRNZXRob2RTaWduYXR1cmUkUXVhbGlmaWVkTWV0aG9kU2lnGH1MtG0dbPUCAANMAAZwYXJhbXNxAH4AAkwAE3F1YWxpZmllZE1ldGhvZE5hbWV0AChMc3BlYy9jdmxhc3QvQ29udHJhY3RGdW5jdGlvbklkZW50aWZpZXI7TAADcmVzcQB+AAJ4cHNyABNqYXZhLnV0aWwuQXJyYXlMaXN0eIHSHZnHYZ0DAAFJAARzaXpleHAAAAACdwQAAAACc3IAGXNwZWMuY3ZsYXN0LlZNUGFyYW0kTmFtZWQAXezwjrrQjQIABEwABG5hbWV0ABJMamF2YS9sYW5nL1N0cmluZztMAAxvcmlnaW5hbE5hbWVxAH4ADEwABXJhbmdldAANTHV0aWxzL1JhbmdlO0wABnZtVHlwZXQALkxzcGVjL2N2bGFzdC90eXBlZGVzY3JpcHRvcnMvVk1UeXBlRGVzY3JpcHRvcjt4cgATc3BlYy5jdmxhc3QuVk1QYXJhbaA5qID7MF6/AgAAeHB0AAFhcQB+ABFzcgARdXRpbHMuUmFuZ2UkRW1wdHnEgx6SXniV1wIAAUwAB2NvbW1lbnRxAH4ADHhyAAt1dGlscy5SYW5nZegD9PKVZX9XAgAAeHB0AABzcgAzc3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yJFVJbnRLqHosSzB6DiUCAAFJAAhiaXR3aWR0aHhyAERzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkRVZNSXNvbW9ycGhpY1ZhbHVlVHlwZZbjlXdq3fF/AgAAeHIAOnNwZWMuY3ZsYXN0LnR5cGVkZXNjcmlwdG9ycy5FVk1UeXBlRGVzY3JpcHRvciRFVk1WYWx1ZVR5cGUQ5NL1qK834QIAAHhyAC1zcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3JeVh3cxo4+6AIAAHhwAAABAHNxAH4AC3QAAWJxAH4AHHNxAH4AEnEAfgAVc3EAfgAWAAABAHhzcgAdc3BlYy5jdmxhc3QuUXVhbGlmaWVkRnVuY3Rpb27lKUzy5DlRgwIAAkwABGhvc3R0AB5Mc3BlYy9jdmxhc3QvU29saWRpdHlDb250cmFjdDtMAAhtZXRob2RJZHEAfgAMeHBzcgAcc3BlYy5jdmxhc3QuU29saWRpdHlDb250cmFjdCNpfXcagT2iAgABTAAEbmFtZXEAfgAMeHB0AAxUZXN0Q29udHJhY3R0AANhZGRzcQB+AAkAAAABdwQAAAABc3IAG3NwZWMuY3ZsYXN0LlZNUGFyYW0kVW5uYW1lZEDN5s++OabjAgACTAAFcmFuZ2VxAH4ADUwABnZtVHlwZXEAfgAOeHEAfgAPc3EAfgAScQB+ABVzcQB+ABYAAAEAeHNxAH4ACQAAAAF3BAAAAAFzcgAbYW5hbHlzaXMuaXAuSW50ZXJuYWxGdW5jUmV05InEVWrb2SYCAANJAAZvZmZzZXRMAAhsb2NhdGlvbnQAJ0xhbmFseXNpcy9pcC9JbnRlcm5hbEZ1bmNWYWx1ZUxvY2F0aW9uO0wAAXN0ABdMdmMvZGF0YS9UQUNTeW1ib2wkVmFyO3hwAAAAAHNyACxhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmNWYWx1ZUxvY2F0aW9uJFNjYWxhcurS/t67vyj1AgAAeHIAJWFuYWx5c2lzLmlwLkludGVybmFsRnVuY1ZhbHVlTG9jYXRpb25sjAqdSNnt+wIAAHhwc3IANXZjLmRhdGEuVEFDU3ltYm9sJFZhciRXaXRoRGVmYXVsdENhbGxJbmRleCRXaXRoQml0MjU2nq3gkxche2QCAAJMAARtZXRhdAAeTGNvbS9jZXJ0b3JhL2NvbGxlY3QvVHJlYXBNYXA7TAAKbmFtZVByZWZpeHEAfgAMeHIAFXZjLmRhdGEuVEFDU3ltYm9sJFZhcvxIa9S+MEYRAgAAeHIAEXZjLmRhdGEuVEFDU3ltYm9sEpMi2OesctQCAAB4cHNyACBjb20uY2VydG9yYS5jb2xsZWN0Lkhhc2hUcmVhcE1hcM4n+3qupXKcAgADTAADa2V5dAASTGphdmEvbGFuZy9PYmplY3Q7TAAEbmV4dHQAK0xjb20vY2VydG9yYS9jb2xsZWN0L0tleVZhbHVlUGFpckxpc3QkTW9yZTtMAAV2YWx1ZXEAfgA5eHIAJGNvbS5jZXJ0b3JhLmNvbGxlY3QuQWJzdHJhY3RUcmVhcE1hcC1u3UdoTQYZAgAAeHIAGWNvbS5jZXJ0b3JhLmNvbGxlY3QuVHJlYXD/3sPjttw/IwIAAkwABGxlZnR0ABtMY29tL2NlcnRvcmEvY29sbGVjdC9UcmVhcDtMAAVyaWdodHEAfgA9eHBzcQB+ADhwcHNyAAt0YWMuTWV0YUtleWr2F4pDsqLdAgADTAAPZXJhc3VyZVN0cmF0ZWd5dAAdTHRhYy9NZXRhS2V5JEVyYXN1cmVTdHJhdGVneTtMAARuYW1lcQB+AAxMAAN0eXB0ABFMamF2YS9sYW5nL0NsYXNzO3hwfnIAG3RhYy5NZXRhS2V5JEVyYXN1cmVTdHJhdGVneQAAAAAAAAAAEgAAeHIADmphdmEubGFuZy5FbnVtAAAAAAAAAAASAAB4cHQACUNhbm9uaWNhbHQAElRhYy5zeW1ib2wua2V5d29yZHZyACJ2Yy5kYXRhLlRBQ1N5bWJvbCRWYXIkS2V5d29yZEVudHJ5TuPA5DR23HYCAAB4cHBzcgAydmMuZGF0YS5UQUNTeW1ib2wkVmFyJEtleXdvcmRFbnRyeSRUQUNLZXl3b3JkRW50cnm4mRaPLAQsrQIAAkkAFm1heWJlVEFDS2V5d29yZE9yZGluYWxMAARuYW1lcQB+AAx4cQB+AEkAAAAtdAABTHBzcQB+AEBxAH4ARnQAEHRhYy5zdGFjay5oZWlnaHR2cgARamF2YS5sYW5nLkludGVnZXIS4qCk94GHOAIAAUkABXZhbHVleHIAEGphdmEubGFuZy5OdW1iZXKGrJUdC5TgiwIAAHhwcHNxAH4AUAAAA/90AANSNDl4c3IAImphdmEudXRpbC5Db2xsZWN0aW9ucyRTaW5nbGV0b25TZXQsUkGYKcCxvwIAAUwAB2VsZW1lbnRxAH4AOXhwcQB+ADc="}
		JumpCmd 5_0_0_2_0_0
	}
	Block 5_0_0_2_0_0 Succ [6_0_0_0_0_0] {
		AnnotationCmd:124 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":176,"bytecodeCount":8,"sources":[{"source":0,"begin":75,"end":500}]}}
		AnnotationCmd:117 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":1180,"bytecodeCount":14,"sources":[{"source":1,"begin":957,"end":1179},{"source":1,"begin":1050,"end":1054},{"source":1,"begin":1088,"end":1090},{"source":1,"begin":1077,"end":1086},{"source":1,"begin":1073,"end":1091},{"source":1,"begin":1065,"end":1091},{"source":1,"begin":1101,"end":1172},{"source":1,"begin":1169,"end":1170},{"source":1,"begin":1158,"end":1167},{"source":1,"begin":1154,"end":1171},{"source":1,"begin":1145,"end":1151}]}}
		AnnotationCmd:117 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":1165,"bytecodeCount":5,"sources":[{"source":1,"begin":833,"end":951},{"source":1,"begin":920,"end":944},{"source":1,"begin":938,"end":943}]}}
		AnnotationCmd:117 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":1383,"bytecodeCount":9,"sources":[{"source":1,"begin":1850,"end":1927},{"source":1,"begin":1887,"end":1894},{"source":1,"begin":1916,"end":1921},{"source":1,"begin":1905,"end":1921},{"source":1,"begin":1895,"end":1927}]}}
		AnnotationCmd:117 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":1174,"bytecodeCount":6,"sources":[{"source":1,"begin":920,"end":944},{"source":1,"begin":915,"end":918},{"source":1,"begin":908,"end":945},{"source":1,"begin":898,"end":951}]}}
		AnnotationCmd:99 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Const","value":"9"},"callIndex":2}}
		AnnotationCmd:117 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":1201,"bytecodeCount":6,"sources":[{"source":1,"begin":1101,"end":1172},{"source":1,"begin":1055,"end":1179}]}}
		AnnotationCmd:117 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":189,"bytecodeCount":8,"sources":[{"source":0,"begin":75,"end":500}]}}
		AssignExpCmd:125 lastHasThrown!!50:45 false
		AssignExpCmd:125 lastReverted!!51:6 false
		AnnotationCmd:125 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:99 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.HaltSnippet.Return","range":{"specFile":"TestContract.sol","start":{"line":5,"charByteOffset":4},"end":{"line":7,"charByteOffset":5}}}}
		LabelCmd:99 "End procedure TestContract-add(uint256,uint256)"
		LabelCmd:99 "0: Move primitive value for variable r2201:int..."
		AssignExpCmd:99 CANON26!!52:36 0x9
		LabelCmd:99 "...done 0"
		AnnotationCmd:99 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":{"callee":{"contractId":"ce4604a0000000000000000000000001","sigHash":{"n":"771602f7"},"attr":{"#class":"scene.MethodAttribute.Common"}},"calleeId":2}}
	}
	Block 6_0_0_0_0_0 Succ [7_0_0_5_0_0] {
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule"}},{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.NonTACKeywordEntry","name":"lastStorage"}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AnnotationCmd:99 JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":26}
		AnnotationCmd:126 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Definition","range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":37,"charByteOffset":4},"end":{"line":37,"charByteOffset":30}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"idL":[{"#class":"spec.cvlast.CVLLhs.Id","range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":37,"charByteOffset":4},"end":{"line":37,"charByteOffset":14}},"id":"r3","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":37,"charByteOffset":4},"end":{"line":37,"charByteOffset":14}}}}],"exp":{"#class":"spec.cvlast.CVLExp.ApplyExp.ContractFunction.Concrete","methodIdWithCallContext":{"#class":"spec.cvlast.ConcreteMethod","signature":{"#class":"spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig","wrapped":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"TestContract"},"methodId":"double"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"d","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}]},"sighashInt":{"n":"eee97206"}}},"args":[{"#class":"spec.cvlast.CVLExp.VariableExp","id":"e","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"env","fields":[{"fieldName":"msg","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"msg","fields":[{"fieldName":"sender","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"value","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}},{"fieldName":"tx","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"tx","fields":[{"fieldName":"origin","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}}]}},{"fieldName":"block","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Struct","name":"block","fields":[{"fieldName":"basefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"blobbasefee","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"coinbase","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.AccountIdentifier"}},{"fieldName":"difficulty","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"gaslimit","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"number","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"fieldName":"timestamp","cvlType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}}]},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":37,"charByteOffset":24},"end":{"line":37,"charByteOffset":25}}},"twoStateIndex":"NEITHER"},{"#class":"spec.cvlast.CVLExp.Constant.NumberLit","n":"7","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral","n":"7"},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":37,"charByteOffset":27},"end":{"line":37,"charByteOffset":28}}}}],"noRevert":true,"storage":{"id":"lastStorage","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"},"range":{"#class":"utils.Range.Empty","comment":"empty storage type"}},"twoStateIndex":"NEITHER"},"isWhole":false,"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.VM","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"context":{"#class":"spec.cvlast.typedescriptors.FromVMContext.ReturnValue"}},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":37,"charByteOffset":17},"end":{"line":37,"charByteOffset":29}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.CallResolution$DirectPassing","target":{"methodSignature":{"#class":"spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig","wrapped":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"TestContract"},"methodId":"double"},"params":[{"#class":"spec.cvlast.VMParam.Named","name":"d","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}]},"sighashInt":{"n":"eee97206"}},"definitelyNonPayable":true,"annotation":{"visibility":"EXTERNAL","envFree":false,"library":false,"virtual":false},"stateMutability":"nonpayable","evmExternalMethodInfo":{"sigHash":"eee97206","name":"double","argTypes":[{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}],"resultTypes":[{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}],"stateMutability":"nonpayable","isConstant":false,"paramNames":["d"],"isLibrary":false,"contractName":"TestContract","contractInstanceId":"ce4604a0000000000000000000000001","sourceSegment":{"range":{"specFile":"TestContract.sol","start":{"line":9,"charByteOffset":4},"end":{"line":11,"charByteOffset":5}},"content":"function double(uint256 d) public returns (uint256) {\n        return 2 * d;\n    }"}}},"hasEnv":true}}},"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AnnotationCmd JSON{"key":{"name":"cvl.trace.data.movement","type":"spec.CVLCompiler$Companion$TraceMeta$CVLMovement","erasureStrategy":"Erased"},"value":{"dst":{"id":"certoraArg318319"},"src":{"id":"e186"}}}
		AssignExpCmd:127 I54 0x7
	}
	Block 7_0_0_5_0_0 Succ [8_0_0_6_0_0] {
		AssignHavocCmd:128 CANON59!!55:17
		AnnotationCmd:128 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":{"callee":{"contractId":"ce4604a0000000000000000000000001","sigHash":{"n":"eee97206"},"attr":{"#class":"scene.MethodAttribute.Common"}},"summary":null,"convention":{"#class":"analysis.icfg.Inliner.CallConventionType.FromCVL"},"calleeId":5}}
		AssignHavocCmd:128 tacCalldatasize!!56:9
		AssumeExpCmd Eq(tacCalldatasize!!56:9 0x24 )
		AssignExpCmd:128 tacCalldatabuf@5:15 MapDefinition(CANON60.599:bv256 -> Ite(Lt(CANON60.599 tacCalldatasize!!56:9 ) Select(Select(Select(CANON28!7:26 CANON60.599 ) tacCalldatasize!!56:9 ) 0xeee97206 ) 0x0 ) bytemap)
		AssignExpCmd:128 R57:20 Select(Select(Select(CANON28!7:26 0x0 ) 0x24 ) 0xeee97206 )
		AssumeExpCmd LAnd(Ge(R57:20 0xeee9720600000000000000000000000000000000000000000000000000000000 ) Le(R57:20 0xeee97206ffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) )
		AnnotationCmd:128 JSON{"key":{"name":"cvl.arg-serialization.start","type":"spec.CVLInvocationCompiler$StartSerializationMarker","erasureStrategy":"Canonical"},"value":{"id":1,"callId":5}}
		LabelCmd:128 "4: Read primitive from certoraArg320321:int..."
		AssertCmd:129 true "sanity bounds check on cvl to vm encoding (unsigned int elements of a user array) of %1$s failed"
		AssertCmd:129 true "sanity bounds check on cvl to vm encoding (unsigned int elements of a user array) of %1$s failed"
		AssignExpCmd:128 tacCalldatabufCANON0@5:2 0x7
		LabelCmd:128 "...done 4"
		AnnotationCmd JSON{"key":{"name":"cvl.trace.external","type":"spec.CVLCompiler$Companion$TraceMeta$ExternalArg","erasureStrategy":"Erased"},"value":{"s":{"#class":"spec.CVLCompiler.Companion.TraceMeta.ValueIdentity.TACVar","t":{"namePrefix":"I54","tag":{"#class":"tac.Tag.Int"},"callIndex":0}},"rootOffset":"0","callId":5,"targetType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"sourceType":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral","n":"7"},"fields":null}}
		AnnotationCmd:128 JSON{"key":{"name":"cvl.arg-serialization.end","type":"spec.CVLInvocationCompiler$EndSerializationMarker","erasureStrategy":"Canonical"},"value":{"id":1,"callId":5}}
		AssignExpCmd:128 lastHasThrown!!58:45 false
		AssertCmd:130 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:131 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:132 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:133 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:134 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:135 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:136 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:137 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:138 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:139 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:140 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssertCmd:141 true "sanity bounds check on cvl to vm encoding (unsigned int) of %1$s failed"
		AssignExpCmd:128 R60:20 Apply(safe_math_narrow_bv256:bif CANON4:46)
		AssignExpCmd:128 R62:20 Select(tacBalance!!40:13 Apply(to_skey:bif R60:20) )
		AssignExpCmd:142 tacBalance!!64:13 Store(tacBalance!!40:13 Apply(to_skey:bif R60:20) R62:20 )
		AssignExpCmd:128 R65:20 Select(tacBalance!!64:13 Apply(to_skey:bif R12:57) )
		AssignExpCmd:142 R67:20 Apply(safe_math_narrow_bv256:bif R65:20)
		AnnotationCmd:128 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.TransferSnippet","srcAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R62","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R62","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R60","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]}},"trgAccountInfo":{"old":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R65","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"new":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R67","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"addr":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R12","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.NonTACKeywordEntry","name":"tacContractAt"}},{"key":{"name":"tac.contract.sym.addr.name","type":"java.lang.String","erasureStrategy":"Erased"},"value":"TestContract"},{"key":{"name":"tac.contract.sym.addr","type":"java.math.BigInteger","erasureStrategy":"Erased"},"value":"ce4604a0000000000000000000000001"}]}},"transferredAmount":{"#class":"vc.data.TACSymbol.Const","value":"0"}}}
		LabelCmd:128 "Start procedure TestContract-double(uint256)"
		AnnotationCmd:128 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:128 R68:20 Select(tacExtcodesize!!4:7 Apply(to_skey:bif R12:115) )
		AssumeExpCmd Ge(R68:20 0x1 )
		AnnotationCmd:128 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.RawStorageAccess.WithLocSym","isLoad":true,"loc":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R12","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"tacAddress","maybeTACKeywordOrdinal":22}},{"key":{"name":"tac.env.known-bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.contract.sym.addr.name","type":"java.lang.String","erasureStrategy":"Erased"},"value":"TestContract"},{"key":{"name":"tac.contract.sym.addr","type":"java.math.BigInteger","erasureStrategy":"Erased"},"value":"ce4604a0000000000000000000000001"}]},"contractInstance":"ce4604a0000000000000000000000001","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R68","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"storageType":null,"range":null}}
		AnnotationCmd:128 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":{"unresolvedFunctions":[]}}
		AnnotationCmd:128 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AnnotationCmd:128 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":0,"bytecodeCount":8,"sources":[{"source":0,"begin":25,"end":2021}]}}
		LabelCmd "→ Assuming FP is strictly monotonic increasing"
		LabelCmd "←"
		AnnotationCmd:128 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.StartBranchSnippet","branchIndex":2,"branchSource":{"range":{"specFile":"TestContract.sol","start":{"line":2,"charByteOffset":0},"end":{"line":24,"charByteOffset":1}},"content":"contract TestContract {...}"}}}
		AnnotationCmd:128 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.EndBranchSnippet","branchIndex":2}}
		AnnotationCmd:143 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":16,"bytecodeCount":7,"sources":[{"source":0,"begin":25,"end":2021}]}}
		AnnotationCmd:143 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":26,"bytecodeCount":9,"sources":[{"source":0,"begin":25,"end":2021}]}}
		AnnotationCmd:143 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":43,"bytecodeCount":5,"sources":[{"source":0,"begin":25,"end":2021}]}}
		AnnotationCmd:143 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":54,"bytecodeCount":5,"sources":[{"source":0,"begin":25,"end":2021}]}}
		AnnotationCmd:143 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":65,"bytecodeCount":5,"sources":[{"source":0,"begin":25,"end":2021}]}}
		AnnotationCmd:143 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":76,"bytecodeCount":5,"sources":[{"source":0,"begin":25,"end":2021}]}}
		AnnotationCmd:143 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":208,"bytecodeCount":14,"sources":[{"source":0,"begin":506,"end":923}]}}
		AnnotationCmd:144 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":1064,"bytecodeCount":10,"sources":[{"source":1,"begin":152,"end":414},{"source":1,"begin":211,"end":217},{"source":1,"begin":260,"end":262},{"source":1,"begin":248,"end":257},{"source":1,"begin":239,"end":246},{"source":1,"begin":235,"end":258},{"source":1,"begin":231,"end":263},{"source":1,"begin":228,"end":230}]}}
		AnnotationCmd:128 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.StartBranchSnippet","branchIndex":3,"branchSource":{"range":{"specFile":"TestContract.sol","start":{"line":9,"charByteOffset":4},"end":{"line":11,"charByteOffset":5}},"content":"compiler-generate condition in function double(uint256 d) public returns (uint256) "}}}
		AnnotationCmd:128 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.EndBranchSnippet","branchIndex":3}}
		AnnotationCmd:128 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":1082,"bytecodeCount":9,"sources":[{"source":1,"begin":228,"end":230},{"source":1,"begin":319,"end":320},{"source":1,"begin":344,"end":397},{"source":1,"begin":389,"end":396},{"source":1,"begin":380,"end":386},{"source":1,"begin":369,"end":378},{"source":1,"begin":365,"end":387}]}}
		AnnotationCmd:128 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":1043,"bytecodeCount":10,"sources":[{"source":1,"begin":7,"end":146},{"source":1,"begin":53,"end":58},{"source":1,"begin":91,"end":97},{"source":1,"begin":78,"end":98},{"source":1,"begin":69,"end":98},{"source":1,"begin":107,"end":140},{"source":1,"begin":134,"end":139}]}}
		AnnotationCmd:128 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":1440,"bytecodeCount":5,"sources":[{"source":1,"begin":2119,"end":2241},{"source":1,"begin":2192,"end":2216},{"source":1,"begin":2210,"end":2215}]}}
		AnnotationCmd:128 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":1383,"bytecodeCount":9,"sources":[{"source":1,"begin":1850,"end":1927},{"source":1,"begin":1887,"end":1894},{"source":1,"begin":1916,"end":1921},{"source":1,"begin":1905,"end":1921},{"source":1,"begin":1895,"end":1927}]}}
		AnnotationCmd:128 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":1449,"bytecodeCount":5,"sources":[{"source":1,"begin":2192,"end":2216},{"source":1,"begin":2185,"end":2190},{"source":1,"begin":2182,"end":2217},{"source":1,"begin":2172,"end":2174}]}}
		AnnotationCmd:128 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":1460,"bytecodeCount":3,"sources":[{"source":1,"begin":2172,"end":2174},{"source":1,"begin":2162,"end":2241}]}}
		AnnotationCmd:128 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":1058,"bytecodeCount":6,"sources":[{"source":1,"begin":107,"end":140},{"source":1,"begin":59,"end":146}]}}
		AnnotationCmd:128 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":1096,"bytecodeCount":9,"sources":[{"source":1,"begin":344,"end":397},{"source":1,"begin":334,"end":397},{"source":1,"begin":290,"end":407},{"source":1,"begin":218,"end":414}]}}
		AnnotationCmd:128 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":229,"bytecodeCount":3,"sources":[{"source":0,"begin":506,"end":923}]}}
		JumpCmd 8_0_0_6_0_0
	}
	Block 8_0_0_6_0_0 Succ [9_0_0_5_0_0] {
		AnnotationCmd JSON{"key":{"name":"call.trace.internal.summary.start","type":"analysis.icfg.SummaryStack$SummaryStart$Internal","erasureStrategy":"CallTrace"},"value":"rO0ABXNyADBhbmFseXNpcy5pY2ZnLlN1bW1hcnlTdGFjayRTdW1tYXJ5U3RhcnQkSW50ZXJuYWwlfWFJE7iemQIABkwADmFwcGxpZWRTdW1tYXJ5dAAsTGFuYWx5c2lzL2ljZmcvU3VtbWFyaXphdGlvbiRBcHBsaWVkU3VtbWFyeTtMABdjYWxsUmVzb2x1dGlvblRhYmxlSW5mb3QANkxyZXBvcnQvY2FsbHJlc29sdXRpb24vQ2FsbFJlc29sdXRpb25UYWJsZVN1bW1hcnlJbmZvO0wAC2NhbGxTaXRlU3JjdAAVTHZjL2RhdGEvVEFDTWV0YUluZm87TAAPbWV0aG9kU2lnbmF0dXJldAAmTHNwZWMvY3ZsYXN0L1F1YWxpZmllZE1ldGhvZFNpZ25hdHVyZTtMAARyZXRzdAAQTGphdmEvdXRpbC9MaXN0O0wAB3N1cHBvcnR0AA9MamF2YS91dGlsL1NldDt4cgAnYW5hbHlzaXMuaWNmZy5TdW1tYXJ5U3RhY2skU3VtbWFyeVN0YXJ0zo/b071HRz0CAAB4cHNyADdhbmFseXNpcy5pY2ZnLlN1bW1hcml6YXRpb24kQXBwbGllZFN1bW1hcnkkTWV0aG9kc0Jsb2NrxBlpQb2eQrwCAAJMAAxzcGVjQ2FsbFN1bW10AC5Mc3BlYy9jdmxhc3QvU3BlY0NhbGxTdW1tYXJ5JEV4cHJlc3NpYmxlSW5DVkw7TAAQc3VtbWFyaXplZE1ldGhvZHQAG0xzcGVjL0NWTCRTdW1tYXJ5U2lnbmF0dXJlO3hwc3IAH3NwZWMuY3ZsYXN0LlNwZWNDYWxsU3VtbWFyeSRFeHCItcAI/3pVHwIAB0wAA2V4cHQAFExzcGVjL2N2bGFzdC9DVkxFeHA7TAAMZXhwZWN0ZWRUeXBlcQB+AAVMAAlmdW5QYXJhbXNxAH4ABUwABXJhbmdldAANTHV0aWxzL1JhbmdlO0wABXNjb3BldAAWTHNwZWMvY3ZsYXN0L0NWTFNjb3BlO0wAEXN1bW1hcml6YXRpb25Nb2RldAAvTHNwZWMvY3ZsYXN0L1NwZWNDYWxsU3VtbWFyeSRTdW1tYXJpemF0aW9uTW9kZTtMAAp3aXRoQ2xhdXNldAAsTHNwZWMvY3ZsYXN0L1NwZWNDYWxsU3VtbWFyeSRFeHAkV2l0aENsYXVzZTt4cgAsc3BlYy5jdmxhc3QuU3BlY0NhbGxTdW1tYXJ5JEV4cHJlc3NpYmxlSW5DVkw5jBEFxNlONwIAAHhyABtzcGVjLmN2bGFzdC5TcGVjQ2FsbFN1bW1hcnmf4QieXcWlAQIAAHhwc3IAIHNwZWMuY3ZsYXN0LkNWTEV4cCRBcnJheURlcmVmRXhw5CTb4GwIYAYCAANMAAVhcnJheXEAfgAOTAAFaW5kZXhxAH4ADkwAA3RhZ3QAF0xzcGVjL2N2bGFzdC9DVkxFeHBUYWc7eHIAEnNwZWMuY3ZsYXN0LkNWTEV4cAH4n9w14ZOIAgAAeHBzcgAec3BlYy5jdmxhc3QuQ1ZMRXhwJFZhcmlhYmxlRXhwnRQuSnnYgo0CAARMAAJpZHQAEkxqYXZhL2xhbmcvU3RyaW5nO0wADG9yaWdpbmFsTmFtZXEAfgAbTAADdGFncQB+ABdMAA10d29TdGF0ZUluZGV4dAAbTHNwZWMvY3ZsYXN0L1R3b1N0YXRlSW5kZXg7eHEAfgAYdAAMZ2hvc3RfZG91YmxlcQB+AB5zcgAVc3BlYy5jdmxhc3QuQ1ZMRXhwVGFn1YsqmFoL+1MCAAVaAAloYXNQYXJlbnNMAAphbm5vdGF0aW9udAAiTHNwZWMvY3ZsYXN0L0V4cHJlc3Npb25Bbm5vdGF0aW9uO0wABXJhbmdlcQB+AA9MAAVzY29wZXEAfgAQTAAEdHlwZXQAFUxzcGVjL2N2bGFzdC9DVkxUeXBlO3hwAHBzcgARdXRpbHMuUmFuZ2UkUmFuZ2V6V69yjESxBgIAA0wAA2VuZHQAFkx1dGlscy9Tb3VyY2VQb3NpdGlvbjtMAAhzcGVjRmlsZXEAfgAbTAAFc3RhcnRxAH4AJHhyAAt1dGlscy5SYW5nZegD9PKVZX9XAgAAeHBzcgAUdXRpbHMuU291cmNlUG9zaXRpb26V9OfU6pnEjQIAAkkADmNoYXJCeXRlT2Zmc2V0SQAEbGluZXhwAAAAVgAAAAJ0AApCYXNpYy5zcGVjc3EAfgAnAAAASgAAAAJzcgAUc3BlYy5jdmxhc3QuQ1ZMU2NvcGUiyWBY1B1dVAIAA0wAFmhhc2hDb2RlQ2FjaGUkZGVsZWdhdGV0AA1Ma290bGluL0xhenk7TAAKaW5uZXJTY29wZXEAfgAQTAAKc2NvcGVTdGFja3EAfgAFeHBzcgAaa290bGluLkluaXRpYWxpemVkTGF6eUltcGx7x3/xICqBjQIAAUwABXZhbHVldAASTGphdmEvbGFuZy9PYmplY3Q7eHBzcgARamF2YS5sYW5nLkludGVnZXIS4qCk94GHOAIAAUkABXZhbHVleHIAEGphdmEubGFuZy5OdW1iZXKGrJUdC5TgiwIAAHhwzPGofnNxAH4AK3NxAH4ALnNxAH4AMU5njWFzcQB+ACtzcQB+AC5zcQB+ADEAAAAfcHNyABxrb3RsaW4uY29sbGVjdGlvbnMuRW1wdHlMaXN0mW/H0KfgYDICAAB4cHNyACNqYXZhLnV0aWwuQ29sbGVjdGlvbnMkU2luZ2xldG9uTGlzdCrvKRA8p5uXAgABTAAHZWxlbWVudHEAfgAveHBzcgAmc3BlYy5jdmxhc3QuQ1ZMU2NvcGUkSXRlbSRBc3RTY29wZUl0ZW2Hm6f3BtWhkwIAAHhyABlzcGVjLmN2bGFzdC5DVkxTY29wZSRJdGVtLwOv/543VkUCAAB4cHNyABNqYXZhLnV0aWwuQXJyYXlMaXN0eIHSHZnHYZ0DAAFJAARzaXpleHAAAAACdwQAAAACcQB+AEBzcgArc3BlYy5jdmxhc3QuQ1ZMU2NvcGUkSXRlbSRFeHByZXNzaW9uU3VtbWFyeQ8zGp1aX6loAgABSQAHc2NvcGVJZHhyAClzcGVjLmN2bGFzdC5DVkxTY29wZSRJdGVtJEFTVEVsZW1lbnRTY29wZVKrjxFR5CKWAgABTAAHZWxlbWVudHQAGkxzcGVjL2N2bGFzdC9DcmVhdGVzU2NvcGU7eHEAfgA/c3EAfgANc3EAfgAWc3EAfgAacQB+AB5xAH4AHnNxAH4AHwBwcQB+ACZxAH4ALXB+cgAZc3BlYy5jdmxhc3QuVHdvU3RhdGVJbmRleAAAAAAAAAAAEgAAeHIADmphdmEubGFuZy5FbnVtAAAAAAAAAAASAAB4cHQAB05FSVRIRVJzcQB+ABp0AAFkcQB+AFBzcQB+AB8AcHNxAH4AI3NxAH4AJwAAAFgAAAACcQB+AClzcQB+ACcAAABXAAAAAnEAfgAtcHEAfgBNc3EAfgAfAHBzcQB+ACNzcQB+ACcAAABZAAAAAnEAfgApc3EAfgAnAAAASgAAAAJxAH4ALXBwc3EAfgBBAAAAAXcEAAAAAXNyABlzcGVjLmN2bGFzdC5WTVBhcmFtJE5hbWVkAF3s8I660I0CAARMAARuYW1lcQB+ABtMAAxvcmlnaW5hbE5hbWVxAH4AG0wABXJhbmdlcQB+AA9MAAZ2bVR5cGV0AC5Mc3BlYy9jdmxhc3QvdHlwZWRlc2NyaXB0b3JzL1ZNVHlwZURlc2NyaXB0b3I7eHIAE3NwZWMuY3ZsYXN0LlZNUGFyYW2gOaiA+zBevwIAAHhwcQB+AFBxAH4AUHNxAH4AI3NxAH4AJwAAACoAAAACcQB+AClzcQB+ACcAAAAhAAAAAnNyADNzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkVUludEuoeixLMHoOJQIAAUkACGJpdHdpZHRoeHIARHNwZWMuY3ZsYXN0LnR5cGVkZXNjcmlwdG9ycy5FVk1UeXBlRGVzY3JpcHRvciRFVk1Jc29tb3JwaGljVmFsdWVUeXBlluOVd2rd8X8CAAB4cgA6c3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yJEVWTVZhbHVlVHlwZRDk0vWorzfhAgAAeHIALXNwZWMuY3ZsYXN0LnR5cGVkZXNjcmlwdG9ycy5FVk1UeXBlRGVzY3JpcHRvcl5WHdzGjj7oAgAAeHAAAAEAeHNxAH4AI3NxAH4AJwAAAFkAAAACcQB+AClzcQB+ACcAAABKAAAAAnEAfgAtfnIALXNwZWMuY3ZsYXN0LlNwZWNDYWxsU3VtbWFyeSRTdW1tYXJpemF0aW9uTW9kZQAAAAAAAAAAEgAAeHEAfgBMdAADQUxMcAAAAAF4c3IALXNwZWMuY3ZsYXN0LkNWTFR5cGUkUHVyZUNWTFR5cGUkR2hvc3QkTWFwcGluZwvwB+ncfDg9AgACTAADa2V5dAAhTHNwZWMvY3ZsYXN0L0NWTFR5cGUkUHVyZUNWTFR5cGU7TAAFdmFsdWVxAH4AbXhyACVzcGVjLmN2bGFzdC5DVkxUeXBlJFB1cmVDVkxUeXBlJEdob3N0s9fykUcZKbgCAAB4cgAfc3BlYy5jdmxhc3QuQ1ZMVHlwZSRQdXJlQ1ZMVHlwZf0GtBZTtiixAgAAeHIAE3NwZWMuY3ZsYXN0LkNWTFR5cGV0MROVt8FlUAIAAHhwc3IAL3NwZWMuY3ZsYXN0LkNWTFR5cGUkUHVyZUNWTFR5cGUkUHJpbWl0aXZlJFVJbnRLuQuajikSRikCAAJJAAhiaXRXaWR0aEkAAWt4cgApc3BlYy5jdmxhc3QuQ1ZMVHlwZSRQdXJlQ1ZMVHlwZSRQcmltaXRpdmUKm9v/NH7COwIAAHhxAH4AbwAAAQAAAAEAc3EAfgByAAABAAAAAQBxAH4ATXNxAH4AGnEAfgBQcQB+AFBzcQB+AB8AcHEAfgBScQB+AC1zcgAWc3BlYy5jdmxhc3QuQ1ZMVHlwZSRWTaOrOy0dfN99AgACTAAHY29udGV4dHQAK0xzcGVjL2N2bGFzdC90eXBlZGVzY3JpcHRvcnMvRnJvbVZNQ29udGV4dDtMAApkZXNjcmlwdG9ycQB+AFt4cQB+AHBzcgBDc3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkZyb21WTUNvbnRleHQkSW50ZXJuYWxTdW1tYXJ5QXJnQmluZGluZ57F5M8BP4knAgAAeHIAKXNwZWMuY3ZsYXN0LnR5cGVkZXNjcmlwdG9ycy5Gcm9tVk1Db250ZXh0xdrxhvd38GUCAAB4cHEAfgBlcQB+AE1zcQB+AB8AcHEAfgBWcQB+AC1xAH4AdXBzcQB+AEEAAAABdwQAAAABcQB+AF14cQB+AGZxAH4ALXEAfgBqcHNyABZzcGVjLkNWTCRJbnRlcm5hbEV4YWN0hfxIIfCO7GACAAFMAAlzaWduYXR1cmV0AC9Mc3BlYy9jdmxhc3QvUXVhbGlmaWVkTWV0aG9kUGFyYW1ldGVyU2lnbmF0dXJlO3hwc3IAN3NwZWMuY3ZsYXN0LlF1YWxpZmllZE1ldGhvZFNpZ25hdHVyZSRRdWFsaWZpZWRNZXRob2RTaWcYfUy0bR1s9QIAA0wABnBhcmFtc3EAfgAFTAATcXVhbGlmaWVkTWV0aG9kTmFtZXQAKExzcGVjL2N2bGFzdC9Db250cmFjdEZ1bmN0aW9uSWRlbnRpZmllcjtMAANyZXNxAH4ABXhwcQB+AFlzcgAdc3BlYy5jdmxhc3QuUXVhbGlmaWVkRnVuY3Rpb27lKUzy5DlRgwIAAkwABGhvc3R0AB5Mc3BlYy9jdmxhc3QvU29saWRpdHlDb250cmFjdDtMAAhtZXRob2RJZHEAfgAbeHBzcgAcc3BlYy5jdmxhc3QuU29saWRpdHlDb250cmFjdCNpfXcagT2iAgABTAAEbmFtZXEAfgAbeHB0AAxUZXN0Q29udHJhY3R0AAZkb3VibGVzcQB+AEEAAAABdwQAAAABc3IAG3NwZWMuY3ZsYXN0LlZNUGFyYW0kVW5uYW1lZEDN5s++OabjAgACTAAFcmFuZ2VxAH4AD0wABnZtVHlwZXEAfgBbeHEAfgBcc3EAfgAjc3EAfgAnAAAARQAAAAJxAH4AKXNxAH4AJwAAAD4AAAACc3EAfgBhAAABAHhzcgBAcmVwb3J0LmNhbGxyZXNvbHV0aW9uLkNhbGxSZXNvbHV0aW9uVGFibGVTdW1tYXJ5SW5mbyREZWZhdWx0SW5mb91yv/CVyTm1AgABTAARYXBwbGljYXRpb25SZWFzb250AChMYW5hbHlzaXMvaWNmZy9TdW1tYXJ5QXBwbGljYXRpb25SZWFzb247eHIANHJlcG9ydC5jYWxscmVzb2x1dGlvbi5DYWxsUmVzb2x1dGlvblRhYmxlU3VtbWFyeUluZm8attBG2mbMhgIAAUwADWluZm8kZGVsZWdhdGVxAH4ALHhwc3EAfgAuc3IAIWRhdGFzdHJ1Y3R1cmVzLkxpbmtlZEFycmF5SGFzaE1hcAAAAAAAAAABAwACRgAKbG9hZEZhY3RvckwACWhhc2hUYWJsZXQALkxkYXRhc3RydWN0dXJlcy9hcnJheWhhc2h0YWJsZS9BcnJheUhhc2hUYWJsZTt4cHcIAAAAAUAAAAB0ABpzdW1tYXJ5IGFwcGxpY2F0aW9uIHJlYXNvbnQAP2RlY2xhcmVkIGF0IEJhc2ljLnNwZWM6Mzo3NSB0byBhcHBseSB0byBhbGwgY2FsbHMgdG8gdGhlIGNhbGxlZXhzcgAvYW5hbHlzaXMuaWNmZy5TdW1tYXJ5QXBwbGljYXRpb25SZWFzb24kU3BlYyRBbGw1W33ZVBMA7QIAAkwAA2xvY3EAfgAPTAAPbWV0aG9kU2lnbmF0dXJlcQB+ABt4cgArYW5hbHlzaXMuaWNmZy5TdW1tYXJ5QXBwbGljYXRpb25SZWFzb24kU3BlY55PD9KbXiwdAgAAeHIAJmFuYWx5c2lzLmljZmcuU3VtbWFyeUFwcGxpY2F0aW9uUmVhc29uQpw/oqvoOJoCAAB4cHEAfgBmdAAPZG91YmxlKHVpbnQyNTYpc3IAE3ZjLmRhdGEuVEFDTWV0YUluZm9Fu1EirQpV2wIABkkABWJlZ2luSQADbGVuSQAGc291cmNlTAAHYWRkcmVzc3QAFkxqYXZhL21hdGgvQmlnSW50ZWdlcjtMAAhqdW1wVHlwZXQAE0xjb21waWxlci9KdW1wVHlwZTtMAA1zb3VyY2VDb250ZXh0dAAYTGNvbXBpbGVyL1NvdXJjZUNvbnRleHQ7eHAAAAH6AAABoQAAAABzcgAUamF2YS5tYXRoLkJpZ0ludGVnZXKM/J8fqTv7HQMABkkACGJpdENvdW50SQAJYml0TGVuZ3RoSQATZmlyc3ROb256ZXJvQnl0ZU51bUkADGxvd2VzdFNldEJpdEkABnNpZ251bVsACW1hZ25pdHVkZXQAAltCeHEAfgAy///////////////+/////gAAAAF1cgACW0Ks8xf4BghU4AIAAHhwAAAAEM5GBKAAAAAAAAAAAAAAAAF4fnIAEWNvbXBpbGVyLkp1bXBUeXBlAAAAAAAAAAASAAB4cQB+AEx0AAVFTlRFUnNyABZjb21waWxlci5Tb3VyY2VDb250ZXh0g3i13hFi1ssCAAJMAA9pbmRleFRvRmlsZVBhdGh0AA9MamF2YS91dGlsL01hcDtMAAlzb3VyY2VEaXJxAH4AG3hwc3EAfgCZdwgAAAABQAAAAHNxAH4AMQAAAAB0ABBUZXN0Q29udHJhY3Quc29seHQAEy5wb3N0X2F1dG9maW5kZXJzLjBzcQB+AINzcQB+AEEAAAABdwQAAAABc3EAfgBacQB+AFBxAH4AUHNyABF1dGlscy5SYW5nZSRFbXB0ecSDHpJeeJXXAgABTAAHY29tbWVudHEAfgAbeHEAfgAldAAAc3EAfgBhAAABAHhzcQB+AIZzcQB+AIlxAH4Ai3EAfgCMc3EAfgBBAAAAAXcEAAAAAXNxAH4AjnNxAH4AunEAfgC8c3EAfgBhAAABAHhzcQB+AEEAAAABdwQAAAABc3IAG2FuYWx5c2lzLmlwLkludGVybmFsRnVuY1JldOSJxFVq29kmAgADSQAGb2Zmc2V0TAAIbG9jYXRpb250ACdMYW5hbHlzaXMvaXAvSW50ZXJuYWxGdW5jVmFsdWVMb2NhdGlvbjtMAAFzdAAXTHZjL2RhdGEvVEFDU3ltYm9sJFZhcjt4cAAAAABzcgAsYW5hbHlzaXMuaXAuSW50ZXJuYWxGdW5jVmFsdWVMb2NhdGlvbiRTY2FsYXLq0v7eu78o9QIAAHhyACVhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmNWYWx1ZUxvY2F0aW9ubIwKnUjZ7fsCAAB4cHNyABp2Yy5kYXRhLlRBQ1N5bWJvbCRWYXIkRnVsbNPLNEzSY95iAgAESQAJY2FsbEluZGV4TAAEbWV0YXQAHkxjb20vY2VydG9yYS9jb2xsZWN0L1RyZWFwTWFwO0wACm5hbWVQcmVmaXhxAH4AG0wAA3RhZ3QACUx0YWMvVGFnO3hyABV2Yy5kYXRhLlRBQ1N5bWJvbCRWYXL8SGvUvjBGEQIAAHhyABF2Yy5kYXRhLlRBQ1N5bWJvbBKTItjnrHLUAgAAeHAAAAAEc3IAIGNvbS5jZXJ0b3JhLmNvbGxlY3QuSGFzaFRyZWFwTWFwzif7eq6lcpwCAANMAANrZXlxAH4AL0wABG5leHR0ACtMY29tL2NlcnRvcmEvY29sbGVjdC9LZXlWYWx1ZVBhaXJMaXN0JE1vcmU7TAAFdmFsdWVxAH4AL3hyACRjb20uY2VydG9yYS5jb2xsZWN0LkFic3RyYWN0VHJlYXBNYXAtbt1HaE0GGQIAAHhyABljb20uY2VydG9yYS5jb2xsZWN0LlRyZWFw/97D47bcPyMCAAJMAARsZWZ0dAAbTGNvbS9jZXJ0b3JhL2NvbGxlY3QvVHJlYXA7TAAFcmlnaHRxAH4A1nhwc3EAfgDScHBzcgALdGFjLk1ldGFLZXlq9heKQ7Ki3QIAA0wAD2VyYXN1cmVTdHJhdGVneXQAHUx0YWMvTWV0YUtleSRFcmFzdXJlU3RyYXRlZ3k7TAAEbmFtZXEAfgAbTAADdHlwdAARTGphdmEvbGFuZy9DbGFzczt4cH5yABt0YWMuTWV0YUtleSRFcmFzdXJlU3RyYXRlZ3kAAAAAAAAAABIAAHhxAH4ATHQACUNhbm9uaWNhbHQAElRhYy5zeW1ib2wua2V5d29yZHZyACJ2Yy5kYXRhLlRBQ1N5bWJvbCRWYXIkS2V5d29yZEVudHJ5TuPA5DR23HYCAAB4cHBzcgAydmMuZGF0YS5UQUNTeW1ib2wkVmFyJEtleXdvcmRFbnRyeSRUQUNLZXl3b3JkRW50cnm4mRaPLAQsrQIAAkkAFm1heWJlVEFDS2V5d29yZE9yZGluYWxMAARuYW1lcQB+ABt4cQB+AOEAAAAtdAABTHBzcQB+ANlxAH4A3nQAEHRhYy5zdGFjay5oZWlnaHR2cQB+ADFwc3EAfgAxAAAD/3QAA1I1MXNyAA50YWMuVGFnJEJpdDI1Ngwk+60L/KKgAgAAeHIADHRhYy5UYWckQml0c42WGHdpIwuYAgAGSQAIYml0d2lkdGhMAAltYXhTaWduZWRxAH4ApEwAC21heFVuc2lnbmVkcQB+AKRMAAttaW5TaWduZWQyc3EAfgCkTAANbWluU2lnbmVkTWF0aHEAfgCkTAAHbW9kdWx1c3EAfgCkeHIAB3RhYy5UYWd6JeJmnUHF9QIAAHhwAAABAHNxAH4AqP///////////////v////4AAAABdXEAfgCrAAAAIH//////////////////////////////////////////eHNxAH4AqP///////////////v////4AAAABdXEAfgCrAAAAIP//////////////////////////////////////////eHNxAH4AqP///////////////v////4AAAABdXEAfgCrAAAAIIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAeHNxAH4AqP///////////////v////7/////dXEAfgCrAAAAIIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAeHNxAH4AqP///////////////v////4AAAABdXEAfgCrAAAAIQEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHh4c3IAG2tvdGxpbi5jb2xsZWN0aW9ucy5FbXB0eVNldC9GsBV21+L0AgAAeHA="}
		AssignExpCmd calledContract!!69:10 R12:57
		AssignExpCmd executingContract!!70:44 R12:57
		AssignExpCmd CANON!!71:25 R12:57
		LabelCmd "7: Move primitive value for variable tmp490491:int..."
		AssignExpCmd I72 0x7
		LabelCmd "...done 7"
		AssignExpCmd CANON83:40 Select(CANON84:41 0x7(int) )
		AssumeExpCmd LAnd(Ge(CANON83:40 0x0(int) ) Le(CANON83:40 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff(int) ) )
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.CVLSnippetCmd.GhostRead","readValue":{"namePrefix":"CANON83","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.ghost","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Ghost.Mapping","key":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"ghost_double"}]},"indices":[{"namePrefix":"I72","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}}]}],"name":"ghost_double","sort":{"#class":"spec.cvlast.GhostSort.Mapping"},"persistent":false,"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":2,"charByteOffset":74},"end":{"line":2,"charByteOffset":89}},"readExpr":"ghost_double[d]"}}
		LabelCmd "6: Read primitive from tmp488489:int..."
		AssertCmd:145 true "sanity bounds check on cvl to vm encoding (unsigned int elements of a user array) of %1$s failed"
		AssignExpCmd R73:24 Apply(safe_math_narrow_bv256:bif CANON83)
		LabelCmd "...done 6"
		AnnotationCmd JSON{"key":{"name":"call.trace.internal.summary.end","type":"analysis.icfg.SummaryStack$SummaryEnd$Internal","erasureStrategy":"Canonical"},"value":"rO0ABXNyAC5hbmFseXNpcy5pY2ZnLlN1bW1hcnlTdGFjayRTdW1tYXJ5RW5kJEludGVybmFs/bQ7d/THvhkCAANMAA9tZXRob2RTaWduYXR1cmV0ACZMc3BlYy9jdmxhc3QvUXVhbGlmaWVkTWV0aG9kU2lnbmF0dXJlO0wABHJldHN0ABBMamF2YS91dGlsL0xpc3Q7TAAHc3VwcG9ydHQAD0xqYXZhL3V0aWwvU2V0O3hyACVhbmFseXNpcy5pY2ZnLlN1bW1hcnlTdGFjayRTdW1tYXJ5RW5kFZQmA8fWa+kCAAB4cHNyADdzcGVjLmN2bGFzdC5RdWFsaWZpZWRNZXRob2RTaWduYXR1cmUkUXVhbGlmaWVkTWV0aG9kU2lnGH1MtG0dbPUCAANMAAZwYXJhbXNxAH4AAkwAE3F1YWxpZmllZE1ldGhvZE5hbWV0AChMc3BlYy9jdmxhc3QvQ29udHJhY3RGdW5jdGlvbklkZW50aWZpZXI7TAADcmVzcQB+AAJ4cHNyABNqYXZhLnV0aWwuQXJyYXlMaXN0eIHSHZnHYZ0DAAFJAARzaXpleHAAAAABdwQAAAABc3IAGXNwZWMuY3ZsYXN0LlZNUGFyYW0kTmFtZWQAXezwjrrQjQIABEwABG5hbWV0ABJMamF2YS9sYW5nL1N0cmluZztMAAxvcmlnaW5hbE5hbWVxAH4ADEwABXJhbmdldAANTHV0aWxzL1JhbmdlO0wABnZtVHlwZXQALkxzcGVjL2N2bGFzdC90eXBlZGVzY3JpcHRvcnMvVk1UeXBlRGVzY3JpcHRvcjt4cgATc3BlYy5jdmxhc3QuVk1QYXJhbaA5qID7MF6/AgAAeHB0AAFkcQB+ABFzcgARdXRpbHMuUmFuZ2UkRW1wdHnEgx6SXniV1wIAAUwAB2NvbW1lbnRxAH4ADHhyAAt1dGlscy5SYW5nZegD9PKVZX9XAgAAeHB0AABzcgAzc3BlYy5jdmxhc3QudHlwZWRlc2NyaXB0b3JzLkVWTVR5cGVEZXNjcmlwdG9yJFVJbnRLqHosSzB6DiUCAAFJAAhiaXR3aWR0aHhyAERzcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3IkRVZNSXNvbW9ycGhpY1ZhbHVlVHlwZZbjlXdq3fF/AgAAeHIAOnNwZWMuY3ZsYXN0LnR5cGVkZXNjcmlwdG9ycy5FVk1UeXBlRGVzY3JpcHRvciRFVk1WYWx1ZVR5cGUQ5NL1qK834QIAAHhyAC1zcGVjLmN2bGFzdC50eXBlZGVzY3JpcHRvcnMuRVZNVHlwZURlc2NyaXB0b3JeVh3cxo4+6AIAAHhwAAABAHhzcgAdc3BlYy5jdmxhc3QuUXVhbGlmaWVkRnVuY3Rpb27lKUzy5DlRgwIAAkwABGhvc3R0AB5Mc3BlYy9jdmxhc3QvU29saWRpdHlDb250cmFjdDtMAAhtZXRob2RJZHEAfgAMeHBzcgAcc3BlYy5jdmxhc3QuU29saWRpdHlDb250cmFjdCNpfXcagT2iAgABTAAEbmFtZXEAfgAMeHB0AAxUZXN0Q29udHJhY3R0AAZkb3VibGVzcQB+AAkAAAABdwQAAAABc3IAG3NwZWMuY3ZsYXN0LlZNUGFyYW0kVW5uYW1lZEDN5s++OabjAgACTAAFcmFuZ2VxAH4ADUwABnZtVHlwZXEAfgAOeHEAfgAPc3EAfgAScQB+ABVzcQB+ABYAAAEAeHNxAH4ACQAAAAF3BAAAAAFzcgAbYW5hbHlzaXMuaXAuSW50ZXJuYWxGdW5jUmV05InEVWrb2SYCAANJAAZvZmZzZXRMAAhsb2NhdGlvbnQAJ0xhbmFseXNpcy9pcC9JbnRlcm5hbEZ1bmNWYWx1ZUxvY2F0aW9uO0wAAXN0ABdMdmMvZGF0YS9UQUNTeW1ib2wkVmFyO3hwAAAAAHNyACxhbmFseXNpcy5pcC5JbnRlcm5hbEZ1bmNWYWx1ZUxvY2F0aW9uJFNjYWxhcurS/t67vyj1AgAAeHIAJWFuYWx5c2lzLmlwLkludGVybmFsRnVuY1ZhbHVlTG9jYXRpb25sjAqdSNnt+wIAAHhwc3IANXZjLmRhdGEuVEFDU3ltYm9sJFZhciRXaXRoRGVmYXVsdENhbGxJbmRleCRXaXRoQml0MjU2nq3gkxche2QCAAJMAARtZXRhdAAeTGNvbS9jZXJ0b3JhL2NvbGxlY3QvVHJlYXBNYXA7TAAKbmFtZVByZWZpeHEAfgAMeHIAFXZjLmRhdGEuVEFDU3ltYm9sJFZhcvxIa9S+MEYRAgAAeHIAEXZjLmRhdGEuVEFDU3ltYm9sEpMi2OesctQCAAB4cHNyACBjb20uY2VydG9yYS5jb2xsZWN0Lkhhc2hUcmVhcE1hcM4n+3qupXKcAgADTAADa2V5dAASTGphdmEvbGFuZy9PYmplY3Q7TAAEbmV4dHQAK0xjb20vY2VydG9yYS9jb2xsZWN0L0tleVZhbHVlUGFpckxpc3QkTW9yZTtMAAV2YWx1ZXEAfgA1eHIAJGNvbS5jZXJ0b3JhLmNvbGxlY3QuQWJzdHJhY3RUcmVhcE1hcC1u3UdoTQYZAgAAeHIAGWNvbS5jZXJ0b3JhLmNvbGxlY3QuVHJlYXD/3sPjttw/IwIAAkwABGxlZnR0ABtMY29tL2NlcnRvcmEvY29sbGVjdC9UcmVhcDtMAAVyaWdodHEAfgA5eHBzcQB+ADRwcHNyAAt0YWMuTWV0YUtleWr2F4pDsqLdAgADTAAPZXJhc3VyZVN0cmF0ZWd5dAAdTHRhYy9NZXRhS2V5JEVyYXN1cmVTdHJhdGVneTtMAARuYW1lcQB+AAxMAAN0eXB0ABFMamF2YS9sYW5nL0NsYXNzO3hwfnIAG3RhYy5NZXRhS2V5JEVyYXN1cmVTdHJhdGVneQAAAAAAAAAAEgAAeHIADmphdmEubGFuZy5FbnVtAAAAAAAAAAASAAB4cHQACUNhbm9uaWNhbHQAElRhYy5zeW1ib2wua2V5d29yZHZyACJ2Yy5kYXRhLlRBQ1N5bWJvbCRWYXIkS2V5d29yZEVudHJ5TuPA5DR23HYCAAB4cHBzcgAydmMuZGF0YS5UQUNTeW1ib2wkVmFyJEtleXdvcmRFbnRyeSRUQUNLZXl3b3JkRW50cnm4mRaPLAQsrQIAAkkAFm1heWJlVEFDS2V5d29yZE9yZGluYWxMAARuYW1lcQB+AAx4cQB+AEUAAAAtdAABTHBzcQB+ADxxAH4AQnQAEHRhYy5zdGFjay5oZWlnaHR2cgARamF2YS5sYW5nLkludGVnZXIS4qCk94GHOAIAAUkABXZhbHVleHIAEGphdmEubGFuZy5OdW1iZXKGrJUdC5TgiwIAAHhwcHNxAH4ATAAAA/90AANSNzN4c3IAImphdmEudXRpbC5Db2xsZWN0aW9ucyRTaW5nbGV0b25TZXQsUkGYKcCxvwIAAUwAB2VsZW1lbnRxAH4ANXhwcQB+ADM="}
		JumpCmd 9_0_0_5_0_0
	}
	Block 9_0_0_5_0_0 Succ [10_0_0_0_0_0] {
		AnnotationCmd:146 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":234,"bytecodeCount":8,"sources":[{"source":0,"begin":506,"end":923}]}}
		AnnotationCmd:144 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":1180,"bytecodeCount":14,"sources":[{"source":1,"begin":957,"end":1179},{"source":1,"begin":1050,"end":1054},{"source":1,"begin":1088,"end":1090},{"source":1,"begin":1077,"end":1086},{"source":1,"begin":1073,"end":1091},{"source":1,"begin":1065,"end":1091},{"source":1,"begin":1101,"end":1172},{"source":1,"begin":1169,"end":1170},{"source":1,"begin":1158,"end":1167},{"source":1,"begin":1154,"end":1171},{"source":1,"begin":1145,"end":1151}]}}
		AnnotationCmd:144 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":1165,"bytecodeCount":5,"sources":[{"source":1,"begin":833,"end":951},{"source":1,"begin":920,"end":944},{"source":1,"begin":938,"end":943}]}}
		AnnotationCmd:144 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":1383,"bytecodeCount":9,"sources":[{"source":1,"begin":1850,"end":1927},{"source":1,"begin":1887,"end":1894},{"source":1,"begin":1916,"end":1921},{"source":1,"begin":1905,"end":1921},{"source":1,"begin":1895,"end":1927}]}}
		AnnotationCmd:144 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":1174,"bytecodeCount":6,"sources":[{"source":1,"begin":920,"end":944},{"source":1,"begin":915,"end":918},{"source":1,"begin":908,"end":945},{"source":1,"begin":898,"end":951}]}}
		AnnotationCmd:128 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R73","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":5}}
		AnnotationCmd:144 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":1201,"bytecodeCount":6,"sources":[{"source":1,"begin":1101,"end":1172},{"source":1,"begin":1055,"end":1179}]}}
		AnnotationCmd:144 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":247,"bytecodeCount":8,"sources":[{"source":0,"begin":506,"end":923}]}}
		AssignExpCmd:147 lastHasThrown!!74:45 false
		AssignExpCmd:147 lastReverted!!75:6 false
		AnnotationCmd:147 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:128 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.HaltSnippet.Return","range":{"specFile":"TestContract.sol","start":{"line":9,"charByteOffset":4},"end":{"line":11,"charByteOffset":5}}}}
		LabelCmd:128 "End procedure TestContract-double(uint256)"
		LabelCmd:128 "3: Move primitive value for variable r3317:int..."
		AssignExpCmd:128 CANON59!!76:17 R73:24
		LabelCmd:128 "...done 3"
		AnnotationCmd:128 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":{"callee":{"contractId":"ce4604a0000000000000000000000001","sigHash":{"n":"eee97206"},"attr":{"#class":"scene.MethodAttribute.Common"}},"calleeId":5}}
	}
	Block 10_0_0_0_0_0 Succ [11_0_0_7_0_0] {
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule"}},{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.NonTACKeywordEntry","name":"lastStorage"}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AnnotationCmd:128 JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":28}
		AnnotationCmd:148 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Definition","range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":38,"charByteOffset":4},"end":{"line":38,"charByteOffset":26}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"idL":[{"#class":"spec.cvlast.CVLLhs.Id","range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":38,"charByteOffset":4},"end":{"line":38,"charByteOffset":14}},"id":"r4","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":38,"charByteOffset":4},"end":{"line":38,"charByteOffset":14}}}}],"exp":{"#class":"spec.cvlast.CVLExp.ApplyExp.ContractFunction.Concrete","methodIdWithCallContext":{"#class":"spec.cvlast.ConcreteMethod","signature":{"#class":"spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig","wrapped":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"TestContract"},"methodId":"getval"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}]},"sighashInt":{"n":"31b6bd06"}}},"args":[],"noRevert":true,"storage":{"id":"lastStorage","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"},"range":{"#class":"utils.Range.Empty","comment":"empty storage type"}},"twoStateIndex":"NEITHER"},"isWhole":false,"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.VM","descriptor":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"context":{"#class":"spec.cvlast.typedescriptors.FromVMContext.ReturnValue"}},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":38,"charByteOffset":17},"end":{"line":38,"charByteOffset":25}},"annotation":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.CallResolution$DirectPassing","target":{"methodSignature":{"#class":"spec.cvlast.ExternalQualifiedMethodSignature.ExternalQualifiedMethodSig","wrapped":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"TestContract"},"methodId":"getval"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}]},"sighashInt":{"n":"31b6bd06"}},"definitelyNonPayable":true,"annotation":{"visibility":"EXTERNAL","envFree":true,"library":false,"virtual":false},"stateMutability":"nonpayable","evmExternalMethodInfo":{"sigHash":"31b6bd06","name":"getval","argTypes":[],"resultTypes":[{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}],"stateMutability":"nonpayable","isConstant":false,"isLibrary":false,"contractName":"TestContract","contractInstanceId":"ce4604a0000000000000000000000001","sourceSegment":{"range":{"specFile":"TestContract.sol","start":{"line":13,"charByteOffset":4},"end":{"line":15,"charByteOffset":5}},"content":"function getval() public returns (uint256) {\n        return val;\n    }"}}},"hasEnv":false}}},"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
	}
	Block 11_0_0_7_0_0 Succ [12_0_0_0_0_0] {
		AssignHavocCmd:149 CANON85!!77:4
		AnnotationCmd:149 JSON{"key":{"name":"call.trace.push","type":"analysis.icfg.Inliner$CallStack$PushRecord","erasureStrategy":"Canonical"},"value":{"callee":{"contractId":"ce4604a0000000000000000000000001","sigHash":{"n":"31b6bd06"},"attr":{"#class":"scene.MethodAttribute.Common"}},"summary":null,"convention":{"#class":"analysis.icfg.Inliner.CallConventionType.FromCVL"},"calleeId":7}}
		AssignHavocCmd:149 tacCalldatasize!!78:9
		AssumeExpCmd Eq(tacCalldatasize!!78:9 0x4 )
		AssignExpCmd:149 tacCalldatabuf@7:16 MapDefinition(CANON86.600:bv256 -> Ite(Lt(CANON86.600 tacCalldatasize!!78:9 ) Select(Select(Select(CANON28!7:26 CANON86.600 ) tacCalldatasize!!78:9 ) 0x31b6bd06 ) 0x0 ) bytemap)
		AssignExpCmd:149 R79:20 Select(Select(Select(CANON28!7:26 0x0 ) 0x4 ) 0x31b6bd06 )
		AssumeExpCmd LAnd(Ge(R79:20 0x31b6bd0600000000000000000000000000000000000000000000000000000000 ) Le(R79:20 0x31b6bd06ffffffffffffffffffffffffffffffffffffffffffffffffffffffff ) )
		AnnotationCmd:149 JSON{"key":{"name":"cvl.arg-serialization.start","type":"spec.CVLInvocationCompiler$StartSerializationMarker","erasureStrategy":"Canonical"},"value":{"id":2,"callId":7}}
		AnnotationCmd:149 JSON{"key":{"name":"cvl.arg-serialization.end","type":"spec.CVLInvocationCompiler$EndSerializationMarker","erasureStrategy":"Canonical"},"value":{"id":2,"callId":7}}
		LabelCmd:149 "Start procedure TestContract-getval()"
		AnnotationCmd:149 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AssignExpCmd:149 R81:20 Select(tacExtcodesize!!4:7 Apply(to_skey:bif R12:115) )
		AssumeExpCmd Ge(R81:20 0x1 )
		AnnotationCmd:149 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.RawStorageAccess.WithLocSym","isLoad":true,"loc":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R12","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"tacAddress","maybeTACKeywordOrdinal":22}},{"key":{"name":"tac.env.known-bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":160},{"key":{"name":"tac.contract.sym.addr.name","type":"java.lang.String","erasureStrategy":"Erased"},"value":"TestContract"},{"key":{"name":"tac.contract.sym.addr","type":"java.math.BigInteger","erasureStrategy":"Erased"},"value":"ce4604a0000000000000000000000001"}]},"contractInstance":"ce4604a0000000000000000000000001","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"R81","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.is-temp-var","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}]},"storageType":null,"range":null}}
		AnnotationCmd:149 JSON{"key":{"name":"internal.func.finder.info","type":"analysis.ip.InternalFunctionFinderReport","erasureStrategy":"Erased"},"value":{"unresolvedFunctions":[]}}
		AnnotationCmd:149 JSON{"key":{"name":"fps.free-pointer-is-scalarized","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true}
		AnnotationCmd:149 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":0,"bytecodeCount":8,"sources":[{"source":0,"begin":25,"end":2021}]}}
		LabelCmd "→ Assuming FP is strictly monotonic increasing"
		LabelCmd "←"
		AnnotationCmd:149 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.StartBranchSnippet","branchIndex":4,"branchSource":{"range":{"specFile":"TestContract.sol","start":{"line":2,"charByteOffset":0},"end":{"line":24,"charByteOffset":1}},"content":"contract TestContract {...}"}}}
		AnnotationCmd:149 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.BranchSnippet.EndBranchSnippet","branchIndex":4}}
		AnnotationCmd:150 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":16,"bytecodeCount":7,"sources":[{"source":0,"begin":25,"end":2021}]}}
		AnnotationCmd:150 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":26,"bytecodeCount":9,"sources":[{"source":0,"begin":25,"end":2021}]}}
		AnnotationCmd:150 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":92,"bytecodeCount":4,"sources":[{"source":0,"begin":929,"end":1257}]}}
		AnnotationCmd:149 JSON{"key":{"name":"internal.func.start","type":"analysis.ip.InternalFuncStartAnnotation","erasureStrategy":"CallTrace"},"value":{"id":0,"startPc":256,"args":[],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"TestContract"},"methodId":"getval"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}]},"stackOffsetToArgPos":{},"callSiteSrc":{"source":0,"begin":929,"len":328,"jumpType":"ENTER","address":"ce4604a0000000000000000000000001","sourceContext":{"indexToFilePath":{"0":"TestContract.sol"},"sourceDir":".post_autofinders.0"}}}}
		AnnotationCmd:151 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":256,"bytecodeCount":17,"sources":[{"source":0,"begin":929,"end":1257},{"source":0,"begin":963,"end":970},{"source":0,"begin":1059,"end":1072},{"source":0,"begin":991,"end":1057},{"source":0,"begin":984,"end":1073},{"source":0,"begin":1149,"end":1150},{"source":0,"begin":1081,"end":1147},{"source":0,"begin":1074,"end":1151},{"source":0,"begin":1227,"end":1228},{"source":0,"begin":1159,"end":1225},{"source":0,"begin":1152,"end":1229},{"source":0,"begin":1247,"end":1250},{"source":0,"begin":1240,"end":1250}]}}
		AnnotationCmd:152 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.ApplyHook","hookPatternString":"Hook Sload uint256 contractVal 0x0.0x0 tacS","range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":15,"charByteOffset":0},"end":{"line":18,"charByteOffset":1}}}}
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.CVLSnippetCmd.InlinedHook","cvlPattern":{"#class":"spec.cvlast.CVLHookPattern.StoragePattern.Load","value":{"name":"contractVal","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":15,"charByteOffset":11},"end":{"line":15,"charByteOffset":30}}},"slot":{"#class":"spec.cvlast.CVLSlotPattern.Static.Named","solidityContract":{"name":"TestContract"},"name":"val"},"base":"STORAGE"},"substitutions":[{"name":"contractVal","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":15,"charByteOffset":11},"end":{"line":15,"charByteOffset":30}}},{"#class":"vc.data.HookValue.Direct","expr":{"#class":"vc.data.TACExpr.Sym.Var","s":{"namePrefix":"R6","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1021}]},"tag":{"#class":"tac.Tag.Bit256"}}}],"displayPath":null}}
		AssignExpCmd:153 B83:12 true
		AssignExpCmd:154 B84 true
		AssignExpCmd:155 I85 CANON92:156
		AnnotationCmd:157 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.CVLSnippetCmd.GhostRead","readValue":{"namePrefix":"CANON92","tag":{"#class":"tac.Tag.Int"},"callIndex":0,"meta":[{"key":{"name":"cvl.ghost","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"tac.no.callindex","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"innerVal"}]},"indices":[],"name":"innerVal","sort":{"#class":"spec.cvlast.GhostSort.Variable"},"persistent":false,"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":17,"charByteOffset":12},"end":{"line":17,"charByteOffset":20}},"readExpr":"innerVal"}}
		AssignExpCmd:158 CANON94:11 Eq(I85:43 CANON88!!8:159 )
		AssumeCmd CANON94:11 "expToAssumeCmd"
		AnnotationCmd JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":30}
		AnnotationCmd:149 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet","value":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON88!!8","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.storage.non-indexed-path.family","type":"analysis.storage.StorageAnalysisResult$StoragePaths","erasureStrategy":"Canonical"},"value":{"storagePaths":[{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"0"}]}},{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"0"}},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"val"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"0"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000001"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1021}]},"displayPath":{"#class":"analysis.storage.DisplayPath.Root","name":"val"},"storageType":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256},"contractInstance":"ce4604a0000000000000000000000001","range":{"specFile":"TestContract.sol","start":{"line":14,"charByteOffset":15},"end":{"line":14,"charByteOffset":18}},"linkableStorageReadId":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageSnippet.LoadSnippet.Id","id":0}}}
		AnnotationCmd:149 JSON{"key":{"name":"internal.func.end","type":"analysis.ip.InternalFuncExitAnnotation","erasureStrategy":"Canonical"},"value":{"id":0,"rets":[{"s":{"namePrefix":"CANON88!!8","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.storage.non-indexed-path.family","type":"analysis.storage.StorageAnalysisResult$StoragePaths","erasureStrategy":"Canonical"},"value":{"storagePaths":[{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"0"}]}},{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"0"}},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"val"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"0"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000001"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"offset":0,"location":{"#class":"analysis.ip.InternalFuncValueLocation.Scalar"}}],"methodSignature":{"#class":"spec.cvlast.QualifiedMethodSignature.QualifiedMethodSig","qualifiedMethodName":{"#class":"spec.cvlast.QualifiedFunction","host":{"name":"TestContract"},"methodId":"getval"},"params":[],"res":[{"#class":"spec.cvlast.VMParam.Unnamed","vmType":{"#class":"ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK","bitwidth":256},"range":{"#class":"utils.Range.Empty"}}]}}}
		AnnotationCmd:160 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":100,"bytecodeCount":8,"sources":[{"source":0,"begin":929,"end":1257}]}}
		AnnotationCmd:151 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":1180,"bytecodeCount":14,"sources":[{"source":1,"begin":957,"end":1179},{"source":1,"begin":1050,"end":1054},{"source":1,"begin":1088,"end":1090},{"source":1,"begin":1077,"end":1086},{"source":1,"begin":1073,"end":1091},{"source":1,"begin":1065,"end":1091},{"source":1,"begin":1101,"end":1172},{"source":1,"begin":1169,"end":1170},{"source":1,"begin":1158,"end":1167},{"source":1,"begin":1154,"end":1171},{"source":1,"begin":1145,"end":1151}]}}
		AnnotationCmd:151 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":1165,"bytecodeCount":5,"sources":[{"source":1,"begin":833,"end":951},{"source":1,"begin":920,"end":944},{"source":1,"begin":938,"end":943}]}}
		AnnotationCmd:151 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":1383,"bytecodeCount":9,"sources":[{"source":1,"begin":1850,"end":1927},{"source":1,"begin":1887,"end":1894},{"source":1,"begin":1916,"end":1921},{"source":1,"begin":1905,"end":1921},{"source":1,"begin":1895,"end":1927}]}}
		AnnotationCmd:151 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":1174,"bytecodeCount":6,"sources":[{"source":1,"begin":920,"end":944},{"source":1,"begin":915,"end":918},{"source":1,"begin":908,"end":945},{"source":1,"begin":898,"end":951}]}}
		AnnotationCmd:149 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.EVMFunctionReturnWrite","returnbufOffset":"0","returnValueSym":{"#class":"vc.data.TACSymbol.Var.Full","namePrefix":"CANON88!!8","tag":{"#class":"tac.Tag.Bit256"},"callIndex":0,"meta":[{"key":{"name":"tac.storage.non-indexed-path.family","type":"analysis.storage.StorageAnalysisResult$StoragePaths","erasureStrategy":"Canonical"},"value":{"storagePaths":[{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"0"}]}},{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.TACKeywordEntry","name":"L","maybeTACKeywordOrdinal":45}},{"key":{"name":"tac.scalarization.sort","type":"vc.data.ScalarizationSort","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.ScalarizationSort.Split","idx":"0"}},{"key":{"name":"tac.storage.bit-width","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":256},{"key":{"name":"tac.storage.pretty.paths","type":"analysis.storage.DisplayPaths","erasureStrategy":"Erased"},"value":{"paths":[{"#class":"analysis.storage.DisplayPath.Root","name":"val"}]}},{"key":{"name":"tac.slot.type","type":"spec.cvlast.typedescriptors.EVMTypeDescriptor$EVMValueType","erasureStrategy":"Canonical"},"value":{"#class":"spec.cvlast.typedescriptors.EVMTypeDescriptor.UIntK","bitwidth":256}},{"key":{"name":"tac.storage.non-indexed-path","type":"analysis.storage.StorageAnalysisResult$NonIndexedPath","erasureStrategy":"Canonical"},"value":{"#class":"analysis.storage.StorageAnalysisResult.NonIndexedPath.Root","slot":"0"}},{"key":{"name":"tac.storage","type":"java.math.BigInteger","erasureStrategy":"Canonical"},"value":"ce4604a0000000000000000000000001"},{"key":{"name":"tac.stack.height","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":1023}]},"callIndex":7}}
		AnnotationCmd:151 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":1201,"bytecodeCount":6,"sources":[{"source":1,"begin":1101,"end":1172},{"source":1,"begin":1055,"end":1179}]}}
		AnnotationCmd:151 JSON{"key":{"name":"block.source","type":"decompiler.Decompiler$BlockSourceInfo","erasureStrategy":"Canonical"},"value":{"contractName":"TestContract","contractAddress":"ce4604a0000000000000000000000001","contractBytecodeHash":"da560ac15b509fa81ecdbfe8703fc549973862a6c99487cf19bea297e2ef30da","pc":113,"bytecodeCount":8,"sources":[{"source":0,"begin":929,"end":1257}]}}
		AssignExpCmd:161 lastHasThrown!!87:45 false
		AssignExpCmd:161 lastReverted!!88:6 false
		AnnotationCmd:161 JSON{"key":{"name":"tac.return.path","type":"tac.MetaMap$Companion$NothingValue","erasureStrategy":"Canonical"},"value":{}}
		AnnotationCmd:149 JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.HaltSnippet.Return","range":{"specFile":"TestContract.sol","start":{"line":13,"charByteOffset":4},"end":{"line":15,"charByteOffset":5}}}}
		LabelCmd:149 "End procedure TestContract-getval()"
		LabelCmd:149 "5: Move primitive value for variable r4423:int..."
		AssignExpCmd:149 CANON85!!89:4 CANON88!!8:159
		LabelCmd:149 "...done 5"
		AnnotationCmd:149 JSON{"key":{"name":"call.trace.pop","type":"analysis.icfg.Inliner$CallStack$PopRecord","erasureStrategy":"Canonical"},"value":{"callee":{"contractId":"ce4604a0000000000000000000000001","sigHash":{"n":"31b6bd06"},"attr":{"#class":"scene.MethodAttribute.Common"}},"calleeId":7}}
	}
	Block 12_0_0_0_0_0 Succ [] {
		AnnotationCmd JSON{"key":{"name":"snippet.cmd","type":"vc.data.SnippetCmd","erasureStrategy":"CallTrace"},"value":{"#class":"vc.data.SnippetCmd.EVMSnippetCmd.StorageGlobalChangeSnippet.StorageTakeSnapshot","lhs":{"namePrefix":"lastStorage","tag":{"#class":"tac.Tag.BlockchainState"},"callIndex":0,"meta":[{"key":{"name":"cvl.def.site","type":"spec.CVLDefinitionSite","erasureStrategy":"Canonical"},"value":{"#class":"spec.CVLDefinitionSite.Rule"}},{"key":{"name":"Tac.symbol.keyword","type":"vc.data.TACSymbol$Var$KeywordEntry","erasureStrategy":"Canonical"},"value":{"#class":"vc.data.TACSymbol.Var.KeywordEntry.NonTACKeywordEntry","name":"lastStorage"}},{"key":{"name":"cvl.type","type":"spec.cvlast.CVLType$PureCVLType","erasureStrategy":"CallTrace"},"value":{"#class":"spec.cvlast.CVLType.PureCVLType.VMInternal.BlockchainState"}},{"key":{"name":"cvl","type":"java.lang.Boolean","erasureStrategy":"Canonical"},"value":true},{"key":{"name":"cvl.display","type":"java.lang.String","erasureStrategy":"CallTrace"},"value":"lastStorage"}]}}}
		AnnotationCmd:149 JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":29}
		AnnotationCmd:162 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.AssumeCmd.Assume","range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":39,"charByteOffset":4},"end":{"line":39,"charByteOffset":20}},"exp":{"#class":"spec.cvlast.CVLExp.RelopExp.ArithRelopExp.GtExp","l":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"t","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":39,"charByteOffset":12},"end":{"line":39,"charByteOffset":13}}},"twoStateIndex":"NEITHER"},"r":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"num","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":39,"charByteOffset":16},"end":{"line":39,"charByteOffset":19}}},"twoStateIndex":"NEITHER"},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":39,"charByteOffset":12},"end":{"line":39,"charByteOffset":19}}}},"description":null,"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssignExpCmd:163 I90 0x14(int)
		AssignExpCmd:164 I91 0x5(int)
		AssignExpCmd:165 B92 true
		AnnotationCmd:166 JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":31}
		AnnotationCmd:167 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.AssumeCmd.Assume","range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":40,"charByteOffset":4},"end":{"line":40,"charByteOffset":20}},"exp":{"#class":"spec.cvlast.CVLExp.RelopExp.EqExp","l":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"t","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":40,"charByteOffset":12},"end":{"line":40,"charByteOffset":13}}},"twoStateIndex":"NEITHER"},"r":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"r1","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":40,"charByteOffset":17},"end":{"line":40,"charByteOffset":19}}},"twoStateIndex":"NEITHER"},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":40,"charByteOffset":12},"end":{"line":40,"charByteOffset":19}}}},"description":null,"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssignExpCmd:168 I93 0x14(int)
		AssignExpCmd:169 I94 0x14(int)
		AssignExpCmd:170 CANON100:11 true
		AnnotationCmd:171 JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":32}
		AnnotationCmd:172 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Assert","range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":41,"charByteOffset":4},"end":{"line":41,"charByteOffset":19}},"exp":{"#class":"spec.cvlast.CVLExp.RelopExp.EqExp","l":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"r2","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":41,"charByteOffset":11},"end":{"line":41,"charByteOffset":13}}},"twoStateIndex":"NEITHER"},"r":{"#class":"spec.cvlast.CVLExp.Constant.NumberLit","n":"9","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral","n":"9"},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":41,"charByteOffset":17},"end":{"line":41,"charByteOffset":18}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":41,"charByteOffset":11},"end":{"line":41,"charByteOffset":18}}}},"description":null,"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssignExpCmd:173 I95 0x9
		AssignExpCmd:174 I96 0x9
		AssignExpCmd:175 CANON103:11 true
		AssertCmd:176 true "r2 == 9"
		AnnotationCmd:177 JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":33}
		AnnotationCmd:178 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Assert","range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":42,"charByteOffset":4},"end":{"line":42,"charByteOffset":20}},"exp":{"#class":"spec.cvlast.CVLExp.RelopExp.EqExp","l":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"r3","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":42,"charByteOffset":11},"end":{"line":42,"charByteOffset":13}}},"twoStateIndex":"NEITHER"},"r":{"#class":"spec.cvlast.CVLExp.Constant.NumberLit","n":"e","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral","n":"e"},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":42,"charByteOffset":17},"end":{"line":42,"charByteOffset":19}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":42,"charByteOffset":11},"end":{"line":42,"charByteOffset":19}}}},"description":null,"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssignExpCmd:179 I97 CANON59!!76:17
		AssignExpCmd:180 I98 0xe
		AssignExpCmd:181 CANON106!!99:11 Eq(I97 0xe(int) )
		AssertCmd:182 CANON106!!99:11 "r3 == 14"
		AnnotationCmd:183 JSON{"key":{"name":"cvl.label.end","type":"java.lang.Integer","erasureStrategy":"Canonical"},"value":34}
		AnnotationCmd:184 JSON{"key":{"name":"cvl.label.start","type":"report.calltrace.CVLReportLabel","erasureStrategy":"CallTrace"},"value":{"#class":"report.calltrace.CVLReportLabel.Cmd","cmd":{"cmd_type":"spec.cvlast.CVLCmd.Simple.Assert","range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":43,"charByteOffset":4},"end":{"line":43,"charByteOffset":19}},"exp":{"#class":"spec.cvlast.CVLExp.RelopExp.EqExp","l":{"#class":"spec.cvlast.CVLExp.VariableExp","id":"r4","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.UIntK","k":256},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":43,"charByteOffset":11},"end":{"line":43,"charByteOffset":13}}},"twoStateIndex":"NEITHER"},"r":{"#class":"spec.cvlast.CVLExp.Constant.NumberLit","n":"1","tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.NumberLiteral","n":"1"},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":43,"charByteOffset":17},"end":{"line":43,"charByteOffset":18}}}},"tag":{"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}},"type":{"#class":"spec.cvlast.CVLType.PureCVLType.Primitive.Bool"},"range":{"#class":"utils.Range.Range","specFile":"Basic.spec","start":{"line":43,"charByteOffset":11},"end":{"line":43,"charByteOffset":18}}}},"description":null,"scope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"},{"#class":"spec.cvlast.CVLScope.Item.RuleScopeItem","scopeId":2}],"innerScope":{"scopeStack":[{"#class":"spec.cvlast.CVLScope.Item.AstScopeItem"}],"innerScope":{"scopeStack":[],"innerScope":null}}}}}}
		AssignExpCmd:185 I100 CANON85!!89:186
		AssignExpCmd:187 B101:12 true
		AssignExpCmd:188 CANON109:11 false
		AssertCmd:189 false "r4 == 1"
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
  "1": [
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
  "2": [
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
  "3": [
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
      "value": "24"
    },
    {
      "key": {
        "name": "tac.scalarization.sort",
        "type": "vc.data.ScalarizationSort",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.ScalarizationSort.Split",
        "idx": "24"
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
      "value": "24"
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
  "4": [
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
          "specFile": "Basic.spec",
          "start": {
            "line": 38,
            "charByteOffset": 4
          },
          "end": {
            "line": 38,
            "charByteOffset": 14
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
      "value": "r4"
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
  "6": [
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
  "7": [
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
  "8": [
    {
      "key": {
        "name": "tac.storage.non-indexed-path.family",
        "type": "analysis.storage.StorageAnalysisResult$StoragePaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "storagePaths": [
          {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
            "slot": "0"
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
        "#class": "vc.data.ScalarizationSort.Split",
        "idx": "0"
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
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.Root",
            "name": "val"
          }
        ]
      }
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
        "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
        "slot": "0"
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
  "9": [
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
  "10": [
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
  "11": [
    {
      "key": {
        "name": "cvl",
        "type": "java.lang.Boolean",
        "erasureStrategy": "Canonical"
      },
      "value": true
    }
  ],
  "12": [
    {
      "key": {
        "name": "tac.was.replaced.with.bool",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "13": [
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
  "14": [
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
          "callIndex": 2,
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
  "15": [
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
          "callIndex": 5,
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
  "16": [
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
          "callIndex": 7,
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
  "17": [
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
          "specFile": "Basic.spec",
          "start": {
            "line": 37,
            "charByteOffset": 4
          },
          "end": {
            "line": 37,
            "charByteOffset": 14
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
      "value": "r3"
    }
  ],
  "18": [
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
  "19": [
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
  "20": [
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
  "21": [
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
  "22": [
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
  "24": [
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
      "value": 1023
    }
  ],
  "25": [
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
  "26": [
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
  "27": [
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
          "specFile": "Basic.spec",
          "start": {
            "line": 32,
            "charByteOffset": 4
          },
          "end": {
            "line": 32,
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
  "28": [
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
          "specFile": "Basic.spec",
          "start": {
            "line": 32,
            "charByteOffset": 4
          },
          "end": {
            "line": 32,
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
  "29": [
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
          "specFile": "Basic.spec",
          "start": {
            "line": 32,
            "charByteOffset": 4
          },
          "end": {
            "line": 32,
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
  "30": [
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
          "specFile": "Basic.spec",
          "start": {
            "line": 32,
            "charByteOffset": 4
          },
          "end": {
            "line": 32,
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
  "31": [
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
          "specFile": "Basic.spec",
          "start": {
            "line": 33,
            "charByteOffset": 4
          },
          "end": {
            "line": 33,
            "charByteOffset": 15
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
      "value": "num"
    }
  ],
  "32": [
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
          "specFile": "Basic.spec",
          "start": {
            "line": 34,
            "charByteOffset": 4
          },
          "end": {
            "line": 34,
            "charByteOffset": 14
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
      "value": "t"
    }
  ],
  "33": [
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
          "specFile": "Basic.spec",
          "start": {
            "line": 25,
            "charByteOffset": 4
          },
          "end": {
            "line": 25,
            "charByteOffset": 15
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
      "value": "num"
    }
  ],
  "34": [
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
          "specFile": "Basic.spec",
          "start": {
            "line": 26,
            "charByteOffset": 4
          },
          "end": {
            "line": 26,
            "charByteOffset": 15
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
      "value": "ret"
    }
  ],
  "35": [
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
          "specFile": "Basic.spec",
          "start": {
            "line": 35,
            "charByteOffset": 4
          },
          "end": {
            "line": 35,
            "charByteOffset": 14
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
      "value": "r1"
    }
  ],
  "36": [
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
          "specFile": "Basic.spec",
          "start": {
            "line": 36,
            "charByteOffset": 4
          },
          "end": {
            "line": 36,
            "charByteOffset": 14
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
      "value": "r2"
    }
  ],
  "37": [
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
          "specFile": "Basic.spec",
          "start": {
            "line": 11,
            "charByteOffset": 17
          },
          "end": {
            "line": 11,
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
      "value": "a"
    }
  ],
  "38": [
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
          "specFile": "Basic.spec",
          "start": {
            "line": 11,
            "charByteOffset": 28
          },
          "end": {
            "line": 11,
            "charByteOffset": 37
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
      "value": "b"
    }
  ],
  "39": [
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
  "40": [
    {
      "key": {
        "name": "cvl.ghost",
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
        "#class": "spec.cvlast.CVLType.PureCVLType.Ghost.Mapping",
        "key": {
          "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
          "k": 256
        },
        "value": {
          "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
          "k": 256
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
        "name": "cvl.display",
        "type": "java.lang.String",
        "erasureStrategy": "CallTrace"
      },
      "value": "ghost_double"
    }
  ],
  "41": [
    {
      "key": {
        "name": "cvl.ghost",
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
        "#class": "spec.cvlast.CVLType.PureCVLType.Ghost.Mapping",
        "key": {
          "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
          "k": 256
        },
        "value": {
          "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.UIntK",
          "k": 256
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
      "value": "ghost_double"
    }
  ],
  "42": [
    {
      "key": {
        "name": "cvl.ghost",
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
      "value": "innerVal"
    }
  ],
  "43": [
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
  "44": [
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
  "45": [
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
          "specFile": "Basic.spec",
          "start": {
            "line": 32,
            "charByteOffset": 4
          },
          "end": {
            "line": 32,
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
          "specFile": "Basic.spec",
          "start": {
            "line": 32,
            "charByteOffset": 4
          },
          "end": {
            "line": 32,
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
          "specFile": "Basic.spec",
          "start": {
            "line": 32,
            "charByteOffset": 4
          },
          "end": {
            "line": 32,
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
          "specFile": "Basic.spec",
          "start": {
            "line": 32,
            "charByteOffset": 4
          },
          "end": {
            "line": 32,
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
          "specFile": "Basic.spec",
          "start": {
            "line": 32,
            "charByteOffset": 4
          },
          "end": {
            "line": 32,
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
          "specFile": "Basic.spec",
          "start": {
            "line": 32,
            "charByteOffset": 4
          },
          "end": {
            "line": 32,
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
  "52": [
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
  "53": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 0
    }
  ],
  "54": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 1
    }
  ],
  "55": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 2
    }
  ],
  "56": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 3
    }
  ],
  "57": [
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
  "58": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 4
    }
  ],
  "59": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 5
    }
  ],
  "60": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 6
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
        "name": "tac.non.zero.var",
        "type": "tac.MetaMap$Companion$NothingValue",
        "erasureStrategy": "Canonical"
      },
      "value": {
      }
    }
  ],
  "62": [
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
  "63": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 7
    }
  ],
  "64": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 8
    }
  ],
  "65": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 9
    }
  ],
  "66": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 10
    }
  ],
  "67": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 11
    }
  ],
  "68": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 12
    }
  ],
  "69": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 13
    }
  ],
  "70": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 14
    }
  ],
  "71": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 15
    }
  ],
  "72": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 16
    }
  ],
  "73": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 17
    }
  ],
  "74": [
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
        "specFile": "Basic.spec",
        "start": {
          "line": 32,
          "charByteOffset": 4
        },
        "end": {
          "line": 32,
          "charByteOffset": 10
        }
      }
    }
  ],
  "75": [
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "Basic.spec",
        "start": {
          "line": 32,
          "charByteOffset": 4
        },
        "end": {
          "line": 32,
          "charByteOffset": 10
        }
      }
    }
  ],
  "76": [
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
        "specFile": "Basic.spec",
        "start": {
          "line": 33,
          "charByteOffset": 4
        },
        "end": {
          "line": 33,
          "charByteOffset": 20
        }
      }
    }
  ],
  "77": [
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
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 2
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
              "specFile": "Basic.spec",
              "start": {
                "line": 33,
                "charByteOffset": 18
              },
              "end": {
                "line": 33,
                "charByteOffset": 19
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
        "specFile": "Basic.spec",
        "start": {
          "line": 33,
          "charByteOffset": 4
        },
        "end": {
          "line": 33,
          "charByteOffset": 20
        }
      }
    }
  ],
  "78": [
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "Basic.spec",
        "start": {
          "line": 33,
          "charByteOffset": 4
        },
        "end": {
          "line": 33,
          "charByteOffset": 20
        }
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
        "specFile": "Basic.spec",
        "start": {
          "line": 34,
          "charByteOffset": 4
        },
        "end": {
          "line": 34,
          "charByteOffset": 14
        }
      }
    }
  ],
  "80": [
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "Basic.spec",
        "start": {
          "line": 34,
          "charByteOffset": 4
        },
        "end": {
          "line": 34,
          "charByteOffset": 14
        }
      }
    }
  ],
  "81": [
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
        "specFile": "Basic.spec",
        "start": {
          "line": 35,
          "charByteOffset": 4
        },
        "end": {
          "line": 35,
          "charByteOffset": 24
        }
      }
    }
  ],
  "82": [
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "Basic.spec",
        "start": {
          "line": 35,
          "charByteOffset": 4
        },
        "end": {
          "line": 35,
          "charByteOffset": 24
        }
      }
    }
  ],
  "83": [
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
        "specFile": "Basic.spec",
        "start": {
          "line": 25,
          "charByteOffset": 4
        },
        "end": {
          "line": 25,
          "charByteOffset": 21
        }
      }
    }
  ],
  "84": [
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
          "n": "a",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                  "scopeId": 4
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
              "n": "a"
            },
            "range": {
              "#class": "utils.Range.Range",
              "specFile": "Basic.spec",
              "start": {
                "line": 25,
                "charByteOffset": 18
              },
              "end": {
                "line": 25,
                "charByteOffset": 20
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
        "specFile": "Basic.spec",
        "start": {
          "line": 25,
          "charByteOffset": 4
        },
        "end": {
          "line": 25,
          "charByteOffset": 21
        }
      }
    }
  ],
  "85": [
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "Basic.spec",
        "start": {
          "line": 25,
          "charByteOffset": 4
        },
        "end": {
          "line": 25,
          "charByteOffset": 21
        }
      }
    }
  ],
  "86": [
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
        "specFile": "Basic.spec",
        "start": {
          "line": 26,
          "charByteOffset": 4
        },
        "end": {
          "line": 26,
          "charByteOffset": 21
        }
      }
    }
  ],
  "87": [
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
          "n": "14",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                  "scopeId": 4
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
              "n": "14"
            },
            "range": {
              "#class": "utils.Range.Range",
              "specFile": "Basic.spec",
              "start": {
                "line": 26,
                "charByteOffset": 18
              },
              "end": {
                "line": 26,
                "charByteOffset": 20
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
        "specFile": "Basic.spec",
        "start": {
          "line": 26,
          "charByteOffset": 4
        },
        "end": {
          "line": 26,
          "charByteOffset": 21
        }
      }
    }
  ],
  "88": [
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "Basic.spec",
        "start": {
          "line": 26,
          "charByteOffset": 4
        },
        "end": {
          "line": 26,
          "charByteOffset": 21
        }
      }
    }
  ],
  "89": [
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
        "specFile": "Basic.spec",
        "start": {
          "line": 27,
          "charByteOffset": 4
        },
        "end": {
          "line": 27,
          "charByteOffset": 22
        }
      }
    }
  ],
  "90": [
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
          "id": "ret",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                  "scopeId": 4
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
              "specFile": "Basic.spec",
              "start": {
                "line": 27,
                "charByteOffset": 12
              },
              "end": {
                "line": 27,
                "charByteOffset": 15
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
        "specFile": "Basic.spec",
        "start": {
          "line": 27,
          "charByteOffset": 4
        },
        "end": {
          "line": 27,
          "charByteOffset": 22
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
          "id": "num",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                  "scopeId": 4
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
              "specFile": "Basic.spec",
              "start": {
                "line": 27,
                "charByteOffset": 18
              },
              "end": {
                "line": 27,
                "charByteOffset": 21
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
        "specFile": "Basic.spec",
        "start": {
          "line": 27,
          "charByteOffset": 4
        },
        "end": {
          "line": 27,
          "charByteOffset": 22
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
        "#class": "spec.CVLExpToTACExprMeta.BinaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.RelopExp.ArithRelopExp.GtExp",
          "l": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "ret",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                    "scopeId": 4
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
                "specFile": "Basic.spec",
                "start": {
                  "line": 27,
                  "charByteOffset": 12
                },
                "end": {
                  "line": 27,
                  "charByteOffset": 15
                }
              }
            },
            "twoStateIndex": "NEITHER"
          },
          "r": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "num",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                    "scopeId": 4
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
                "specFile": "Basic.spec",
                "start": {
                  "line": 27,
                  "charByteOffset": 18
                },
                "end": {
                  "line": 27,
                  "charByteOffset": 21
                }
              }
            },
            "twoStateIndex": "NEITHER"
          },
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                  "scopeId": 4
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
              "specFile": "Basic.spec",
              "start": {
                "line": 27,
                "charByteOffset": 12
              },
              "end": {
                "line": 27,
                "charByteOffset": 21
              }
            }
          }
        },
        "o1": {
          "out": {
            "#class": "vc.data.TACSymbol.Const",
            "value": "14",
            "tag": {
              "#class": "tac.Tag.Int"
            }
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "ret",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                    "scopeId": 4
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
                "specFile": "Basic.spec",
                "start": {
                  "line": 27,
                  "charByteOffset": 12
                },
                "end": {
                  "line": 27,
                  "charByteOffset": 15
                }
              }
            },
            "twoStateIndex": "NEITHER"
          }
        },
        "o2": {
          "out": {
            "#class": "vc.data.TACSymbol.Const",
            "value": "a",
            "tag": {
              "#class": "tac.Tag.Int"
            }
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "num",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                    "scopeId": 4
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
                "specFile": "Basic.spec",
                "start": {
                  "line": 27,
                  "charByteOffset": 18
                },
                "end": {
                  "line": 27,
                  "charByteOffset": 21
                }
              }
            },
            "twoStateIndex": "NEITHER"
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
        "specFile": "Basic.spec",
        "start": {
          "line": 27,
          "charByteOffset": 4
        },
        "end": {
          "line": 27,
          "charByteOffset": 22
        }
      }
    }
  ],
  "93": [
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "Basic.spec",
        "start": {
          "line": 27,
          "charByteOffset": 4
        },
        "end": {
          "line": 27,
          "charByteOffset": 22
        }
      }
    }
  ],
  "94": [
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
          "id": "ret",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.CVLFunctionScopeItem",
                  "scopeId": 4
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
              "specFile": "Basic.spec",
              "start": {
                "line": 28,
                "charByteOffset": 11
              },
              "end": {
                "line": 28,
                "charByteOffset": 14
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
        "specFile": "Basic.spec",
        "start": {
          "line": 28,
          "charByteOffset": 4
        },
        "end": {
          "line": 28,
          "charByteOffset": 15
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
        "specFile": "Basic.spec",
        "start": {
          "line": 35,
          "charByteOffset": 4
        },
        "end": {
          "line": 35,
          "charByteOffset": 24
        }
      }
    }
  ],
  "96": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 26
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "Basic.spec",
        "start": {
          "line": 36,
          "charByteOffset": 4
        },
        "end": {
          "line": 36,
          "charByteOffset": 30
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
          "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
          "n": "4",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 2
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
              "n": "4"
            },
            "range": {
              "#class": "utils.Range.Range",
              "specFile": "Basic.spec",
              "start": {
                "line": 36,
                "charByteOffset": 24
              },
              "end": {
                "line": 36,
                "charByteOffset": 25
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
        "specFile": "Basic.spec",
        "start": {
          "line": 36,
          "charByteOffset": 4
        },
        "end": {
          "line": 36,
          "charByteOffset": 30
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
          "n": "5",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 2
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
              "specFile": "Basic.spec",
              "start": {
                "line": 36,
                "charByteOffset": 27
              },
              "end": {
                "line": 36,
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
        "specFile": "Basic.spec",
        "start": {
          "line": 36,
          "charByteOffset": 4
        },
        "end": {
          "line": 36,
          "charByteOffset": 30
        }
      }
    }
  ],
  "99": [
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "Basic.spec",
        "start": {
          "line": 36,
          "charByteOffset": 4
        },
        "end": {
          "line": 36,
          "charByteOffset": 30
        }
      }
    }
  ],
  "100": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Const",
        "value": "4"
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
        "specFile": "Basic.spec",
        "start": {
          "line": 36,
          "charByteOffset": 4
        },
        "end": {
          "line": 36,
          "charByteOffset": 30
        }
      }
    }
  ],
  "101": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Const",
        "value": "5"
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
        "specFile": "Basic.spec",
        "start": {
          "line": 36,
          "charByteOffset": 4
        },
        "end": {
          "line": 36,
          "charByteOffset": 30
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
        "specFile": "Basic.spec",
        "start": {
          "line": 36,
          "charByteOffset": 4
        },
        "end": {
          "line": 36,
          "charByteOffset": 30
        }
      }
    }
  ],
  "103": [
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
        "specFile": "Basic.spec",
        "start": {
          "line": 36,
          "charByteOffset": 4
        },
        "end": {
          "line": 36,
          "charByteOffset": 30
        }
      }
    }
  ],
  "104": [
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
        "specFile": "Basic.spec",
        "start": {
          "line": 36,
          "charByteOffset": 4
        },
        "end": {
          "line": 36,
          "charByteOffset": 30
        }
      }
    }
  ],
  "105": [
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
        "specFile": "Basic.spec",
        "start": {
          "line": 36,
          "charByteOffset": 4
        },
        "end": {
          "line": 36,
          "charByteOffset": 30
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
        "specFile": "Basic.spec",
        "start": {
          "line": 36,
          "charByteOffset": 4
        },
        "end": {
          "line": 36,
          "charByteOffset": 30
        }
      }
    }
  ],
  "107": [
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
        "specFile": "Basic.spec",
        "start": {
          "line": 36,
          "charByteOffset": 4
        },
        "end": {
          "line": 36,
          "charByteOffset": 30
        }
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
        "namePrefix": "CANON36",
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
        "specFile": "Basic.spec",
        "start": {
          "line": 36,
          "charByteOffset": 4
        },
        "end": {
          "line": 36,
          "charByteOffset": 30
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
        "namePrefix": "CANON37",
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
        "specFile": "Basic.spec",
        "start": {
          "line": 36,
          "charByteOffset": 4
        },
        "end": {
          "line": 36,
          "charByteOffset": 30
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
        "namePrefix": "CANON38",
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
        "specFile": "Basic.spec",
        "start": {
          "line": 36,
          "charByteOffset": 4
        },
        "end": {
          "line": 36,
          "charByteOffset": 30
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
        "namePrefix": "CANON39",
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
        "specFile": "Basic.spec",
        "start": {
          "line": 36,
          "charByteOffset": 4
        },
        "end": {
          "line": 36,
          "charByteOffset": 30
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
        "namePrefix": "CANON40",
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
        "specFile": "Basic.spec",
        "start": {
          "line": 36,
          "charByteOffset": 4
        },
        "end": {
          "line": 36,
          "charByteOffset": 30
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
        "namePrefix": "CANON41",
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
        "specFile": "Basic.spec",
        "start": {
          "line": 36,
          "charByteOffset": 4
        },
        "end": {
          "line": 36,
          "charByteOffset": 30
        }
      }
    }
  ],
  "114": [
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
        "specFile": "Basic.spec",
        "start": {
          "line": 36,
          "charByteOffset": 4
        },
        "end": {
          "line": 36,
          "charByteOffset": 30
        }
      }
    }
  ],
  "115": [
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
  "116": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 25,
        "len": 1996,
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
        "specFile": "Basic.spec",
        "start": {
          "line": 36,
          "charByteOffset": 4
        },
        "end": {
          "line": 36,
          "charByteOffset": 30
        }
      }
    }
  ],
  "117": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 75,
        "len": 425,
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
        "specFile": "Basic.spec",
        "start": {
          "line": 36,
          "charByteOffset": 4
        },
        "end": {
          "line": 36,
          "charByteOffset": 30
        }
      }
    }
  ],
  "118": [
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
          "id": "a",
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
              "specFile": "Basic.spec",
              "start": {
                "line": 12,
                "charByteOffset": 27
              },
              "end": {
                "line": 12,
                "charByteOffset": 28
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
        "specFile": "Basic.spec",
        "start": {
          "line": 12,
          "charByteOffset": 4
        },
        "end": {
          "line": 12,
          "charByteOffset": 34
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
          "#class": "spec.cvlast.CVLExp.VariableExp",
          "id": "b",
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
              "specFile": "Basic.spec",
              "start": {
                "line": 12,
                "charByteOffset": 31
              },
              "end": {
                "line": 12,
                "charByteOffset": 32
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
        "specFile": "Basic.spec",
        "start": {
          "line": 12,
          "charByteOffset": 4
        },
        "end": {
          "line": 12,
          "charByteOffset": 34
        }
      }
    }
  ],
  "120": [
    {
      "key": {
        "name": "cvl.exp",
        "type": "spec.CVLExpToTACExprMeta",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "spec.CVLExpToTACExprMeta.BinaryCVLExp",
        "exp": {
          "#class": "spec.cvlast.CVLExp.BinaryExp.AddExp",
          "l": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "a",
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
                "specFile": "Basic.spec",
                "start": {
                  "line": 12,
                  "charByteOffset": 27
                },
                "end": {
                  "line": 12,
                  "charByteOffset": 28
                }
              }
            },
            "twoStateIndex": "NEITHER"
          },
          "r": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "b",
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
                "specFile": "Basic.spec",
                "start": {
                  "line": 12,
                  "charByteOffset": 31
                },
                "end": {
                  "line": 12,
                  "charByteOffset": 32
                }
              }
            },
            "twoStateIndex": "NEITHER"
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
              "#class": "spec.cvlast.CVLType.PureCVLType.Primitive.Mathint"
            },
            "range": {
              "#class": "utils.Range.Range",
              "specFile": "Basic.spec",
              "start": {
                "line": 12,
                "charByteOffset": 27
              },
              "end": {
                "line": 12,
                "charByteOffset": 32
              }
            }
          }
        },
        "o1": {
          "out": {
            "#class": "vc.data.TACSymbol.Const",
            "value": "4",
            "tag": {
              "#class": "tac.Tag.Int"
            }
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "a",
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
                "specFile": "Basic.spec",
                "start": {
                  "line": 12,
                  "charByteOffset": 27
                },
                "end": {
                  "line": 12,
                  "charByteOffset": 28
                }
              }
            },
            "twoStateIndex": "NEITHER"
          }
        },
        "o2": {
          "out": {
            "#class": "vc.data.TACSymbol.Const",
            "value": "5",
            "tag": {
              "#class": "tac.Tag.Int"
            }
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "b",
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
                "specFile": "Basic.spec",
                "start": {
                  "line": 12,
                  "charByteOffset": 31
                },
                "end": {
                  "line": 12,
                  "charByteOffset": 32
                }
              }
            },
            "twoStateIndex": "NEITHER"
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
        "specFile": "Basic.spec",
        "start": {
          "line": 12,
          "charByteOffset": 4
        },
        "end": {
          "line": 12,
          "charByteOffset": 34
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
        "specFile": "Basic.spec",
        "start": {
          "line": 12,
          "charByteOffset": 4
        },
        "end": {
          "line": 12,
          "charByteOffset": 34
        }
      }
    }
  ],
  "122": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 27
    }
  ],
  "123": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Const",
        "value": "9",
        "tag": {
          "#class": "tac.Tag.Int"
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
        "begin": 75,
        "len": 425,
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
        "specFile": "Basic.spec",
        "start": {
          "line": 36,
          "charByteOffset": 4
        },
        "end": {
          "line": 36,
          "charByteOffset": 30
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
        "begin": 75,
        "len": 425,
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
        "specFile": "Basic.spec",
        "start": {
          "line": 36,
          "charByteOffset": 4
        },
        "end": {
          "line": 36,
          "charByteOffset": 30
        }
      }
    }
  ],
  "126": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 28
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "Basic.spec",
        "start": {
          "line": 37,
          "charByteOffset": 4
        },
        "end": {
          "line": 37,
          "charByteOffset": 30
        }
      }
    }
  ],
  "127": [
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
          "n": "7",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 2
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
              "n": "7"
            },
            "range": {
              "#class": "utils.Range.Range",
              "specFile": "Basic.spec",
              "start": {
                "line": 37,
                "charByteOffset": 27
              },
              "end": {
                "line": 37,
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
        "specFile": "Basic.spec",
        "start": {
          "line": 37,
          "charByteOffset": 4
        },
        "end": {
          "line": 37,
          "charByteOffset": 30
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
        "specFile": "Basic.spec",
        "start": {
          "line": 37,
          "charByteOffset": 4
        },
        "end": {
          "line": 37,
          "charByteOffset": 30
        }
      }
    }
  ],
  "129": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Const",
        "value": "7"
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
        "specFile": "Basic.spec",
        "start": {
          "line": 37,
          "charByteOffset": 4
        },
        "end": {
          "line": 37,
          "charByteOffset": 30
        }
      }
    }
  ],
  "130": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON62",
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
        "specFile": "Basic.spec",
        "start": {
          "line": 37,
          "charByteOffset": 4
        },
        "end": {
          "line": 37,
          "charByteOffset": 30
        }
      }
    }
  ],
  "131": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON63",
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
        "specFile": "Basic.spec",
        "start": {
          "line": 37,
          "charByteOffset": 4
        },
        "end": {
          "line": 37,
          "charByteOffset": 30
        }
      }
    }
  ],
  "132": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON64",
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
        "specFile": "Basic.spec",
        "start": {
          "line": 37,
          "charByteOffset": 4
        },
        "end": {
          "line": 37,
          "charByteOffset": 30
        }
      }
    }
  ],
  "133": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON65",
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
        "specFile": "Basic.spec",
        "start": {
          "line": 37,
          "charByteOffset": 4
        },
        "end": {
          "line": 37,
          "charByteOffset": 30
        }
      }
    }
  ],
  "134": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON66",
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
        "specFile": "Basic.spec",
        "start": {
          "line": 37,
          "charByteOffset": 4
        },
        "end": {
          "line": 37,
          "charByteOffset": 30
        }
      }
    }
  ],
  "135": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON67",
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
        "specFile": "Basic.spec",
        "start": {
          "line": 37,
          "charByteOffset": 4
        },
        "end": {
          "line": 37,
          "charByteOffset": 30
        }
      }
    }
  ],
  "136": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON68",
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
        "specFile": "Basic.spec",
        "start": {
          "line": 37,
          "charByteOffset": 4
        },
        "end": {
          "line": 37,
          "charByteOffset": 30
        }
      }
    }
  ],
  "137": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON69",
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
        "specFile": "Basic.spec",
        "start": {
          "line": 37,
          "charByteOffset": 4
        },
        "end": {
          "line": 37,
          "charByteOffset": 30
        }
      }
    }
  ],
  "138": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON70",
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
        "specFile": "Basic.spec",
        "start": {
          "line": 37,
          "charByteOffset": 4
        },
        "end": {
          "line": 37,
          "charByteOffset": 30
        }
      }
    }
  ],
  "139": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON71",
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
        "specFile": "Basic.spec",
        "start": {
          "line": 37,
          "charByteOffset": 4
        },
        "end": {
          "line": 37,
          "charByteOffset": 30
        }
      }
    }
  ],
  "140": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON72",
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
        "specFile": "Basic.spec",
        "start": {
          "line": 37,
          "charByteOffset": 4
        },
        "end": {
          "line": 37,
          "charByteOffset": 30
        }
      }
    }
  ],
  "141": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON73",
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
        "specFile": "Basic.spec",
        "start": {
          "line": 37,
          "charByteOffset": 4
        },
        "end": {
          "line": 37,
          "charByteOffset": 30
        }
      }
    }
  ],
  "142": [
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
        "specFile": "Basic.spec",
        "start": {
          "line": 37,
          "charByteOffset": 4
        },
        "end": {
          "line": 37,
          "charByteOffset": 30
        }
      }
    }
  ],
  "143": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 25,
        "len": 1996,
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
        "specFile": "Basic.spec",
        "start": {
          "line": 37,
          "charByteOffset": 4
        },
        "end": {
          "line": 37,
          "charByteOffset": 30
        }
      }
    }
  ],
  "144": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 506,
        "len": 417,
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
        "specFile": "Basic.spec",
        "start": {
          "line": 37,
          "charByteOffset": 4
        },
        "end": {
          "line": 37,
          "charByteOffset": 30
        }
      }
    }
  ],
  "145": [
    {
      "key": {
        "name": "assert.format.arg.1",
        "type": "vc.data.TACSymbol",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "#class": "vc.data.TACSymbol.Var.Full",
        "namePrefix": "CANON83",
        "tag": {
          "#class": "tac.Tag.Int"
        },
        "callIndex": 0
      }
    }
  ],
  "146": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 506,
        "len": 417,
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
        "specFile": "Basic.spec",
        "start": {
          "line": 37,
          "charByteOffset": 4
        },
        "end": {
          "line": 37,
          "charByteOffset": 30
        }
      }
    }
  ],
  "147": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 506,
        "len": 417,
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
        "specFile": "Basic.spec",
        "start": {
          "line": 37,
          "charByteOffset": 4
        },
        "end": {
          "line": 37,
          "charByteOffset": 30
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
      "value": 29
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "Basic.spec",
        "start": {
          "line": 38,
          "charByteOffset": 4
        },
        "end": {
          "line": 38,
          "charByteOffset": 26
        }
      }
    }
  ],
  "149": [
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "Basic.spec",
        "start": {
          "line": 38,
          "charByteOffset": 4
        },
        "end": {
          "line": 38,
          "charByteOffset": 26
        }
      }
    }
  ],
  "150": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 25,
        "len": 1996,
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
        "specFile": "Basic.spec",
        "start": {
          "line": 38,
          "charByteOffset": 4
        },
        "end": {
          "line": 38,
          "charByteOffset": 26
        }
      }
    }
  ],
  "151": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 929,
        "len": 328,
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
        "specFile": "Basic.spec",
        "start": {
          "line": 38,
          "charByteOffset": 4
        },
        "end": {
          "line": 38,
          "charByteOffset": 26
        }
      }
    }
  ],
  "152": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 30
    }
  ],
  "153": [
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
          "n": "1",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.HookScopeItem",
                  "scopeId": 5
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
              "n": "1"
            },
            "range": {
              "#class": "utils.Range.Range",
              "specFile": "Basic.spec",
              "start": {
                "line": 16,
                "charByteOffset": 26
              },
              "end": {
                "line": 16,
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
        "specFile": "Basic.spec",
        "start": {
          "line": 16,
          "charByteOffset": 4
        },
        "end": {
          "line": 16,
          "charByteOffset": 28
        }
      }
    }
  ],
  "154": [
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
            "id": "contractVal",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.HookScopeItem",
                    "scopeId": 5
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
                  "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                  "bitwidth": 256
                },
                "context": {
                  "#class": "spec.cvlast.typedescriptors.FromVMContext.HookValue"
                }
              },
              "range": {
                "#class": "utils.Range.Range",
                "specFile": "Basic.spec",
                "start": {
                  "line": 16,
                  "charByteOffset": 12
                },
                "end": {
                  "line": 16,
                  "charByteOffset": 23
                }
              }
            },
            "twoStateIndex": "NEITHER"
          },
          "r": {
            "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
            "n": "1",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.HookScopeItem",
                    "scopeId": 5
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
                "n": "1"
              },
              "range": {
                "#class": "utils.Range.Range",
                "specFile": "Basic.spec",
                "start": {
                  "line": 16,
                  "charByteOffset": 26
                },
                "end": {
                  "line": 16,
                  "charByteOffset": 27
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
                  "#class": "spec.cvlast.CVLScope.Item.HookScopeItem",
                  "scopeId": 5
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
              "specFile": "Basic.spec",
              "start": {
                "line": 16,
                "charByteOffset": 12
              },
              "end": {
                "line": 16,
                "charByteOffset": 27
              }
            }
          }
        },
        "o1": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "CANON88!!8",
            "tag": {
              "#class": "tac.Tag.Bit256"
            },
            "callIndex": 0,
            "meta": [
              {
                "key": {
                  "name": "tac.storage.non-indexed-path.family",
                  "type": "analysis.storage.StorageAnalysisResult$StoragePaths",
                  "erasureStrategy": "Canonical"
                },
                "value": {
                  "storagePaths": [
                    {
                      "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
                      "slot": "0"
                    }
                  ]
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
                  "name": "L",
                  "maybeTACKeywordOrdinal": 45
                }
              },
              {
                "key": {
                  "name": "tac.scalarization.sort",
                  "type": "vc.data.ScalarizationSort",
                  "erasureStrategy": "Canonical"
                },
                "value": {
                  "#class": "vc.data.ScalarizationSort.Split",
                  "idx": "0"
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
                  "name": "tac.storage.pretty.paths",
                  "type": "analysis.storage.DisplayPaths",
                  "erasureStrategy": "Erased"
                },
                "value": {
                  "paths": [
                    {
                      "#class": "analysis.storage.DisplayPath.Root",
                      "name": "val"
                    }
                  ]
                }
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
                  "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
                  "slot": "0"
                }
              },
              {
                "key": {
                  "name": "tac.storage",
                  "type": "java.math.BigInteger",
                  "erasureStrategy": "Canonical"
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
              }
            ]
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "contractVal",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.HookScopeItem",
                    "scopeId": 5
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
                  "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                  "bitwidth": 256
                },
                "context": {
                  "#class": "spec.cvlast.typedescriptors.FromVMContext.HookValue"
                }
              },
              "range": {
                "#class": "utils.Range.Range",
                "specFile": "Basic.spec",
                "start": {
                  "line": 16,
                  "charByteOffset": 12
                },
                "end": {
                  "line": 16,
                  "charByteOffset": 23
                }
              }
            },
            "twoStateIndex": "NEITHER"
          }
        },
        "o2": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "CANON91",
            "tag": {
              "#class": "tac.Tag.Int"
            },
            "callIndex": 0
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
            "n": "1",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.HookScopeItem",
                    "scopeId": 5
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
                "n": "1"
              },
              "range": {
                "#class": "utils.Range.Range",
                "specFile": "Basic.spec",
                "start": {
                  "line": 16,
                  "charByteOffset": 26
                },
                "end": {
                  "line": 16,
                  "charByteOffset": 27
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
        "specFile": "Basic.spec",
        "start": {
          "line": 16,
          "charByteOffset": 4
        },
        "end": {
          "line": 16,
          "charByteOffset": 28
        }
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
          "id": "innerVal",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.HookScopeItem",
                  "scopeId": 5
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
              "specFile": "Basic.spec",
              "start": {
                "line": 17,
                "charByteOffset": 12
              },
              "end": {
                "line": 17,
                "charByteOffset": 20
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
        "specFile": "Basic.spec",
        "start": {
          "line": 17,
          "charByteOffset": 4
        },
        "end": {
          "line": 17,
          "charByteOffset": 36
        }
      }
    }
  ],
  "156": [
    {
      "key": {
        "name": "cvl.ghost",
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
      "value": "innerVal"
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
  "157": [
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "Basic.spec",
        "start": {
          "line": 17,
          "charByteOffset": 4
        },
        "end": {
          "line": 17,
          "charByteOffset": 36
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
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "innerVal",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.HookScopeItem",
                    "scopeId": 5
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
                "specFile": "Basic.spec",
                "start": {
                  "line": 17,
                  "charByteOffset": 12
                },
                "end": {
                  "line": 17,
                  "charByteOffset": 20
                }
              }
            },
            "twoStateIndex": "NEITHER"
          },
          "r": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "contractVal",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.HookScopeItem",
                    "scopeId": 5
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
                  "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                  "bitwidth": 256
                },
                "context": {
                  "#class": "spec.cvlast.typedescriptors.FromVMContext.HookValue"
                }
              },
              "range": {
                "#class": "utils.Range.Range",
                "specFile": "Basic.spec",
                "start": {
                  "line": 17,
                  "charByteOffset": 24
                },
                "end": {
                  "line": 17,
                  "charByteOffset": 35
                }
              }
            },
            "twoStateIndex": "NEITHER"
          },
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.HookScopeItem",
                  "scopeId": 5
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
              "specFile": "Basic.spec",
              "start": {
                "line": 17,
                "charByteOffset": 12
              },
              "end": {
                "line": 17,
                "charByteOffset": 35
              }
            }
          }
        },
        "o1": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "I85",
            "tag": {
              "#class": "tac.Tag.Int"
            },
            "callIndex": 0
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "innerVal",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.HookScopeItem",
                    "scopeId": 5
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
                "specFile": "Basic.spec",
                "start": {
                  "line": 17,
                  "charByteOffset": 12
                },
                "end": {
                  "line": 17,
                  "charByteOffset": 20
                }
              }
            },
            "twoStateIndex": "NEITHER"
          }
        },
        "o2": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "CANON88!!8",
            "tag": {
              "#class": "tac.Tag.Bit256"
            },
            "callIndex": 0,
            "meta": [
              {
                "key": {
                  "name": "tac.storage.non-indexed-path.family",
                  "type": "analysis.storage.StorageAnalysisResult$StoragePaths",
                  "erasureStrategy": "Canonical"
                },
                "value": {
                  "storagePaths": [
                    {
                      "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
                      "slot": "0"
                    }
                  ]
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
                  "name": "L",
                  "maybeTACKeywordOrdinal": 45
                }
              },
              {
                "key": {
                  "name": "tac.scalarization.sort",
                  "type": "vc.data.ScalarizationSort",
                  "erasureStrategy": "Canonical"
                },
                "value": {
                  "#class": "vc.data.ScalarizationSort.Split",
                  "idx": "0"
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
                  "name": "tac.storage.pretty.paths",
                  "type": "analysis.storage.DisplayPaths",
                  "erasureStrategy": "Erased"
                },
                "value": {
                  "paths": [
                    {
                      "#class": "analysis.storage.DisplayPath.Root",
                      "name": "val"
                    }
                  ]
                }
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
                  "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
                  "slot": "0"
                }
              },
              {
                "key": {
                  "name": "tac.storage",
                  "type": "java.math.BigInteger",
                  "erasureStrategy": "Canonical"
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
              }
            ]
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "contractVal",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.HookScopeItem",
                    "scopeId": 5
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
                  "#class": "ReflectivePolymorphicSerializer::spec.cvlast.typedescriptors.EVMTypeDescriptor$UIntK",
                  "bitwidth": 256
                },
                "context": {
                  "#class": "spec.cvlast.typedescriptors.FromVMContext.HookValue"
                }
              },
              "range": {
                "#class": "utils.Range.Range",
                "specFile": "Basic.spec",
                "start": {
                  "line": 17,
                  "charByteOffset": 24
                },
                "end": {
                  "line": 17,
                  "charByteOffset": 35
                }
              }
            },
            "twoStateIndex": "NEITHER"
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
        "specFile": "Basic.spec",
        "start": {
          "line": 17,
          "charByteOffset": 4
        },
        "end": {
          "line": 17,
          "charByteOffset": 36
        }
      }
    }
  ],
  "159": [
    {
      "key": {
        "name": "tac.storage.non-indexed-path.family",
        "type": "analysis.storage.StorageAnalysisResult$StoragePaths",
        "erasureStrategy": "Canonical"
      },
      "value": {
        "storagePaths": [
          {
            "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
            "slot": "0"
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
        "#class": "vc.data.ScalarizationSort.Split",
        "idx": "0"
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
        "name": "tac.storage.pretty.paths",
        "type": "analysis.storage.DisplayPaths",
        "erasureStrategy": "Erased"
      },
      "value": {
        "paths": [
          {
            "#class": "analysis.storage.DisplayPath.Root",
            "name": "val"
          }
        ]
      }
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
        "#class": "analysis.storage.StorageAnalysisResult.NonIndexedPath.Root",
        "slot": "0"
      }
    },
    {
      "key": {
        "name": "tac.storage",
        "type": "java.math.BigInteger",
        "erasureStrategy": "Canonical"
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
  "160": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 929,
        "len": 328,
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
        "specFile": "Basic.spec",
        "start": {
          "line": 38,
          "charByteOffset": 4
        },
        "end": {
          "line": 38,
          "charByteOffset": 26
        }
      }
    }
  ],
  "161": [
    {
      "key": {
        "name": "tac.meta",
        "type": "vc.data.TACMetaInfo",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "source": 0,
        "begin": 929,
        "len": 328,
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
        "specFile": "Basic.spec",
        "start": {
          "line": 38,
          "charByteOffset": 4
        },
        "end": {
          "line": 38,
          "charByteOffset": 26
        }
      }
    }
  ],
  "162": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 31
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "Basic.spec",
        "start": {
          "line": 39,
          "charByteOffset": 4
        },
        "end": {
          "line": 39,
          "charByteOffset": 20
        }
      }
    }
  ],
  "163": [
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
          "id": "t",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 2
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
              "specFile": "Basic.spec",
              "start": {
                "line": 39,
                "charByteOffset": 12
              },
              "end": {
                "line": 39,
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
        "specFile": "Basic.spec",
        "start": {
          "line": 39,
          "charByteOffset": 4
        },
        "end": {
          "line": 39,
          "charByteOffset": 20
        }
      }
    }
  ],
  "164": [
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
          "id": "num",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 2
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
              "specFile": "Basic.spec",
              "start": {
                "line": 39,
                "charByteOffset": 16
              },
              "end": {
                "line": 39,
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
        "specFile": "Basic.spec",
        "start": {
          "line": 39,
          "charByteOffset": 4
        },
        "end": {
          "line": 39,
          "charByteOffset": 20
        }
      }
    }
  ],
  "165": [
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
            "id": "t",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 2
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
                "specFile": "Basic.spec",
                "start": {
                  "line": 39,
                  "charByteOffset": 12
                },
                "end": {
                  "line": 39,
                  "charByteOffset": 13
                }
              }
            },
            "twoStateIndex": "NEITHER"
          },
          "r": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "num",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 2
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
                "specFile": "Basic.spec",
                "start": {
                  "line": 39,
                  "charByteOffset": 16
                },
                "end": {
                  "line": 39,
                  "charByteOffset": 19
                }
              }
            },
            "twoStateIndex": "NEITHER"
          },
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 2
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
              "specFile": "Basic.spec",
              "start": {
                "line": 39,
                "charByteOffset": 12
              },
              "end": {
                "line": 39,
                "charByteOffset": 19
              }
            }
          }
        },
        "o1": {
          "out": {
            "#class": "vc.data.TACSymbol.Const",
            "value": "14",
            "tag": {
              "#class": "tac.Tag.Int"
            }
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "t",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 2
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
                "specFile": "Basic.spec",
                "start": {
                  "line": 39,
                  "charByteOffset": 12
                },
                "end": {
                  "line": 39,
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
            "value": "5",
            "tag": {
              "#class": "tac.Tag.Int"
            }
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "num",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 2
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
                "specFile": "Basic.spec",
                "start": {
                  "line": 39,
                  "charByteOffset": 16
                },
                "end": {
                  "line": 39,
                  "charByteOffset": 19
                }
              }
            },
            "twoStateIndex": "NEITHER"
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
        "specFile": "Basic.spec",
        "start": {
          "line": 39,
          "charByteOffset": 4
        },
        "end": {
          "line": 39,
          "charByteOffset": 20
        }
      }
    }
  ],
  "166": [
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "Basic.spec",
        "start": {
          "line": 39,
          "charByteOffset": 4
        },
        "end": {
          "line": 39,
          "charByteOffset": 20
        }
      }
    }
  ],
  "167": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 32
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "Basic.spec",
        "start": {
          "line": 40,
          "charByteOffset": 4
        },
        "end": {
          "line": 40,
          "charByteOffset": 20
        }
      }
    }
  ],
  "168": [
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
          "id": "t",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 2
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
              "specFile": "Basic.spec",
              "start": {
                "line": 40,
                "charByteOffset": 12
              },
              "end": {
                "line": 40,
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
        "specFile": "Basic.spec",
        "start": {
          "line": 40,
          "charByteOffset": 4
        },
        "end": {
          "line": 40,
          "charByteOffset": 20
        }
      }
    }
  ],
  "169": [
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
          "id": "r1",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 2
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
              "specFile": "Basic.spec",
              "start": {
                "line": 40,
                "charByteOffset": 17
              },
              "end": {
                "line": 40,
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
        "specFile": "Basic.spec",
        "start": {
          "line": 40,
          "charByteOffset": 4
        },
        "end": {
          "line": 40,
          "charByteOffset": 20
        }
      }
    }
  ],
  "170": [
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
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "t",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 2
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
                "specFile": "Basic.spec",
                "start": {
                  "line": 40,
                  "charByteOffset": 12
                },
                "end": {
                  "line": 40,
                  "charByteOffset": 13
                }
              }
            },
            "twoStateIndex": "NEITHER"
          },
          "r": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "r1",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 2
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
                "specFile": "Basic.spec",
                "start": {
                  "line": 40,
                  "charByteOffset": 17
                },
                "end": {
                  "line": 40,
                  "charByteOffset": 19
                }
              }
            },
            "twoStateIndex": "NEITHER"
          },
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 2
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
              "specFile": "Basic.spec",
              "start": {
                "line": 40,
                "charByteOffset": 12
              },
              "end": {
                "line": 40,
                "charByteOffset": 19
              }
            }
          }
        },
        "o1": {
          "out": {
            "#class": "vc.data.TACSymbol.Const",
            "value": "14",
            "tag": {
              "#class": "tac.Tag.Int"
            }
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "t",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 2
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
                "specFile": "Basic.spec",
                "start": {
                  "line": 40,
                  "charByteOffset": 12
                },
                "end": {
                  "line": 40,
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
            "value": "14",
            "tag": {
              "#class": "tac.Tag.Int"
            }
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "r1",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 2
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
                "specFile": "Basic.spec",
                "start": {
                  "line": 40,
                  "charByteOffset": 17
                },
                "end": {
                  "line": 40,
                  "charByteOffset": 19
                }
              }
            },
            "twoStateIndex": "NEITHER"
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
        "specFile": "Basic.spec",
        "start": {
          "line": 40,
          "charByteOffset": 4
        },
        "end": {
          "line": 40,
          "charByteOffset": 20
        }
      }
    }
  ],
  "171": [
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "Basic.spec",
        "start": {
          "line": 40,
          "charByteOffset": 4
        },
        "end": {
          "line": 40,
          "charByteOffset": 20
        }
      }
    }
  ],
  "172": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 33
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "Basic.spec",
        "start": {
          "line": 41,
          "charByteOffset": 4
        },
        "end": {
          "line": 41,
          "charByteOffset": 19
        }
      }
    }
  ],
  "173": [
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
          "id": "r2",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 2
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
              "specFile": "Basic.spec",
              "start": {
                "line": 41,
                "charByteOffset": 11
              },
              "end": {
                "line": 41,
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
        "specFile": "Basic.spec",
        "start": {
          "line": 41,
          "charByteOffset": 4
        },
        "end": {
          "line": 41,
          "charByteOffset": 19
        }
      }
    }
  ],
  "174": [
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
          "n": "9",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 2
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
              "n": "9"
            },
            "range": {
              "#class": "utils.Range.Range",
              "specFile": "Basic.spec",
              "start": {
                "line": 41,
                "charByteOffset": 17
              },
              "end": {
                "line": 41,
                "charByteOffset": 18
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
        "specFile": "Basic.spec",
        "start": {
          "line": 41,
          "charByteOffset": 4
        },
        "end": {
          "line": 41,
          "charByteOffset": 19
        }
      }
    }
  ],
  "175": [
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
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "r2",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 2
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
                "specFile": "Basic.spec",
                "start": {
                  "line": 41,
                  "charByteOffset": 11
                },
                "end": {
                  "line": 41,
                  "charByteOffset": 13
                }
              }
            },
            "twoStateIndex": "NEITHER"
          },
          "r": {
            "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
            "n": "9",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 2
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
                "n": "9"
              },
              "range": {
                "#class": "utils.Range.Range",
                "specFile": "Basic.spec",
                "start": {
                  "line": 41,
                  "charByteOffset": 17
                },
                "end": {
                  "line": 41,
                  "charByteOffset": 18
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
                  "scopeId": 2
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
              "specFile": "Basic.spec",
              "start": {
                "line": 41,
                "charByteOffset": 11
              },
              "end": {
                "line": 41,
                "charByteOffset": 18
              }
            }
          }
        },
        "o1": {
          "out": {
            "#class": "vc.data.TACSymbol.Const",
            "value": "9"
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "r2",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 2
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
                "specFile": "Basic.spec",
                "start": {
                  "line": 41,
                  "charByteOffset": 11
                },
                "end": {
                  "line": 41,
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
            "value": "9"
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
            "n": "9",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 2
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
                "n": "9"
              },
              "range": {
                "#class": "utils.Range.Range",
                "specFile": "Basic.spec",
                "start": {
                  "line": 41,
                  "charByteOffset": 17
                },
                "end": {
                  "line": 41,
                  "charByteOffset": 18
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
        "specFile": "Basic.spec",
        "start": {
          "line": 41,
          "charByteOffset": 4
        },
        "end": {
          "line": 41,
          "charByteOffset": 19
        }
      }
    }
  ],
  "176": [
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
        "specFile": "Basic.spec",
        "start": {
          "line": 41,
          "charByteOffset": 4
        },
        "end": {
          "line": 41,
          "charByteOffset": 19
        }
      }
    }
  ],
  "177": [
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "Basic.spec",
        "start": {
          "line": 41,
          "charByteOffset": 4
        },
        "end": {
          "line": 41,
          "charByteOffset": 19
        }
      }
    }
  ],
  "178": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 34
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "Basic.spec",
        "start": {
          "line": 42,
          "charByteOffset": 4
        },
        "end": {
          "line": 42,
          "charByteOffset": 20
        }
      }
    }
  ],
  "179": [
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
          "id": "r3",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 2
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
              "specFile": "Basic.spec",
              "start": {
                "line": 42,
                "charByteOffset": 11
              },
              "end": {
                "line": 42,
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
        "specFile": "Basic.spec",
        "start": {
          "line": 42,
          "charByteOffset": 4
        },
        "end": {
          "line": 42,
          "charByteOffset": 20
        }
      }
    }
  ],
  "180": [
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
          "n": "e",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 2
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
              "n": "e"
            },
            "range": {
              "#class": "utils.Range.Range",
              "specFile": "Basic.spec",
              "start": {
                "line": 42,
                "charByteOffset": 17
              },
              "end": {
                "line": 42,
                "charByteOffset": 19
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
        "specFile": "Basic.spec",
        "start": {
          "line": 42,
          "charByteOffset": 4
        },
        "end": {
          "line": 42,
          "charByteOffset": 20
        }
      }
    }
  ],
  "181": [
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
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "r3",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 2
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
                "specFile": "Basic.spec",
                "start": {
                  "line": 42,
                  "charByteOffset": 11
                },
                "end": {
                  "line": 42,
                  "charByteOffset": 13
                }
              }
            },
            "twoStateIndex": "NEITHER"
          },
          "r": {
            "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
            "n": "e",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 2
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
                "n": "e"
              },
              "range": {
                "#class": "utils.Range.Range",
                "specFile": "Basic.spec",
                "start": {
                  "line": 42,
                  "charByteOffset": 17
                },
                "end": {
                  "line": 42,
                  "charByteOffset": 19
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
                  "scopeId": 2
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
              "specFile": "Basic.spec",
              "start": {
                "line": 42,
                "charByteOffset": 11
              },
              "end": {
                "line": 42,
                "charByteOffset": 19
              }
            }
          }
        },
        "o1": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "I97",
            "tag": {
              "#class": "tac.Tag.Int"
            },
            "callIndex": 0
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "r3",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 2
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
                "specFile": "Basic.spec",
                "start": {
                  "line": 42,
                  "charByteOffset": 11
                },
                "end": {
                  "line": 42,
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
            "value": "e"
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
            "n": "e",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 2
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
                "n": "e"
              },
              "range": {
                "#class": "utils.Range.Range",
                "specFile": "Basic.spec",
                "start": {
                  "line": 42,
                  "charByteOffset": 17
                },
                "end": {
                  "line": 42,
                  "charByteOffset": 19
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
        "specFile": "Basic.spec",
        "start": {
          "line": 42,
          "charByteOffset": 4
        },
        "end": {
          "line": 42,
          "charByteOffset": 20
        }
      }
    }
  ],
  "182": [
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
        "specFile": "Basic.spec",
        "start": {
          "line": 42,
          "charByteOffset": 4
        },
        "end": {
          "line": 42,
          "charByteOffset": 20
        }
      }
    }
  ],
  "183": [
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "Basic.spec",
        "start": {
          "line": 42,
          "charByteOffset": 4
        },
        "end": {
          "line": 42,
          "charByteOffset": 20
        }
      }
    }
  ],
  "184": [
    {
      "key": {
        "name": "cvl.label.start.id",
        "type": "java.lang.Integer",
        "erasureStrategy": "Canonical"
      },
      "value": 35
    },
    {
      "key": {
        "name": "cvl.range",
        "type": "utils.Range",
        "erasureStrategy": "CallTrace"
      },
      "value": {
        "#class": "utils.Range.Range",
        "specFile": "Basic.spec",
        "start": {
          "line": 43,
          "charByteOffset": 4
        },
        "end": {
          "line": 43,
          "charByteOffset": 19
        }
      }
    }
  ],
  "185": [
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
          "id": "r4",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 2
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
              "specFile": "Basic.spec",
              "start": {
                "line": 43,
                "charByteOffset": 11
              },
              "end": {
                "line": 43,
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
        "specFile": "Basic.spec",
        "start": {
          "line": 43,
          "charByteOffset": 4
        },
        "end": {
          "line": 43,
          "charByteOffset": 19
        }
      }
    }
  ],
  "186": [
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
          "specFile": "Basic.spec",
          "start": {
            "line": 38,
            "charByteOffset": 4
          },
          "end": {
            "line": 38,
            "charByteOffset": 14
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
      "value": "r4"
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
  "187": [
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
          "n": "1",
          "tag": {
            "scope": {
              "scopeStack": [
                {
                  "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                },
                {
                  "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                  "scopeId": 2
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
              "n": "1"
            },
            "range": {
              "#class": "utils.Range.Range",
              "specFile": "Basic.spec",
              "start": {
                "line": 43,
                "charByteOffset": 17
              },
              "end": {
                "line": 43,
                "charByteOffset": 18
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
        "specFile": "Basic.spec",
        "start": {
          "line": 43,
          "charByteOffset": 4
        },
        "end": {
          "line": 43,
          "charByteOffset": 19
        }
      }
    }
  ],
  "188": [
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
            "#class": "spec.cvlast.CVLExp.VariableExp",
            "id": "r4",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 2
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
                "specFile": "Basic.spec",
                "start": {
                  "line": 43,
                  "charByteOffset": 11
                },
                "end": {
                  "line": 43,
                  "charByteOffset": 13
                }
              }
            },
            "twoStateIndex": "NEITHER"
          },
          "r": {
            "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
            "n": "1",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 2
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
                "n": "1"
              },
              "range": {
                "#class": "utils.Range.Range",
                "specFile": "Basic.spec",
                "start": {
                  "line": 43,
                  "charByteOffset": 17
                },
                "end": {
                  "line": 43,
                  "charByteOffset": 18
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
                  "scopeId": 2
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
              "specFile": "Basic.spec",
              "start": {
                "line": 43,
                "charByteOffset": 11
              },
              "end": {
                "line": 43,
                "charByteOffset": 18
              }
            }
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
            "id": "r4",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 2
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
                "specFile": "Basic.spec",
                "start": {
                  "line": 43,
                  "charByteOffset": 11
                },
                "end": {
                  "line": 43,
                  "charByteOffset": 13
                }
              }
            },
            "twoStateIndex": "NEITHER"
          }
        },
        "o2": {
          "out": {
            "#class": "vc.data.TACSymbol.Var.Full",
            "namePrefix": "CANON110",
            "tag": {
              "#class": "tac.Tag.Int"
            },
            "callIndex": 0
          },
          "exp": {
            "#class": "spec.cvlast.CVLExp.Constant.NumberLit",
            "n": "1",
            "tag": {
              "scope": {
                "scopeStack": [
                  {
                    "#class": "spec.cvlast.CVLScope.Item.AstScopeItem"
                  },
                  {
                    "#class": "spec.cvlast.CVLScope.Item.RuleScopeItem",
                    "scopeId": 2
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
                "n": "1"
              },
              "range": {
                "#class": "utils.Range.Range",
                "specFile": "Basic.spec",
                "start": {
                  "line": 43,
                  "charByteOffset": 17
                },
                "end": {
                  "line": 43,
                  "charByteOffset": 18
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
        "specFile": "Basic.spec",
        "start": {
          "line": 43,
          "charByteOffset": 4
        },
        "end": {
          "line": 43,
          "charByteOffset": 19
        }
      }
    }
  ],
  "189": [
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
        "specFile": "Basic.spec",
        "start": {
          "line": 43,
          "charByteOffset": 4
        },
        "end": {
          "line": 43,
          "charByteOffset": 19
        }
      }
    }
  ]
}