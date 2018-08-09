import pytest

@pytest.fixture(scope='function')
def functionFixture(request):
	print('\nSetting "functionFixture" up')
	def finalizer():
		print('\nFinalizing "functionFixture"')
	request.addfinalizer(finalizer)
	return 1

@pytest.fixture(scope='module')
def moduleFixture(request):
	print('\nSetting "moduleFixture" up')
	def finalizer():
		print('\nFinalizing "moduleFixture"')
	request.addfinalizer(finalizer)
	return 10

@pytest.fixture(scope='module')
def yield_fixture():
	print('\nSetting "yield_fixture" up. scope=module')
	yieldedValue = 3.14
	yield yieldedValue
	print('\nFinalizing "yield_fixture"')

@pytest.mark.basic
def test_assert(moduleFixture):
	print('\nassert test using moduleFixture')
	assert moduleFixture == 10

@pytest.mark.mid_level
def test_list(moduleFixture):
	print('\nlist test using moduleFixture')
	a = [1, 2, 3]
	b = [10, 20, 30]
	assert [moduleFixture*x for x in a] == b

@pytest.mark.with_yield
def test_yield_fixture(yield_fixture):
	assert yield_fixture == 3.14

def square(x):
	return x*x

@pytest.mark.advanced
@pytest.mark.parametrize('input, expected', [(2,4), (3,9), (5,25)])
def test_parametrized(functionFixture, input, expected):
	print('\nparametrized test using functionFixture')
	assert expected == input**2
	assert functionFixture == 1