use super::intrinsics::*;

#[no_mangle]
pub fn rule_print_simple_struct() {
    unsafe {
        cvt_scope_start_with_location!("someStruct");
        CVT_calltrace_print_u64_1("fieldOfStruct", 1);
        CVT_calltrace_scope_end("someStruct");
        CVT_assert(false)
    }
}

#[no_mangle]
pub fn rule_print_nested_struct() {
    unsafe {
        cvt_scope_start_with_location!("someStruct");
        CVT_calltrace_print_u64_1("fieldOfStruct", 1);
        cvt_scope_start_with_location!("nestedStruct");
        CVT_calltrace_print_u64_1("fieldOfNestedStruct", 1);
        CVT_calltrace_scope_end("nestedStruct");
        CVT_calltrace_scope_end("someStruct");
        CVT_assert(false)
    }
}

#[no_mangle]
pub fn rule_print_incorrectly_balanced_struct1() {
    unsafe {
        cvt_scope_start_with_location!("someStruct");
        CVT_calltrace_print_u64_1("fieldOfStruct", 1);
        CVT_calltrace_scope_end("someStruct");
        CVT_calltrace_scope_end("someStruct");
        CVT_assert(false)
    }
}

#[no_mangle]
pub fn rule_print_incorrectly_balanced_struct2() {
    unsafe {
        cvt_scope_start_with_location!("someStruct");
        CVT_calltrace_print_u64_1("fieldOfStruct", 1);
        CVT_assert(false)
    }
}
