use super::intrinsics::*;

#[inline(never)]
fn a_function() -> u64 {
    cvt_nondet_u64!()
}

#[inline(never)]
fn calls_a_function() -> u64 {
    a_function()
}

#[no_mangle]
pub fn rule_function_call_in_main_body() {
    let x = a_function();
    cvt_assert_with_location!(x < 10);
}

#[no_mangle]
pub fn rule_nested_function_call_in_main_body() {
    let x = calls_a_function();
    cvt_assert_with_location!(x < 10);
}
