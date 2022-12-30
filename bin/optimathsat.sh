#! /bin/sh
optimathsat -opt.fzn.all_solutions=true -opt.fzn.all_solutions=true -opt.fzn.finite_precision=12 -opt.fzn.finite_precision_model=true -input=fzn "$1"