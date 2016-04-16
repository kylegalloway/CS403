(define (level # id)
    (define spot (find-position (cadr (get'__context)) id))
    ; (list-ref (caddr (get'__context)) spot)
    (define (env-iter env id count)
        (if (== spot 'UNDEFINED)
            (if (null? (env'__context))
                spot
                (env-iter (env'__context) id (+ count 1))
            )
            count
        )
    )
    (env-iter (get'__context) id 0)
)

(define (find-position L x)
    (define (iter L x count)
        (if (null? L)
            'UNDEFINED
            (if (== (car L) x)
                count
                (iter (cdr L) x (+ count 1))
            )
        )
    )
    (iter L x 0)
)

(define (list-ref L n)
    (if (= n 0)
        (car L)
        (list-ref (cdr L) (- n 1))
    )
)

; Tests
(define a 4)
(define (f x y)
    (inspect (level 'a))
    (inspect (level 'b))
    (* (+ x y) a)
)
(define s
    (define (g x y)
        (inspect (level 'a))
        (inspect (level 'b))
        (* (+ x y) a)
    )
    (define (this msg @)
        (cond
            ((eq? msg 'g) (g (car @) (cadr @)))
            (else (error "Message not understood: " msg))
        )
    )
    this
)

; (define (run1)
;     (f 1 2)
;     (s'f 1 2)
; )