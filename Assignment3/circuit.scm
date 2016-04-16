(include "priority-queue.scm")
(include "wire.scm")
(include "and-gate.scm")
(include "or-gate.scm")
(include "inverter.scm")
(include "probe.scm")
(include "adders.scm")

(define (and-test)
    (define q (pq))

    (define a (wire))
    (define b (wire))
    (define c (wire))

    (probe q a 'a)
    (probe q b 'b)
    (probe q c 'c)

    (and-gate q a b c)

    ((get 'set a) 1)
    ((get 'set b) 1)

    ((q'go))
)

(define (inverter-test)
    (define q (pq))

    (define a (wire))
    (define b (wire))

    (probe q a 'a)
    (probe q b 'b)

    (inverter q a b)

    ((get 'set a) 0)

    ((q'go))
)

(define (or-test)
    (define q (pq))

    (define a (wire))
    (define b (wire))
    (define c (wire))

    (probe q a 'a)
    (probe q b 'b)
    (probe q c 'c)

    (or-gate q a b c)

    ((get 'set a) 1)
    ((get 'set b) 0)

    ((q'go))
)

(define (halfadder-test)
    (define q (pq))

    (define a (wire))
    (define b (wire))
    (define sum (wire))
    (define c-out (wire))

    (probe q a 'a)
    (probe q b 'b)
    (probe q sum 'sum)
    (probe q c-out 'c-out)

    (half-adder q a b sum c-out)

    ((get 'set a) 1)
    ((get 'set b) 0)

    ((q'go))
)

(define (fulladder-test)
    (define q (pq))

    (define a (wire))
    (define b (wire))
    (define sum (wire))
    (define c-in (wire))
    (define c-out (wire))

    (probe q a 'a)
    (probe q b 'b)
    (probe q sum 'sum)
    (probe q c-in 'c-in)
    (probe q c-out 'c-out)

    (full-adder q a b c-in sum c-out)

    ((get 'set a) 1)
    ((get 'set b) 1)

    ((q'go))
)

; (and-test)
; (inverter-test)
; (or-test)
; (halfadder-test)
(fulladder-test)