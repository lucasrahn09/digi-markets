from flask import abort, Blueprint, request
from flask_restful import Api
from .network import BlockchainNetworkListAPI, BlockchainNetworkAPI
from .nft_account import NFTAccountAPI, NFTAccountTransfersAPI
from .nft_contract import NFTContractSearchAPI, NFTContractMetadataAPI
from .nft_token import NFTTokenAPI, NFTTokenTransfersAPI, NFTTokenListAPI
from .token_uri import FetchTokenURIAPI
import logging

logger = logging.getLogger('src.resources')

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(NFTAccountAPI, '/nft/eoa/<string:address>')
api.add_resource(NFTAccountTransfersAPI, '/nft/eoa/<string:address>/transfers')
api.add_resource(NFTTokenListAPI, '/nft/contract/<string:address>')
api.add_resource(
    NFTTokenAPI, '/nft/contract/<string:address>/<int:token_id>')
api.add_resource(
    NFTTokenTransfersAPI, '/nft/contract/<string:address>/<int:token_id>/transfers')
api.add_resource(NFTContractMetadataAPI,
                 '/nft/contract/<string:address>/metadata')
api.add_resource(NFTContractSearchAPI, '/nft/contract/search')

api.add_resource(BlockchainNetworkAPI, '/network/<int:chain_id>')
api.add_resource(BlockchainNetworkListAPI, '/network')
api.add_resource(FetchTokenURIAPI, '/token_uri')


@api_bp.before_request
def require_api_key():
    logger.info(request.url)
