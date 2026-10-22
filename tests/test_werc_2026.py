"""Independent synthetic checks, including exact values in the author's paper."""
import numpy as np
from classroom.graphs.werc_2026 import softmax, nash_equilibrium, resource_equilibrium, cooperation_margin, make_network


def test_softmax_common_shift():
    q=[3.,7.,2.];assert np.allclose(softmax(q),softmax(np.array(q)+200.))
    assert np.isclose(softmax([80,80])[0],.5)


def test_star_vs_path_exact():
    star=np.zeros((4,4));path=np.zeros((4,4))
    for j in (1,2,3):star[0,j]=star[j,0]=1
    for i in range(3):path[i,i+1]=path[i+1,i]=1
    xs,rhos=nash_equilibrium(star,alpha=.2)
    xp,rhop=nash_equilibrium(path,alpha=.2)
    assert np.allclose(xs,[20/11,15/11,15/11,15/11],atol=1e-11)
    assert np.allclose(xp,[25/19,30/19,30/19,25/19],atol=1e-11)
    assert np.isclose(xs.sum(),65/11) and np.isclose(xp.sum(),110/19)


def test_resource_shadow_exact():
    star=np.zeros((4,4))
    for j in (1,2,3):star[0,j]=star[j,0]=1
    x,mu,bound=resource_equilibrium(star,capacity=4,eta=.2)
    assert bound and np.isclose(mu,21/65)
    assert np.allclose(x,[16/13,12/13,12/13,12/13])
    assert np.isclose(x.sum(),4)
    x,mu,bound=resource_equilibrium(star,capacity=12,eta=.2)
    assert not bound and mu==0


def test_incentive_threshold():
    # G=.8, d=.5, P=.25, deltaU=.6 => delta*=.675/(.675+.3)
    threshold=(.8-.5*.25)/(.8-.5*.25+.5*.6)
    assert np.isclose(threshold,9/13)
    assert abs(cooperation_margin(.8,.5,.25,threshold,.6))<1e-10


def test_synthetic_networks():
    for family in ('ER','WS','BA','SBM'):
        a=make_network(family,24,48,seed=20261020)
        assert a.shape==(24,24) and int(a.sum())==96
        assert (a==a.T).all() and np.all(np.diag(a)==0)
        assert np.array_equal(a,make_network(family,24,48,seed=20261020))


def test_reject_spectral_violation():
    w=np.ones((4,4))-np.eye(4)
    try: nash_equilibrium(w,alpha=0.5)
    except ValueError: pass
    else: raise AssertionError("Must reject unstable inverse")
