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
    (define y (mmutex 3))
    (exprTest ((y'p)) 'ACQUIRED)
    (exprTest ((y'v)) 'RELEASED)

    (define x (mmutex 0))
    (exprTest ((x'v)) 'FORBIDDEN)

    (define m (mmutex 3))
    (define t1
        (thread
            (begin
                (println "Thread 1 " ((m'p)))
                (println "Thread 1 Started")
                (sleep 1)
                (println "Thread 1 " ((m'v)))
                (println "Thread 1 " ((m'v)))
                (println "Thread 1 " ((m'v)))
                (println "Thread 1 Finished")
            )
        )
    )
    (define t2
        (thread
            (begin
                (println "Thread 2 " ((m'p)))
                (println "Thread 2 Started")
                (sleep 1)
                (println "Thread 2 " ((m'v)))
                (println "Thread 2 Finished")
            )
        )
    )
    (define t3
        (thread
            (begin
                (println "Thread 3 " ((m'p)))
                (println "Thread 3 " ((m'p)))
                (println "Thread 3 Started")
                (sleep 1)
                (println "Thread 3 " ((m'v)))
                (println "Thread 3 " ((m'v)))
                (println "Thread 3 Finished")
            )
        )
    )
    (define t4
        (thread
            (begin
                (println "Thread 4 " ((m'p)))
                (println "Thread 4 Started")
                (sleep 1)
                (println "Thread 4 " ((m'v)))
                (println "Thread 4 Finished")
            )
        )
    )
    (define t5
        (thread
            (begin
                (println "Thread 5 " ((m'p))) (println "Thread 5 " ((m'p)))
                (println "Thread 5 Started") (sleep 1) (println "Thread 5 " ((m'v))) (println "Thread 5 " ((m'v))) (println "Thread 5 " ((m'v)))
            )
        )
    )
    (tjoin t1)
    (tjoin t2)
    (tjoin t3)
    (tjoin t4)
    (tjoin t5)
)