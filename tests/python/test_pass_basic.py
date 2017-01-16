import tvm

def test_simplify():
  x = tvm.Var('x')
  e1 = tvm.ir_pass.Simplify(x + 2 + 1)
  assert(tvm.ir_pass.Equal(e1, x + 3))
  e2 = tvm.ir_pass.Simplify(x * 3 + 5 * x)
  assert(tvm.ir_pass.Equal(e2, x * 8))
  e3 = tvm.ir_pass.Simplify(x - x / 3 * 3)
  assert(tvm.ir_pass.Equal(e3, tvm.make.Mod(x, 3)))


def test_verify_ssa():
    x = tvm.Var('x')
    y = tvm.Var()
    z = tvm.make.Evaluate(x + y)
    assert(tvm.ir_pass.VerifySSA(z))


def test_convert_ssa():
    x = tvm.Var('x')
    y = tvm.Var()
    let = tvm.make.Let(x, 1, x + 1)
    z = tvm.make.Evaluate(let + let)
    assert(not tvm.ir_pass.VerifySSA(z))
    z_ssa = tvm.ir_pass.ConvertSSA(z)
    assert(tvm.ir_pass.VerifySSA(z_ssa))
