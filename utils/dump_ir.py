import tvm
import os
import shutil

@tvm.instrument.pass_instrument
class DumpIR:
    def __init__(self) -> None:
        self.counts = 0
        self.root_dir = "dump_ir"
        if os.path.exists(self.root_dir):
            shutil.rmtree(self.root_dir)
        os.makedirs(self.root_dir, mode=0o700)

    def run_after_pass(self, mod, info):
        pname = str(self.counts).rjust(5, "0")+"_"+info.name +".ir.cc"
        pname = os.path.join(self.root_dir, pname)
        with open(pname, "w") as f:
            f.write(mod.astext(show_meta_data=False))
        self.counts += 1
