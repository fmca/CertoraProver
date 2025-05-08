methods {
    function foo(uint) external returns bool envfree;
}

rule inParallel {
    bool b;
    uint a;
    uint x;
    if (b) {
        require a > 10; // not a function-input-require
    } else {
        foo(a);
    }
    assert true;
}

rule orderDoesNotMatter {
    uint a;
    bool b = foo(a);
    require a > 11; // actually a function-input, the require also affects what comes before it
    assert b;
}

rule moreComplicated {
    uint a;
    bool b;
    if (b) {
        require a > 12; // function-input
    }
    assert foo(a);
}

rule moreComplicatedOutOfOrder {
    uint a;
    bool b;
    bool res = foo(a);
    if (b) {
        require a > 13; // function-input
    }
    assert res;
}

rule moreComplicated2 {
    uint a;
    bool b;
    require a > 14; // function-input
    bool res = a > 1;
    if (b) {
        res = foo(a);
    }
    assert res;
}

rule moreComplicated2OutOfOrder {
    uint a;
    bool b;
    bool res = a > 1;
    if (b) {
        res = foo(a);
    }
    require a > 15; // function-input
    assert res;
}

rule nowWeAreJustMean {
    uint a;
    bool b;
    if (!b) {
        require a > 16; // technically not function-input - path conditions are mutually exclusive. Not realistic for us to analyse for this though.
    }
    bool res = true;
    if (b) {
        res = foo(a);
    }
    assert res;
}
