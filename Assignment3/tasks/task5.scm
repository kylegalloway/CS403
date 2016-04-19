(include "extras/exprTest.scm")

(define (mmutex n)
    (define number n)
    (define owners '())

    (define (included5? x L)
        (if (null? L)
            #f
            (begin
                (if (== (car L) x)
                    #t
                    (included5? x (cdr L))
                )
            )
        )
    )

    (define (list-remove x L)
        (if (== (car L) x)
            (cdr L)
            (cons (car L) (list-remove x (cdr L)))
        )
    )

    (define (p)
        ; lock the semaphore
        (lock)
        ; check if there is an open slot to take
        (if (> number 0)
            (begin
                ; decrease the number of slots left
                (set! number (- number 1))
                ; add the id to the owners array
                (set! owners (cons (gettid) owners))
                ; unlock the semaphore
                (unlock)
                'ACQUIRED
            )
            (begin
                ; can't get in the owners array, so unlock and try again
                (unlock)
                (p)
            )
        )
    )
    (define (v)
        (lock)
        (if (included5? (gettid) owners)
            (begin
                (set! number (+ number 1))
                (set! owners (list-remove (gettid) owners))
                (unlock)
                'RELEASED
            )
            (begin
                (unlock)
                'FORBIDDEN
            )
        )
    )
    this
)

(define (run5)
    (define m (mmutex 3))
    (exprTest ((m'p)) 'ACQUIRED)
    (exprTest ((m'v)) 'RELEASED)
    (define x (mmutex 0))
    (exprTest ((x'v)) 'FORBIDDEN)
)