(include "extras/exprTest.scm")
(include "pretty.lib")

(define (denv f) (get'__context f))

(define (included? x L)
    (if (null? L)
        #f
        (begin
            (if (== (car L) x)
                #t
                (included? x (cdr L))
            )
        )
    )
)

(define (cache f)
    ; capture the local variables (parameters)
    (define local-ids (get 'parameters f))
    ; iterate through the code
    (define (iter expr)
        (cond
            ; if the expr is a pair, and the car is define
            ; add the defined id to the local-ids list
            ; and iterate through the cddr to keep going
            ((pair? expr)
                (if (eq? (car expr) 'define)
                    (begin
                        (if (pair? (cadr expr))
                            (set! local-ids (append (cadr expr) local-ids))
                            (set! local-ids (cons (cadr expr) local-ids))
                        )
                        (inspect local-ids)
                        (cons 'define (cons (cadr expr) (iter (cddr expr))))
                    )
                    (cons (iter (car expr)) (iter (cdr expr)))
                )
            )
            ((included? expr local-ids) expr)
            (else (eval expr (denv f)))
        )
    )
    (set* f'code (cons 'begin (cdr (iter (get 'code f)))))
)

(define (run2)
    (define m 2)
    (define (msquare x) (* m x x))
    (pretty msquare)
    (cache msquare)
    (pretty msquare)
    (newline)
    (newline)
    (define a 1)
    (define b 2)
    (define (f x y)
        (define c 3)
        (define (g)
            (+ a b c x y)
        )
        (g)
    )
    (pretty f)
    (cache f)
    (pretty f)
)
