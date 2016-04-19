(include "extras/exprTest.scm")

(define (included1? x L)
    (if (null? L)
        #f
        (if (== (car L) x)
            #t
            (included1? x (cdr L))
        )
    )
)

(define (level # id)
    (define (env-iter env id count)
        (cond
            ((== env 'nil) 'UNDEFINED)
            ((included1? id (cadr env)) count)
            (else
                (env-iter (get'__context env) id (+ count 1))
            )
        )
    )
    (env-iter # id 0)
)

; Tests
(define a 4)

(define (f x y)
    (inspect (level 'a))
    (inspect (level 'b))
    (* (+ x y) a)
)

(define (h x y)
    (define (g)
        (inspect (level 'a))
        (inspect (level 'b))
        (* (+ x y) a)
    )
    (g)
)

(define (s)
    (define b 3)
    (lambda (x y)
        (inspect (level 'a))
        (inspect (level 'b))
        (* (+ x y) a b)
    )
)

(define (run1)
    (f 1 2)
    (h 1 2)
    ((s) 1 2)
)