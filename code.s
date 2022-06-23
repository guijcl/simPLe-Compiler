	.text
	.file	"code.ll"
	.globl	main                    # -- Begin function main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# %bb.0:
	xorl	%eax, %eax
	retq
.Lfunc_end0:
	.size	main, .Lfunc_end0-main
	.cfi_endproc
                                        # -- End function
	.type	pont_pi,@object         # @pont_pi
	.bss
	.globl	pont_pi
	.p2align	2
pont_pi:
	.long	0                       # 0x0
	.size	pont_pi, 4

	.section	".note.GNU-stack","",@progbits
