import React from 'react';
import { graphql } from 'gatsby';
import Layout from '../components/layout';
import styled from 'styled-components';

const Blog = ({ data }) => {
  return (
    <Layout title="Blog">
      <HeaderWrapper>
        <h1>Comps - US 🇺🇸</h1>
        <p>Coming Soon!</p>
       </HeaderWrapper>
    </Layout>
  );
};

export default Blog;

const HeaderWrapper = styled.div`
  display: flex;
  flex-direction: column;
  margin-top: var(--size-900);
  margin-bottom: var(--size-700);

  h1 {
    max-width: none;
  }
`;

export const homePageQuery = graphql`
  query {
    site {
      siteMetadata {
        title
      }
    }
    allMarkdownRemark(
      filter: { fields: { contentType: { eq: "posts" } } }
      sort: { order: ASC, fields: frontmatter___date }
    ) {
      nodes {
        fields {
          slug
        }
        excerpt
        frontmatter {
          date(formatString: "MMMM DD, YYYY")
          description
          title
          tags
          price
          location
        }
      }
    }
  }
`;
