(define scons cons-stream)
(define scar stream-car)
(define scdr stream-cdr)

(define (ints-from n)
    (scons n (ints-from (+ n 1)))
)

(define (floats-from n)
    (scons (* 1.0 n) (floats-from (+ n 1)))
)

(define (sdisplay s n)
    (cond
        ((= n 0) (print "...\n"))
        (else
            (print (scar s) " ")
            (sdisplay (scdr s) (- n 1))
        )
    )
)

(define (add-streams s t)
    (scons
        (+ (scar s) (scar t))
        (add-streams (scdr s) (scdr t))
    )
)

(define (sub-streams s t)
    (scons
        (- (scar s) (scar t))
        (sub-streams (scdr s) (scdr t))
    )
)

(define (mult-streams s t)
    (scons
        (* (scar s) (* 1.0 (scar t)))
        (mult-streams (scdr s) (scdr t))
    )
)

(define (div-streams s t)
    (scons
        (/ (scar s) (* 1.0 (scar t)))
        (div-streams (scdr s) (scdr t))
    )
)

(define ones (scons 1 ones))
(define alt-ones (scons 1 (scons -1 alt-ones)))
(define neg-ones (scons -1 neg-ones))
(define twos (scons 2 twos))
(define odds (scons 1 (add-streams twos odds)))
(define evens (scons 2 (add-streams twos evens)))
(define ints (scons 1 (add-streams ones ints)))
(define fibs (scons 0 (scons 1 (add-streams fibs (scdr fibs)))))

(define (sremove p? s)
    (if (p? (scar s))
        (sremove p? (scdr s))
        (scons (scar s) (sremove p? (scdr s)))
    )
)

(define (divides? x y) (= (% x y) 0))

(define (sieve s)
    (scons
        (scar s)
        (sieve (sremove (lambda (x) (divides? x (scar s))) (scdr s)))
    )
)

; PI/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 ...
; Need alt-ones / odds
(define pi-by-4-stream (div-streams alt-ones odds))

; ; Partial Sum
; (define (psum s)
;     (scons
;         (scar s)
;         (psum
;             (scons
;                 (+ (scar s) (scar (scdr s)))
;                 (scdr (scdr s))
;             )
;         )
;     )
; )

(define (psum s)
    (scons
        (scar s)
        (add-streams
            (psum s)
            (scdr s)
        )
    )
)

(define (sscale s x)
    (scons
        (* x (scar s))
        (sscale (scdr s) x)
    )
)

; Tableau
(define (tableau xform s) (scons s (tableau xform (xform s))))

; Stream-map
(define (smap f s) (scons (f (scar s)) (smap f (scdr s))))

(define (euler-transform s)
    (define s0 (scar s))
    (define s1 (scar (scdr s)))
    (define s2 (scar (scdr (scdr s))))
    (define denominator (+ s0 ( * -2 s1) s2))
    (if (= denominator 0)
        (scons s0 (euler-transform (scdr s)))
        (scons
            (- s2 (/ (^ (- s2 s1) 2) denominator))
            (euler-transform (scdr s))
        )
    )
)

(define (sshuffle s t)
    (scons
        (scar s)
        (sshuffle t (scdr s))
    )
)

(define (pairs s t)
    (scons
        (list (scar s) (scar t))
        (sshuffle
            (smap (lamda (x) (list (scar s) x)) (scdr t))
            (pairs (scdr s) (scdr t))
        )
    )
)


(define (smerge s1 s2)
   (cond
        ((null? s1) s2)
        ((null? s2) s1)
        (else
            (cond
                ((< (scar s1) (scar s2))
                 (scons (scar s1) (smerge (scdr s1) s2))
                )
                ((> (scar s1) (scar s2))
                 (scons (scar s2) (smerge s1 (scdr s2)))
                )
                (else
                    (scons
                        (scar s1)
                        (smerge
                            (scdr s1)
                            (scdr s2)
                        )
                    )
                )
            )
        )
    )
)